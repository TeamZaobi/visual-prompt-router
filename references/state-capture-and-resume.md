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
- which button produced the high-resolution download
- current download folder
- approval state
- app-control success or denial

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
3. what prompt version ran
4. where artifacts were written
5. what succeeded
6. what failed
7. what the next step is

## Storage Rule

Preferred order:

1. project-owned run record location
2. workspace-local hidden run directory such as `./.codex/visual-runs/`
3. if neither is possible, a concise but explicit final message to the user

Best practice:

- keep the route card near the prompt snapshot and output artifacts
- do not bury the only blocker summary inside a long chat turn

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
