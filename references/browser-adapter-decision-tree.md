# Browser Adapter Decision Tree

Use this file when browser adapter selection should be expressed in a
machine-friendly form instead of loose prose.

This file complements:

- [browser-adapter-best-practices.md](./browser-adapter-best-practices.md)
- [execution-preflight.md](./execution-preflight.md)
- [dispatch-contract.md](./dispatch-contract.md)

## Goal

Make adapter choice reproducible.

The agent should first normalize the situation into structured metadata, then
emit a structured decision record.

## Input Metadata Schema

Use this JSON shape before choosing `playwright`, `chrome-devtools`, or
`computer-use`:

```json
{
  "task_id": "string",
  "target_site": "gemini | other",
  "requires_existing_logged_in_tab": true,
  "requires_existing_debug_context": false,
  "requires_manual_to_agent_handoff": true,
  "requires_repeatable_dom_automation": false,
  "requires_browser_only_feature": true,
  "requires_os_level_interaction": false,
  "session_priority": "existing_session | managed_session | either",
  "login_state_source_needed": "existing_browser | storage_state | persistent_profile | none",
  "host_surfaces": {
    "playwright": "full | thin | none",
    "chrome_devtools": "full | attach_only | none",
    "computer_use": "available | none"
  },
  "host_surface_evidence": {
    "playwright": "tool discovery summary or null",
    "chrome_devtools": "tool discovery summary or null",
    "computer_use": "tool discovery summary or null"
  },
  "surface_discovery_status": "verified | assumed | mixed",
  "session_attach_readiness": {
    "chrome_devtools_existing_session": "ready | blocked | unknown",
    "playwright_existing_tab_bridge": "ready | blocked | unknown"
  },
  "session_attach_evidence": {
    "chrome_devtools_existing_session": "proof or blocker summary",
    "playwright_existing_tab_bridge": "proof or blocker summary"
  },
  "host_constraints": {
    "sandboxed_client": false,
    "approval_gating": false,
    "download_sensitive": true
  },
  "site_constraints": {
    "hover_reveal_controls": true,
    "single_flight_download": true,
    "effective_click_requires_active_state": true,
    "local_file_success_required": true,
    "materialization_delay_expected": true
  },
  "download_observability": {
    "network_evidence_available": true,
    "effective_click_evidence": "spinner | loading state | network request | unknown",
    "materialization_grace_window_seconds": 20
  }
}
```

### Field Meaning

- `requires_existing_logged_in_tab`
  - true when the user's already open authenticated page matters
- `requires_existing_debug_context`
  - true when the run needs current Elements, Network, or live DevTools state
- `requires_manual_to_agent_handoff`
  - true when the user is already manually driving the site and wants the agent
    to continue in the same session
- `requires_repeatable_dom_automation`
  - true when deterministic locators, repeatability, and reruns matter more
    than existing session reuse
- `requires_browser_only_feature`
  - true when the target workflow only exists in the website
- `requires_os_level_interaction`
  - true when the task depends on front-window UI or desktop-only interaction
- `session_priority`
  - use `existing_session` when a clean browser is insufficient
- `login_state_source_needed`
  - use `existing_browser` when current real login state is essential
- `host_surfaces`
  - describe what this host actually exposes, not what the adapter name implies
- `host_surface_evidence`
  - concise proof for each surface, such as `tabs-only tools`, `connect plus
    JS execute`, or `app screenshot plus accessibility tree`
- `surface_discovery_status`
  - use `verified` when tool discovery or direct probing established the
    surface, `assumed` when it is only a scenario hypothesis, and `mixed` when
    some surfaces were verified but others were inferred
- `session_attach_readiness`
  - separate "tool exists" from "the target existing session is actually
    reachable"
- `session_attach_evidence`
  - concise proof such as `Chrome on 9226 is Gemini login page, not the
    authenticated front browser`
- `site_constraints.effective_click_requires_active_state`
  - true when a raw click is not enough and the run must observe loading or
    request evidence before treating the download as started
- `site_constraints.local_file_success_required`
  - true when on-page preview state is insufficient and only a local file
    verifies success
- `site_constraints.materialization_delay_expected`
  - true when the site may start a download but write the local file after a
    noticeable delay
- `download_observability`
  - records what evidence is available to confirm that a click became effective
    and what grace window should be allowed before retry

## Output Decision Schema

After normalization, emit this JSON decision:

```json
{
  "recommended_adapter": "chrome-devtools | playwright | computer-use | prompt-only",
  "session_model": "existing_session_attach | managed_persistent | managed_isolated | front_window_control",
  "fallback_adapter": "chrome-devtools | playwright | computer-use | prompt-only",
  "reason_codes": [
    "existing_session_required",
    "managed_automation_preferred",
    "host_surface_thin",
    "browser_only_feature",
    "os_level_interaction_required"
  ],
  "blockers": [],
  "prohibited_moves": [
    "do_not_copy_live_profile",
    "do_not_assume_playwright_inherits_manual_login"
  ],
  "download_policy": {
    "single_flight": true,
    "effective_click_required": true,
    "local_file_success_required": true,
    "materialization_grace_window_seconds": 20
  },
  "confidence": "high | medium | low",
  "evidence_quality": "verified | mixed | assumed"
}
```

## Deterministic Decision Tree

Apply these rules in order:

1. If `requires_existing_debug_context = true`, choose `chrome-devtools`.
   Output:
   - `recommended_adapter = chrome-devtools`
   - `session_model = existing_session_attach`
   - `reason_codes += ["existing_debug_context_required"]`

2. Else if `requires_existing_logged_in_tab = true` or
   `requires_manual_to_agent_handoff = true`:
   - choose `chrome-devtools` only if
     `session_attach_readiness.chrome_devtools_existing_session = ready`
   - else choose `playwright` only if
     `session_attach_readiness.playwright_existing_tab_bridge = ready`
   - else choose `computer-use`
   - `reason_codes += ["existing_session_required"]`
   - if both existing-session paths are blocked, add
     `reason_codes += ["existing_session_attach_blocked"]`

3. Else if `requires_repeatable_dom_automation = true`:
   - choose `playwright`
   - prefer `managed_isolated` or `managed_persistent`
   - `reason_codes += ["repeatable_dom_automation_required"]`

4. Else if browser-native surfaces are thin:
   - if both `playwright` and `chrome_devtools` are thin or none, choose
     `computer-use`
   - `reason_codes += ["host_surface_thin"]`

5. Else if the task is browser-only but session origin is flexible:
   - prefer `chrome-devtools` for existing-session-oriented work
   - prefer `playwright` for clean repeatable automation

6. If `site_constraints.effective_click_requires_active_state = true`:
   - require the run plan to define `download_observability.effective_click_evidence`
   - do not allow `button was pressed` to count as download start by itself

7. If `site_constraints.materialization_delay_expected = true`:
   - require a positive `materialization_grace_window_seconds`
   - prohibit immediate re-click or reroute before that window expires unless a
     hard blocker is observed

8. Never choose profile copying as the default answer for existing-session
   problems.
   - `prohibited_moves += ["do_not_copy_live_profile"]`

9. Confidence must track discovery quality:
   - if `surface_discovery_status = verified`, confidence may be `high`
   - if `surface_discovery_status = mixed`, default confidence to at most
     `medium`
   - if `surface_discovery_status = assumed`, default confidence to `low` unless
     the run is only a hypothetical routing exercise

## Gemini-Specific Overlay

For Gemini website work, add these constraints before finalizing the decision:

```json
{
  "target_site": "gemini",
  "site_constraints": {
    "hover_reveal_controls": true,
    "single_flight_download": true,
    "effective_click_requires_active_state": true,
    "local_file_success_required": true,
    "materialization_delay_expected": true
  },
  "download_observability": {
    "network_evidence_available": true,
    "effective_click_evidence": "spinner | loading state | network request",
    "materialization_grace_window_seconds": 20
  }
}
```

Interpretation:

- if the run needs the user's already open Gemini tab, prefer
  `chrome-devtools` existing-session attach
- if the run can start from a managed authenticated state, Playwright is valid
  only when the session source is explicit such as persistent profile,
  `storage-state`, or an existing-tab bridge
- if the host only exposes tab-level Playwright tools and attach-only
  DevTools tools, say the surfaces are thin and avoid pretending either is a
  full DOM automation answer

## Worked Example: Gemini Existing Session

Input:

```json
{
  "task_id": "gemini-p1-infographic",
  "target_site": "gemini",
  "requires_existing_logged_in_tab": true,
  "requires_existing_debug_context": false,
  "requires_manual_to_agent_handoff": true,
  "requires_repeatable_dom_automation": false,
  "requires_browser_only_feature": true,
  "requires_os_level_interaction": false,
  "session_priority": "existing_session",
  "login_state_source_needed": "existing_browser",
  "host_surfaces": {
    "playwright": "thin",
    "chrome_devtools": "attach_only",
    "computer_use": "available"
  },
  "host_surface_evidence": {
    "playwright": "host exposes only tab-level Playwright actions",
    "chrome_devtools": "host exposes browser connect and JS execution against a debuggable Chrome session",
    "computer_use": "host exposes app screenshot plus accessibility tree"
  },
  "surface_discovery_status": "verified",
  "session_attach_readiness": {
    "chrome_devtools_existing_session": "ready",
    "playwright_existing_tab_bridge": "blocked"
  },
  "session_attach_evidence": {
    "chrome_devtools_existing_session": "existing debuggable Chrome session is the actual logged-in Gemini tab",
    "playwright_existing_tab_bridge": "no extension-based existing-tab bridge configured"
  },
  "host_constraints": {
    "sandboxed_client": false,
    "approval_gating": false,
    "download_sensitive": true
  },
  "site_constraints": {
    "hover_reveal_controls": true,
    "single_flight_download": true,
    "effective_click_requires_active_state": true,
    "local_file_success_required": true,
    "materialization_delay_expected": true
  },
  "download_observability": {
    "network_evidence_available": true,
    "effective_click_evidence": "spinner or request evidence",
    "materialization_grace_window_seconds": 20
  }
}
```

Output:

```json
{
  "recommended_adapter": "chrome-devtools",
  "session_model": "existing_session_attach",
  "fallback_adapter": "computer-use",
  "reason_codes": [
    "existing_session_required",
    "manual_to_agent_handoff_required",
    "browser_only_feature",
    "playwright_surface_too_thin",
    "download_sensitive_workflow",
    "gemini_existing_tab_preferred"
  ],
  "blockers": [],
  "prohibited_moves": [
    "do_not_copy_live_profile",
    "do_not_assume_playwright_inherits_manual_login"
  ],
  "download_policy": {
    "single_flight": true,
    "effective_click_required": true,
    "local_file_success_required": true,
    "materialization_grace_window_seconds": 20
  },
  "confidence": "high",
  "evidence_quality": "verified"
}
```

Interpretation:

- the task needs the user's current logged-in Gemini page
- Playwright is not rejected in theory, but the exposed host surface is too thin
- Chrome DevTools attach is the correct first answer
- `computer-use` remains the fallback if the exposed DevTools surface cannot
  complete the interaction

## Worked Example: Current Host, Logged-In Front Chrome, No Reachable Attach

Input:

```json
{
  "task_id": "chrome-gemini-front-window-current-host",
  "target_site": "gemini",
  "requires_existing_logged_in_tab": true,
  "requires_existing_debug_context": false,
  "requires_manual_to_agent_handoff": true,
  "requires_repeatable_dom_automation": false,
  "requires_browser_only_feature": true,
  "requires_os_level_interaction": false,
  "session_priority": "existing_session",
  "login_state_source_needed": "existing_browser",
  "host_surfaces": {
    "playwright": "thin",
    "chrome_devtools": "attach_only",
    "computer_use": "available"
  },
  "host_surface_evidence": {
    "playwright": "host exposes only tab-level Playwright tools",
    "chrome_devtools": "host can connect to debuggable Chrome ports and execute JS",
    "computer_use": "host can inspect the front Chrome window via screenshot plus accessibility tree"
  },
  "surface_discovery_status": "verified",
  "session_attach_readiness": {
    "chrome_devtools_existing_session": "blocked",
    "playwright_existing_tab_bridge": "blocked"
  },
  "session_attach_evidence": {
    "chrome_devtools_existing_session": "reachable Chrome debug sessions on 9225/9226 are Gemini login pages, while the real logged-in Chrome front window is not the debuggable target",
    "playwright_existing_tab_bridge": "no verified existing-tab bridge is available in this host"
  },
  "host_constraints": {
    "sandboxed_client": false,
    "approval_gating": false,
    "download_sensitive": true
  },
  "site_constraints": {
    "hover_reveal_controls": true,
    "single_flight_download": true,
    "effective_click_requires_active_state": true,
    "local_file_success_required": true,
    "materialization_delay_expected": true
  },
  "download_observability": {
    "network_evidence_available": false,
    "effective_click_evidence": "visible loading only",
    "materialization_grace_window_seconds": 20
  }
}
```

Output:

```json
{
  "recommended_adapter": "computer-use",
  "session_model": "front_window_control",
  "fallback_adapter": "prompt-only",
  "reason_codes": [
    "existing_session_required",
    "manual_to_agent_handoff_required",
    "browser_only_feature",
    "existing_session_attach_blocked",
    "download_sensitive_workflow",
    "gemini_existing_tab_preferred"
  ],
  "blockers": [],
  "prohibited_moves": [
    "do_not_copy_live_profile",
    "do_not_assume_playwright_inherits_manual_login"
  ],
  "download_policy": {
    "single_flight": true,
    "effective_click_required": true,
    "local_file_success_required": true,
    "materialization_grace_window_seconds": 20
  },
  "confidence": "high",
  "evidence_quality": "verified"
}
```

Interpretation:

- the user-facing Chrome window is the correct authenticated Gemini session
- browser-native attach exists in theory, but not to the right session
- `computer-use` is therefore the shortest working path on the current host
- the better long-term path is a dedicated, logged-in, debuggable Chrome
  session rather than copied profiles

## Dispatch Contract Integration

When the route becomes executable, copy these fields into the route card:

```json
{
  "adapter_decision_input": {
    "session_priority": "existing_session",
    "login_state_source_needed": "existing_browser",
    "host_surfaces": {
      "playwright": "thin",
      "chrome_devtools": "attach_only",
      "computer_use": "available"
    },
    "host_surface_evidence": {
      "playwright": "tabs-only surface",
      "chrome_devtools": "attach plus execute-javascript surface",
      "computer_use": "window-state plus accessibility surface"
    },
    "surface_discovery_status": "verified",
    "site_constraints": {
      "hover_reveal_controls": true,
      "single_flight_download": true,
      "effective_click_requires_active_state": true,
      "local_file_success_required": true,
      "materialization_delay_expected": true
    },
    "download_observability": {
      "effective_click_evidence": "spinner or request evidence",
      "materialization_grace_window_seconds": 20
    }
  },
  "adapter_decision_output": {
    "recommended_adapter": "chrome-devtools",
    "session_model": "existing_session_attach",
    "fallback_adapter": "computer-use",
    "reason_codes": [
      "existing_session_required",
      "browser_only_feature",
      "playwright_surface_too_thin"
    ],
    "prohibited_moves": [
      "do_not_copy_live_profile"
    ],
    "download_policy": {
      "single_flight": true,
      "effective_click_required": true,
      "local_file_success_required": true,
      "materialization_grace_window_seconds": 20
    },
    "confidence": "high",
    "evidence_quality": "verified"
  }
}
```

## Reason Code Vocabulary

Use stable codes where possible:

- `existing_session_required`
- `existing_debug_context_required`
- `manual_to_agent_handoff_required`
- `repeatable_dom_automation_required`
- `browser_only_feature`
- `host_surface_thin`
- `playwright_surface_too_thin`
- `chrome_devtools_surface_too_thin`
- `os_level_interaction_required`
- `download_sensitive_workflow`
- `gemini_existing_tab_preferred`
- `effective_click_confirmation_required`
- `materialization_delay_expected`
- `surface_discovery_unverified`

## Prohibited Move Vocabulary

- `do_not_copy_live_profile`
- `do_not_assume_playwright_inherits_manual_login`
- `do_not_confuse_attach_with_managed_browser`
- `do_not_escalate_to_coordinates_before_surface_check`

## Minimal User-Facing Summary

When surfacing the decision to the user, compress the JSON into:

1. chosen adapter
2. chosen session model
3. top reason codes
4. fallback adapter
5. blocker or missing discovery evidence if confidence is not high
