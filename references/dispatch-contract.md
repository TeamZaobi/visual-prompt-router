# Dispatch Contract

When image work moves from prompt design into execution, create a small route
card before running tools.

The route card is what turns a one-off attempt into a resumable workflow.

## Core Rule

Do not rely on chat history alone to recover:

- which adapter was chosen
- which prompt actually ran
- where artifacts were written
- what failed last

## Minimal Route Card Fields

Record:

1. `deliverable`
2. `route`
3. `adapter`
4. `execution_owner`
5. `prompt_source`
6. `prompt_text_snapshot` or prompt hash
7. `artifact_dir`
8. `download_dir`
9. `expected_outputs`
10. `preflight_summary`
11. `last_completed_step`
12. `next_step`
13. `blocker`
14. `download_control`
15. `download_verification_method`
16. `download_attempt_started_at`
17. `materialized_artifact`
18. `download_in_flight`
19. `download_control_reveal_action`
20. `session_origin`
21. `initial_state_source`
22. `adapter_decision_input`
23. `adapter_decision_output`
24. `reason_codes`
25. `host_surface_evidence`
26. `surface_discovery_status`
27. `download_effective_click_status`
28. `download_effective_click_evidence`
29. `download_materialization_grace_window_seconds`
30. `download_reclick_allowed_at`

## Route Examples

### Prompt-Only

- `route = prompt-only`
- `adapter = none`
- `artifact_dir = none`
- `last_completed_step = prompt delivered`

### Gemini CLI

- `route = gemini-cli`
- `adapter = gemini --prompt ...`
- `artifact_dir = workspace-local output path`
- `last_completed_step = CLI preflight passed`

### Browser Create-Image

- `route = browser-create-image`
- `adapter = chrome-devtools` or `playwright` or `computer-use`
- `session_origin = managed-playwright` or `playwright-extension-existing-tab` or `chrome-devtools-autoconnect` or `chrome-devtools-browser-url` or `computer-use-front-window`
- `initial_state_source = clean browser` or `persistent profile` or `storage-state` or `existing logged-in tab`
- `adapter_decision_input = normalized JSON from browser-adapter-decision-tree.md`
- `adapter_decision_output = structured adapter decision JSON`
- `host_surface_evidence = concise proof for actual exposed tool surfaces`
- `surface_discovery_status = verified | mixed | assumed`
- `artifact_dir = workspace-local run dir`
- `download_dir = concrete browser download path`
- `download_control = exact site control, such as Gemini image-local Download Full size`
- `download_verification_method = timestamp + dimensions` or equivalent
- `download_in_flight = false` before the click, then true until materialization
- `download_control_reveal_action = hover over image region` when the control is hidden in the small-card state
- `download_effective_click_status = not_clicked | dispatched | effective_confirmed`
- `download_effective_click_evidence = spinner | loading UI | network request | unknown`
- `download_materialization_grace_window_seconds = 20`
- `download_reclick_allowed_at = ISO timestamp after the grace window`
- `last_completed_step = create-image page loaded`

## Artifact Directory

If the project already has a canonical location, use it.

If not, create a workspace-local run directory such as:

```text
./.codex/visual-runs/YYYYMMDD-HHMM-[slug]/
```

Preferred file-driven layout inside that directory:

```text
./.codex/visual-runs/YYYYMMDD-HHMM-[slug]/
  00-visual-task.md
  01-structured-source.json
  01b-case-references.md
  02-final-prompt.txt
  03-adapter-decision.json
  04-route-card.json
  05-acceptance.md
  06-run-notes.md
  artifacts/
```

Keep there:

- prompt snapshot
- route card
- downloaded images
- chosen candidates
- blocker notes

If you are using the standard pack:

- `00-visual-task.md` and `01-structured-source.json` are the truth source
- `01b-case-references.md` records precedent retrieval
- `02-final-prompt.txt`, `03-adapter-decision.json`, and `04-route-card.json`
  are execution objects
- `05-acceptance.md` and `06-run-notes.md` are status projections

If the site saves outside the workspace first, keep both:

- the original browser-downloaded file path once verified
- the promoted project artifact path after copy or conversion

## Update Rule

Update the route card whenever one of these changes:

1. adapter changed
2. prompt changed materially
3. artifact directory changed
4. a download completed
5. a blocker was hit
6. the route was rerouted
7. the expected download control changed
8. the verification method changed
9. a download was clicked but not yet materialized
10. the in-flight download lock changed
11. the reveal action changed, such as hover becoming necessary in the current UI
12. the session origin changed
13. the initial state source changed
14. the structured adapter decision changed
15. the host surface evidence changed
16. the effective-click evidence changed
17. the materialization grace window changed

## Download Completion Rule

Do not mark `download completed` just because:

- the image is visible on the page
- a button was clicked
- the browser showed a transient spinner

Mark completion only after the route card can name the materialized file or the
verified overwrite target.

Useful browser-download fields:

- `download_control = image card top-right Download Full size`
- `download_control_reveal_action = hover over image region`
- `download_attempt_started_at = 2026-04-19T08:31:00+08:00`
- `download_effective_click_status = effective_confirmed`
- `download_effective_click_evidence = spinner plus request evidence`
- `materialized_artifact = /Users/.../Downloads/Gemini_Generated_Image_xxx.jpg`
- `download_verification_method = precise mtime plus dimensions`
- `download_in_flight = true` until the file is verified locally
- `download_materialization_grace_window_seconds = 20`

## Single-Flight Rule For Gemini

For Gemini website runs, treat `download_in_flight = true` as a hard lock on
additional `Download Full size` clicks.

Do not clear that lock until one of these is true:

- the file materialized locally
- the attempt was declared blocked after reasonable waiting and verification
- the route changed and the old attempt was explicitly abandoned

## Minimum User-Facing Report

When you execute, tell the user:

1. chosen route
2. chosen adapter
3. what preflight actually proved
4. where artifacts are going
5. what the current blocker is, if any
