# State Capture And Resume

Tool state is not memory.

This matters most for browser and CLI image routes.

## Why This Exists

A long visual workflow can fail even when the prompt is fine because:

- a browser adapter changes
- a download step was not captured
- approval gating blocks the app route
- the next turn does not know which tab, folder, or artifact mattered

If you do not externalize that state, the agent learns nothing durable from the
run.

## Core Rule

If the route spans multiple steps, multiple turns, or site-specific behavior,
capture the state to disk or to a durable project note.

Do not assume a future turn can recover all of this from memory:

- chosen adapter
- session origin
- target site or page
- browser app
- login assumption
- download requirement
- last completed step
- kept artifacts
- blocker reason

## Browser-Specific Rule

Browser work is especially easy to lose.

Treat these as non-durable unless written down:

- open tabs
- selected site mode
- whether the state came from a managed browser or an existing attached session
- which button produced the high-resolution download
- current download folder
- approval state
- app-control success or denial
- whether the site may save slowly or overwrite an existing filename
- whether the correct image-local download control has already been clicked

## CLI-Specific Rule

CLI work also needs state capture when image generation or edits may be rerun.

Persist:

- exact command shape
- prompt snapshot
- model or extension assumption
- output directory
- generated filenames
- stderr or failure summary when relevant

## Minimal Resume Packet

If you need to continue later, the packet should answer:

1. what route was chosen
2. what adapter was used
3. whether the session came from a managed browser, persistent profile, storage
   state, existing tab attach, or front-window control
4. what prompt version ran
5. where artifacts were written
6. which exact download control should be used
7. how download completion will be verified
8. what succeeded
9. what failed
10. what the next step is

## Browser Session Origin Rule

Many browser failures are really session-origin failures.

Examples:

- a fresh Playwright browser was started when the task actually needed the
  user's already logged-in tab
- a copied profile was probed when the official attach flow should have been
  used
- the run narrative silently switched from browser-native attach to
  front-window clicking

Record the origin explicitly so later turns do not repeat the wrong assumption.

## Download Materialization Rule

Browser download state is easy to misread.

Capture separately:

- download control identified
- download click issued
- download click confirmed effective
- file materialized locally
- file promoted into project artifact path

Do not compress those into one vague status such as `downloaded`.

## Gemini Browser Rule

For Gemini website image runs, record:

- whether the asset was still in the chat card, in a focused preview, or in a
  lightbox
- the exact control used, such as image-local `Download Full size`
- whether the control first had to be revealed by hovering over the image
  region
- whether a full-size download is currently in flight
- whether the click was only dispatched or was confirmed effective by loading
  state or network evidence
- the grace window being allowed for delayed local materialization
- the observed download behavior: new filename, overwrite, delayed save, or no
  local materialization yet

If no file appears immediately, do not assume failure from one directory listing
alone. First consider:

- hover-reveal UI in the small-card state
- the click was not actually effective because no loading or request evidence
  followed
- slow browser write-out
- reused filename
- delayed timestamp update
- wrong button clicked

Only after checking those should you switch to a fallback plan.

If a Gemini full-size download is already in flight:

- do not click a second full-size download control
- do not switch to another candidate image's download button
- resolve the current download first: materialized, blocked, or abandoned

## Storage Rule

Preferred order:

1. project-owned run record location
2. workspace-local hidden run directory such as `./.codex/visual-runs/`
3. if neither is possible, a concise but explicit final message to the user

Best practice:

- keep the route card near the prompt snapshot and output artifacts
- do not bury the only blocker summary inside a long chat turn
- if download completion is still pending, write that pending state down instead
  of improvising a screenshot fallback too early

## What To Promote Into The Skill

Promote reusable method, not one-off session noise.

Promote:

- adapter selection rules
- blocker patterns
- preflight rules
- state-capture requirements

Do not promote:

- a one-time browser tab id
- a one-time login session
- a one-time output filename unless it became the project convention
