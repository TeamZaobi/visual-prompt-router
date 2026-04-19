# File-Driven Visual Ops

Use this file when the main problem is no longer prompt wording alone, but
operational drift:

- nobody is sure which prompt version counts
- browser runs cannot be resumed cleanly
- failed screenshots and final artifacts mix together
- structured source, final prompt, and route state are scattered across chat

This file stabilizes the visual workflow with `files-driven` thinking.

## First Four Answers

For visual work, answer these before you execute:

1. Which file counts right now
2. What is today's first step
3. Which files should not be touched yet
4. What must be externalized before tool execution

Default answer:

1. `00-visual-task.md` and `01-structured-source.json` count as the current
   truth source
2. retrieve similar cases, then compile `02-final-prompt.txt` from source plus
   precedent
3. do not write directly into the final project deliverable path yet
4. externalize route choice and browser state into `03-adapter-decision.json`
   and `04-route-card.json`

## Scope Mapping

For this skill, the default scope mapping is:

- `truth_source`
  - `00-visual-task.md`
  - `01-structured-source.json`
- `execution_object`
  - `02-final-prompt.txt`
  - `03-adapter-decision.json`
  - `04-route-card.json`
- `status_projection`
  - `05-acceptance.md`
  - `06-run-notes.md`
- `display_projection`
  - promoted approved image under the project artifact path

Do not let `status_projection` silently take over truth-source authority.

Examples:

- a review note saying `looks better` does not replace `01-structured-source.json`
- a browser screenshot is not the final display projection
- an unapproved image under `artifacts/` is still an execution object, not the
  project-facing final artifact

## Standard Run-Pack Layout

Use this layout for any visual run that may be resumed or reviewed:

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

Why this layout works:

1. source files stay separate from render output
2. route decisions become inspectable
3. browser state becomes resumable
4. acceptance gets written before the next random retry
5. the final promotion into the project path happens only after review

## Stable Main Path

### Step 1. Create The Task Pack

Create:

- `00-visual-task.md`
- `01-structured-source.json`

Write only:

- user goal
- deliverable type
- source facts
- visible labels
- forbidden relations
- acceptance language

Do not write browser tactics here.

## Step 2. Compile The Final Prompt

Before compilation, create:

- `01b-case-references.md`

Use it to record the closest approved precedents and the specific lessons to
borrow.

Prefer cases that include approved images, not prompt text alone.

Create:

- `02-final-prompt.txt`

This file is the actual render prompt.

Rule:

- structured source can mention semantic tiers and constraint categories
- retrieved cases should provide reusable layout or route lessons
- approved image examples should anchor the target posture, density, and
  hierarchy
- final prompt should read like image instructions

Do not rely on zero-shot by default when a similar approved case exists.

## Step 3. Decide The Route

Create:

- `03-adapter-decision.json`

This file answers:

- selected route
- selected adapter
- fallback route
- reason codes
- prohibited moves
- download policy

Use the normalized schema from
[browser-adapter-decision-tree.md](./browser-adapter-decision-tree.md).

## Step 4. Externalize The Execution State

Create:

- `04-route-card.json`

This file is required before browser execution.

At minimum it must capture:

- prompt source
- prompt snapshot
- artifact directory
- session origin
- download control
- effective-click rule
- local verification method
- current blocker

## Step 5. Execute Into `artifacts/`

Execution outputs go to:

- `artifacts/`

Do not write unreviewed images directly into:

- the project deliverable directory
- the presentation directory
- the document-facing export path

## Step 6. Review Before Reroute

Write review results to:

- `05-acceptance.md`

Use it to record:

- what passed
- what failed
- whether the problem is source, prompt, route, or output quality
- whether the next action is refine, reroute, or promote

Rule:

- no new prompt round before the previous round has an acceptance record

## Step 7. Keep Notes Small But Real

Write:

- `06-run-notes.md`

Use it for:

- observed site quirks
- overwritten filenames
- download timing behavior
- why a route changed

Do not hide critical route state here if it belongs in `04-route-card.json`.

## Step 8. Promote Only Approved Output

Only after review passes:

1. copy or rename the chosen artifact into the project path
2. record the promoted path in `05-acceptance.md` or `06-run-notes.md`
3. keep temporary failures in `artifacts/` only as long as they are useful

## Stop Rules

Stop and repair the pack first if any of these are true:

- the prompt being executed does not exist as a file
- the route decision exists only in chat prose
- browser state depends on memory of the previous turn
- the final project path already contains unapproved candidate images
- structured source and final prompt are being edited in the same file

## Default "Do Not Touch Yet" List

Before acceptance, do not directly edit:

- final deliverable filenames in the project display path
- project-facing README statements claiming success
- downstream docs that assume the image is final

## What To Keep After Closeout

Keep:

- the truth-source files
- the final prompt
- the adapter decision
- the route card
- the acceptance record
- the approved promoted artifact

Delete or archive:

- expendable wrong-route screenshots
- raw failed downloads that no longer teach anything
- temporary JSON prompt experiments that are not part of the stable source

## Relation To Existing References

Use together with:

- [structured-source-and-final-prompt.md](./structured-source-and-final-prompt.md)
- [execution-preflight.md](./execution-preflight.md)
- [dispatch-contract.md](./dispatch-contract.md)
- [state-capture-and-resume.md](./state-capture-and-resume.md)
