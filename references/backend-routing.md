# Backend Routing

This skill is routing logic, not a backend.

Keep the backend replaceable.

## Route 1: Prompt-Only

Use when:

- the user explicitly says not to generate
- the prompt is still being designed
- clothing, face, mood, or medium are not locked yet
- the user only wants wording for another tool

Action:

- deliver prompts only
- do not silently call image tools

## Route 2: Built-In Image Generation

Use when:

- the host already has a stable image tool
- the task is straightforward
- the task is not Chinese-first, or the user explicitly accepts a rough draft
- the user does not require Gemini-specific behavior
- fast iteration matters more than platform-specific workflow
- the chosen route is already the host-native image path

Action:

- if the user says `做图`, `出图`, `生成图片`, `generate image`, or `render`,
  treat that as direct execution intent on this route
- generate through the host's built-in image path
- review immediately after each image

Native-route rule:

- do not expand tool-call discussion first once the route is already native
- only reopen route analysis if the native path is unavailable in this turn or
  if one native round clearly shows a backend mismatch

Special note for Chinese-first tasks:

- do not make this the default route when Chinese prompt nuance, Chinese copy,
  or Chinese label quality matters
- use it only for rough exploration when the user explicitly prefers speed over
  Chinese-language quality

Special note for technical infographics:

- use this route for style exploration, composition testing, and rough layout
  comparison
- do not assume it is the best final route when exact labels matter

## Route 3: Gemini CLI Or Nano Banana

Use when:

- the user explicitly wants Gemini CLI or Nano Banana
- the task is Chinese-first and image quality depends on Chinese-language
  understanding
- the task depends on Gemini-side image behavior
- reference-image control or repeatable CLI execution matters
- the workflow benefits from shell traceability

Action:

- use the local Gemini CLI or Nano Banana route
- preserve the exact prompt used for reruns
- preserve the exact command form, output directory, and any extension or model
  assumption used for the run
- if image-specific CLI capability is not actually verified in the current host,
  say so and do not pretend shell availability alone proves the route is ready

## Chinese-First Routing Rule

If the image task is Chinese-first, default to a Gemini-family route before the
host built-in image tool.

Chinese-first usually means one or more of these are true:

- the prompt is primarily written in Chinese
- the image needs Chinese labels, signage, captions, or poster copy
- Chinese semantic nuance matters to the subject or scene
- prior built-in image runs already showed weaker Chinese understanding

Route choice inside the Gemini family:

- use Gemini CLI or Nano Banana when local execution is verified and shell
  traceability is useful
- use browser create-image with Gemini as the target site when the website path
  is required or browser-only Gemini behavior matters
- prefer `chrome-devtools` when the host exposes it and the Gemini website flow
  is the intended route

Important limit:

- if exact publishable Chinese wording or later editing is the real requirement,
  do not overpromise on raster generation just because Gemini is better than the
  built-in path; consider diagram, slide, or vector workflows instead

## Route 4: Browser Create-Image Flow

Browser route is a logical route, not one fixed adapter.

Possible adapters include:

- browser MCP such as `playwright`
- browser MCP such as `chrome-devtools`
- desktop app control such as `computer-use`

Adapter preference:

- prefer browser-native MCP control when it is available and sufficient
- use desktop app control only when the job truly depends on full app-level
  interaction or the lighter browser MCP path is unavailable

Adapter choice rule:

- choose by session model first, not by adapter label
- if you need deterministic managed automation, prefer `playwright`
- if you need existing live Chrome session reuse or manual-to-agent debugging
  handoff, prefer `chrome-devtools`
- use `computer-use` only when browser-native control is unavailable or too
  thin for the needed interaction

Do not assume the adapter namespace guarantees a rich surface. Preflight the
actual exposed tool capabilities.

Use when:

- the user explicitly wants the website workflow
- the platform's create-image feature is required
- high-resolution download is only available through the site
- browser-only controls matter
- the host can actually control the target browser for this turn

Action:

- treat browser actions as the main flow, not as a fake CLI wrapper
- include required download clicks as part of the real workflow
- record the actual adapter used, the target browser or app, the intended
  download directory, the exact download control, and the last completed step
  before handing control back
- treat `rendered in-browser preview` and `downloaded final artifact` as two
  separate workflow steps
- do not claim success until the file has actually materialized locally

### Playwright vs Chrome DevTools

Default interpretation:

- `playwright`
  - managed browser automation first
- `chrome-devtools`
  - existing Chrome attach and debugging first

Playwright best practice:

- use it for repeatable flows, stable locators, and controlled session models
- prefer isolated context, storage state, or a persistent Playwright profile
  over ad hoc login recovery
- if the task truly needs an already open logged-in browser tab, prefer the
  official Playwright browser extension or a deliberate CDP attach plan
- do not assume a fresh Playwright session will inherit the user's manual
  browser state

Chrome DevTools best practice:

- use it for active browser-session reuse, authenticated existing tabs, and
  manual-to-agent debugging handoff
- prefer `--autoConnect` when available for live session reuse
- use `--browser-url` or `--ws-endpoint` when the MCP client must connect to a
  running debuggable Chrome
- do not default to profile copying as a login-state strategy
- a reachable debug port is not enough by itself; it must point at the right
  authenticated session
- if the exposed DevTools surface is awkward for target switching but the page
  websocket is reachable, direct CDP websocket scripting is an acceptable
  implementation layer for that same attached session. Record that execution
  detail explicitly instead of pretending the session model changed.

Anti-pattern:

- switching from Playwright to copied browser profiles to remote-debug-port
  probing without first stating that the real requirement is existing-session
  reuse

Gemini website download rule:

- if the goal is the high-resolution asset, use the image-local
  `Download Full size` control, not a generic page-level download action
- if the asset is still shown as a smaller image card, hover over the image
  region first to reveal the image-local controls
- do not treat `button not visible yet` in the small-card state as proof that
  the full-size control is unavailable
- if the image needs to be opened into a lightbox or focused card before that
  control appears, treat that as part of the route
- treat Gemini full-size downloads as single-flight by default: one in-flight
  `Download Full size` at a time
- treat a download click as effective only after the site enters an active
  state such as spinner/loading behavior, or equivalent network/download
  evidence proves the request started
- after clicking the correct download control, wait for the browser save to
  materialize before switching strategies
- once the effective click is confirmed, allow a grace window for local file
  materialization before re-clicking or rerouting
- do not click `Download Full size` for a second image while the first download
  is still pending local materialization
- do not keep re-clicking just because no file appeared immediately; Gemini can
  delay local file creation after the click
- if Gemini reuses a filename or writes slowly, verify by precise timestamp,
  file size, dimensions, or hash rather than assuming `no new filename` means
  `no download`
- do not downgrade to screenshot fallback until you have verified that the
  correct download control was used and a reasonable wait produced no local file

Preflight before promising execution:

- verify browser automation or desktop-control access is available
- verify the target browser is controllable in the current host session
- verify approval or permission gating will not block app control
- verify you know which site-specific control produces the intended asset

If preflight fails:

- say explicitly that the browser route is blocked by environment or approval
  constraints
- do not imply that the prompt or route selection was wrong
- fall back to `prompt-only`, built-in image generation, or Gemini CLI,
  depending on what the user asked for and what remains feasible

If the failure is actually "existing session was required but the chosen
adapter started clean":

- say that explicitly
- reroute to `chrome-devtools` existing-session attach or Playwright extension
- do not describe it as a prompt failure

If the failure is actually "debuggable Chrome exists, but not for the right
logged-in Gemini session":

- say that explicitly
- prefer `computer-use` for the current front logged-in Chrome window
- treat a dedicated logged-in debuggable Chrome session as the long-term
  optimization path

Browser-state rule:

- do not assume the next turn can infer the same browser tab, download state,
  or logged-in session from prior chat alone
- externalize the important state into a route card or run note before you move
  on

Session-origin rule:

- record whether the browser state came from:
  - managed Playwright browser
  - persistent Playwright profile
  - Playwright extension attached to an existing tab
  - Chrome DevTools auto-connect
  - Chrome DevTools remote-debug URL
  - front-window `computer-use`
- do not let these silently blur together in the same run narrative

Download-state rule:

- record whether the correct download control has already been clicked
- record when that click happened
- record whether the click was only dispatched or was confirmed effective by
  active-state or network evidence
- record what local verification method will prove completion
- record whether a Gemini full-size download is currently in flight
- record whether the current state requires hover over the image region to
  reveal the control
- record the grace window before a re-click or reroute is allowed
- if the browser is known to save slowly, prefer explicit waiting and later
  verification over improvising a new capture path too early

## Serial-By-Default Rule

For same-site browser generation:

- default to serial execution
- only parallelize when the user explicitly allows it and risk is acceptable

Reason:

- lower anti-abuse risk
- lower session collision risk
- easier per-image review
- easier recovery when browser control is permission-gated
- aligns with Gemini website behavior where only one full-size download may be
  reliable at a time

## When To Change Route Instead Of Rewriting Prompt

Change route first when:

- the prompt is already clear but the output keeps collapsing to defaults
- one backend gives the right medium but wrong materials
- one backend preserves identity better than another
- the built-in path keeps weakening Chinese prompt intent or Chinese text
  quality
- the needed quality step exists only in one path
- the deliverable is a text-heavy technical infographic and spelling keeps
  drifting
- the user needs later editing in a diagram or slide workflow
- the website route is blocked by browser-control or approval denial

## Special Handling For Technical Infographics

If the job is a box-arrow-label explainer:

1. first decide whether the goal is a style draft or a publishable final
2. use prompt-only or built-in image generation when the user needs fast visual
   exploration
3. reroute to a vector or diagram tool when exact labels, clean editing, or
   downstream maintenance are hard requirements

Rule:

Not every bad image is a prompt problem.

## Route Output Format

When the user asks for routing advice, report:

1. recommended route
2. why it fits
3. fallback route
4. execution cautions
5. whether browser-control preflight passed
