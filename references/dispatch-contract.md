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
- `artifact_dir = workspace-local run dir`
- `download_dir = concrete browser download path`
- `last_completed_step = create-image page loaded`

## Artifact Directory

If the project already has a canonical location, use it.

If not, create a workspace-local run directory such as:

```text
./.codex/visual-runs/YYYYMMDD-HHMM-[slug]/
```

Keep there:

- prompt snapshot
- route card
- downloaded images
- chosen candidates
- blocker notes

## Update Rule

Update the route card whenever one of these changes:

1. adapter changed
2. prompt changed materially
3. artifact directory changed
4. a download completed
5. a blocker was hit
6. the route was rerouted

## Minimum User-Facing Report

When you execute, tell the user:

1. chosen route
2. chosen adapter
3. what preflight actually proved
4. where artifacts are going
5. what the current blocker is, if any
