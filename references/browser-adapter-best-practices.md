# Browser Adapter Best Practices

Use this file when the question is not only "browser route or not", but
"which browser adapter model actually fits the job".

This guidance condenses official Playwright docs, the official Playwright MCP
README, the official Chrome DevTools MCP README and Chrome developer blog, plus
community reports about failure modes.

## Core Split

Do not treat these adapters as interchangeable:

- `playwright`
  - best for deterministic automation in a managed browser or managed browser
    context
- `chrome-devtools`
  - best for attaching to an already running Chrome session or active debugging
    workflow
- `computer-use`
  - best as a last resort when browser-native control is unavailable or too thin
    for the required interaction

## Playwright: Best Fit

Use Playwright when:

- you want repeatable multi-step automation
- you can start from a managed browser or managed context
- stable locators, auto-waiting, and assertions matter
- you need explicit state control such as isolated context, persistent profile,
  or storage-state bootstrap

Official Playwright guidance strongly favors:

- locators over brittle selectors or coordinates
- auto-waiting and web-first assertions
- explicit browser-context isolation
- stored authentication state instead of improvising login every run

Official Playwright MCP guidance gives three clean session models:

- persistent profile
- isolated context plus optional `--storage-state`
- existing browser tabs via the Playwright browser extension

Preferred order for Playwright usage:

1. isolated context plus storage state for reproducible authenticated work
2. persistent Playwright MCP profile when session continuity inside the same
   workspace matters
3. Playwright browser extension when you truly need an already open logged-in
   browser tab
4. CDP attach only when no better Playwright-native path exists

Important limitation:

Playwright's official `connectOverCDP` path is lower fidelity than the native
Playwright protocol connection. Do not treat CDP attach as equivalent to a
fully managed Playwright session.

Practical rule:

If the task needs "take over the browser the user already has open", the clean
Playwright answer is the official browser extension or a deliberate CDP attach
plan, not wishful thinking about a fresh managed browser inheriting the user's
login state.

## Chrome DevTools: Best Fit

Use Chrome DevTools when:

- you need the user's already running Chrome session
- you want manual-to-agent handoff on an authenticated page
- the debugging context already exists in Chrome or DevTools
- you want agent access to active Elements or Network investigation state
- the client is sandboxed and must connect to a browser running elsewhere

Official Chrome DevTools MCP guidance offers three clean modes:

- MCP-managed browser with a dedicated profile
- `--autoConnect` to an active Chrome session
- `--browser-url` or `--ws-endpoint` to a manually debuggable Chrome instance

Preferred order for Chrome DevTools usage:

1. `--autoConnect` for manual plus agent session sharing on Chrome 144+
2. `--browser-url` when you need to connect to an already debuggable Chrome
   from a sandboxed or separated client
3. MCP-managed dedicated profile when existing-session reuse is not required

Important security and setup rule:

Official Chrome guidance now requires a non-default `--user-data-dir` when
using remote debugging switches against a launched Chrome instance. Do not make
the default browser profile the foundation of your remote debugging workflow.

Practical rule:

If login state matters, prefer official existing-session attach. Do not default
to copying `Default` or `Profile 1` into a temporary directory and hoping the
cookies survive.

Implementation note:

If the host's `chrome-devtools` wrapper is thin or awkward for page targeting
but the verified page websocket is reachable, direct CDP websocket scripting is
an acceptable implementation detail for the same attached Chrome session. Keep
the session model labeled as existing-session attach; do not blur it into a new
browser route.

Tested host rule:

Do not stop at "a debuggable Chrome exists".

Verify that the debuggable Chrome is the right authenticated session. If the
reachable debug ports lead to Gemini login pages while the real logged-in page
only exists in the front browser window, `chrome-devtools` is not yet the
shortest working path for that host.

## Computer Use: Last Resort

Use `computer-use` when:

- browser-native tools are missing
- the exposed tool surface is too thin for the task
- the task depends on hover-only, focus-only, or OS-level interactions that the
  browser-native surface cannot express

Do not open with front-window clicking if a browser-native adapter can cleanly
solve the task.

## Download Effectiveness Rule

For browser download workflows, separate these states:

1. click dispatched
2. click confirmed effective
3. file materialized locally

Treat `click confirmed effective` as requiring one of:

- visible loading or spinner behavior after the click
- equivalent network or download evidence that the request actually started

Do not treat a raw button press log as enough proof by itself.

For Gemini website image downloads:

- the correct control is the image-local `Download Full size` action, not a
  generic page-level download button
- in the small-card state, hover over the image region first to reveal the
  control
- once the click is confirmed effective, wait through a defined grace window
  for local materialization before re-clicking
- default to single-flight behavior: do not start another full-size download
  until the current one materializes, is declared blocked, or is explicitly
  abandoned

## Host-Surface Rule

Adapter name is not the capability contract.

Before choosing `playwright` or `chrome-devtools`, inspect what the current
host actually exposes.

Examples of thin surfaces:

- `playwright` only exposes tab management
- `chrome-devtools` only exposes connect and JavaScript execution

If the surface is thin, say so explicitly and change route or escalate to
`computer-use` when necessary.

## Anti-Patterns

Avoid these:

- assuming a fresh Playwright browser will inherit the user's current login
  state
- using coordinate clicking when stable DOM control is available
- treating CDP attach as the default Playwright mode
- cloning a live Chrome or Edge profile to recover login state
- switching from Playwright to profile copying to remote-debug port probing
  without first clarifying whether the job really requires an existing session

## Recommended Adapter Decision

1. If the task needs a real existing logged-in tab or active manual debugging
   state, prefer `chrome-devtools --autoConnect` or the Playwright browser
   extension.
2. If the task needs deterministic, repeatable browser automation from a clean
   start, prefer managed Playwright.
3. If the task needs a controlled authenticated session but not the user's live
   tab, prefer managed Playwright with `--storage-state` or a persistent MCP
   profile.
4. If the host only exposes thin browser-native tools, say that early and fall
   back to `computer-use` instead of pretending the adapter is richer than it
   is.
