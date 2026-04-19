# Execution Preflight

Do not promise an execution path just because it sounds conceptually correct.

Preflight is the difference between:

- a real runnable route
- a route-shaped guess

## Core Rule

Check the actual adapter or command surface that the current host can use now.

Do not collapse these into one claim:

- the backend exists in theory
- a local command is installed
- the current host can control the right tool
- the route is ready for this turn

## Route-Level Preflight

Before executing any non-native image route, confirm:

1. the selected route
2. the exact adapter or tool surface
3. whether the host can call it in this session
4. whether there are approval, login, session, or download constraints
5. where artifacts will go

For non-trivial browser adapter choice, emit normalized decision metadata first.
Use [browser-adapter-decision-tree.md](./browser-adapter-decision-tree.md)
instead of skipping straight to prose.

## Built-In Image Route

Confirm:

1. the host actually exposes an image-generation tool in this turn
2. the task does not require browser-only download or site-only behavior
3. the user did not explicitly ask for prompt-only
4. the selected route is actually the built-in route for this task

If those pass, execute.

Do not turn the built-in path into a separate tool-routing discussion. The
heavy preflight ritual is for non-native routes, not for a native in-thread
image call that is already selected.

If any of those fail, change route.

## Gemini CLI Route

Minimum checks:

1. `gemini` is in `PATH`
2. the CLI help or version command succeeds
3. the exact invocation style is known
4. the route card captures prompt source and output location

Default preference:

- prefer this route family for Chinese-first image tasks when local Gemini
  execution is actually verified in the current host

Important distinction:

- `gemini` installed does not automatically prove image-generation extensions or
  custom slash commands are available
- treat image-specific subcommands or extensions as unverified until the current
  host proves them

Good wording:

- `Gemini CLI shell surface is installed, but image-specific extension support is not yet verified in this host.`

Bad wording:

- `Gemini CLI route is ready` when only `which gemini` was checked

## Browser Create-Image Route

First choose the actual adapter:

1. browser-native MCP such as `playwright`
2. browser-native MCP such as `chrome-devtools`
3. desktop app control such as `computer-use`

Do not choose by name alone. Verify the session model:

- managed browser
- isolated context
- persistent profile
- existing browser attach
- front-window app control

Then check:

1. the adapter is actually callable in this host
2. the target browser or app is controllable
3. approval or permission gating will not block the route
4. the route card records the browser/app and download assumptions
5. the exact site control that produces the final asset is known
6. the download completion check is known before clicking anything
7. the run knows what will count as an effective download click
8. the run knows how long it will wait before retrying or declaring the click
   blocked

### Adapter-Specific Checks

For `playwright`, confirm:

1. whether this host exposes enough Playwright surface for real page control,
   not just tabs or window sizing
2. whether the run is using a managed browser, a persistent profile, isolated
   storage state, or an existing-tab bridge
3. if existing live browser state is required, whether the official browser
   extension or a deliberate CDP attach path is actually configured
4. if CDP attach is the plan, acknowledge that it is a lower-fidelity path than
   a native Playwright protocol session

For `chrome-devtools`, confirm:

1. whether the plan is MCP-managed browser, `--autoConnect`, or a
   `--browser-url` / `--ws-endpoint` attach
2. whether the running Chrome instance is actually debuggable
3. whether the flow depends on a real existing logged-in session
4. whether the chosen path uses an official existing-session attach flow rather
   than copied profile files

For `computer-use`, confirm:

1. why the browser-native adapters are insufficient
2. which exact UI interaction requires app-level control
3. that the task is worth the added fragility of screen-driven interaction

Download-specific distinction:

Do not collapse these into one claim:

- the page shows an image
- the page has some download button
- the exact full-resolution control has been clicked
- the local file has finished materializing

For Gemini website workflows, `Download Full size` on the image card or
lightbox is not the same thing as a generic page-level download gesture.

Also remember:

- in small image-card state, the image-local controls may remain hidden until
  the pointer hovers over the image region
- `not visible before hover` is not the same as `not available`

Minimum verification plan:

1. intended download directory
2. expected filename pattern if known
3. whether the site may overwrite an old name
4. how you will verify success: timestamp, size, dimensions, hash, or explicit
   file-open confirmation
5. whether another full-size download is already in flight
6. whether hover over the image region is required to reveal the control
7. what active-state or network evidence will confirm the click was effective
8. what grace window will be allowed for delayed local materialization

If the adapter is blocked by approval, do not say the route failed because of
prompt quality.

Say instead:

- `The browser route is blocked by host control or approval gating.`

## Browser Tool Discovery

Treat browser route selection as adapter selection, not just site selection.

Practical order:

1. discover what browser-control tools the current host actually exposes
2. prefer the lightest browser-native adapter that can complete the workflow
3. use app-level control only when lighter browser tools are unavailable or
   insufficient

Host-surface caution:

- `playwright` does not automatically mean DOM-complete browser automation
- `chrome-devtools` does not automatically mean existing-session reuse is ready
- if the exposed tool surface is thin, report that before the run becomes a
  dead-end

## Shell Probe

If you need a quick local shell snapshot, run:

```bash
python3 /Users/jixiaokang/.agents/skills/visual-prompt-router/scripts/visual_route_probe.py
```

What this proves:

- command presence
- basic CLI help surface
- local browser-app presence
- likely route readiness hints

What this does not prove:

- MCP availability in the current host
- browser approval state
- site login state
- that an image-generation extension is installed

## Preflight Output

Report the result in concrete terms:

1. selected route
2. selected adapter
3. what was actually verified
4. what remains unverified
5. blocker, if any
6. artifact directory or intended artifact directory

Good wording:

- `Gemini image preview rendered, but the full-size local file is not yet
  verified.`
- `The correct image-local full-size download control is known, and completion
  will be verified by timestamp plus dimensions in Downloads.`
- `The full-size click is only considered effective after Gemini shows loading
  activity or equivalent request evidence, and the run will wait through the
  defined materialization window before retrying.`
- `No second full-size download will be triggered until the current Gemini
  download has materialized or been declared blocked.`

Bad wording:

- `Downloaded` when only the preview image is visible
- `No file appeared, so the download failed` immediately after the click with
  no wait or overwrite check
- `The button was clicked, so the download is running` when no active-state or
  request evidence was observed
