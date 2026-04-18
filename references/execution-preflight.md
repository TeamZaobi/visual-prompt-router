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

Then check:

1. the adapter is actually callable in this host
2. the target browser or app is controllable
3. approval or permission gating will not block the route
4. the route card records the browser/app and download assumptions

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
