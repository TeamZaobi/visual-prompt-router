# Case-Driven Prompting

Use this file when the task has precedent.

The rule is simple:

- if there is a relevant approved case, do not start from zero-shot
- start from case retrieval, then compile the new prompt

## When Case-First Is Mandatory

Do case retrieval before prompt writing when any of these are true:

1. the user gives a prior approved conversation or prompt
2. the project already contains earlier images in the same family
3. the task is a recurring architecture explainer or leadership-briefing
   diagram
4. the user is clearly optimizing consistency, not novelty
5. the previous round already taught a stable visual or route lesson

Zero-shot is only acceptable when:

- no relevant case exists
- the task is genuinely novel
- the user explicitly wants a fresh exploratory branch

## What Counts As A Case

A usable case is not just "an old prompt".

Prefer case bundles that include at least two of these:

- final prompt
- approved image
- review outcome
- route choice
- what was intentionally kept or avoided

Strong case sources:

1. approved project-local prompt and image pairs
2. approved prior runs in `./.codex/visual-runs/`
3. stable benchmark prompts in this skill
4. user-provided prior conversations or approved examples

Weak case sources:

- random failed screenshots
- abandoned experiments with no acceptance record
- prompts with no visible outcome

## Retrieval Order

For a new run, search in this order:

1. same project, same deliverable family
2. same semantic tier pattern
3. same route and same website behavior
4. general skill benchmark examples

This matters because a route lesson and a visual lesson are both transferable.

## What To Extract From A Case

Do not clone the case blindly.

Extract:

- composition pattern
- semantic tier language
- node anatomy pattern
- route constraint pattern
- negative constraints that actually prevented failure

Do not over-copy:

- old project names
- stale labels
- obsolete route assumptions
- accidental wording that belonged only to the previous task

## File-Driven Recording Rule

For a file-driven run, record retrieved cases in:

- `01b-case-references.md`

Each entry should state:

1. case source
2. similarity
3. what to keep
4. what not to inherit blindly
5. whether the case teaches prompt structure, route behavior, or both

## Compilation Rule

The new prompt should be:

- sourced from current facts
- informed by prior cases
- not a pasted collage of old prompts

Good pattern:

1. current task facts from `00-visual-task.md`
2. structured constraints from `01-structured-source.json`
3. reusable case lessons from `01b-case-references.md`
4. compiled final prompt in `02-final-prompt.txt`

## Review Rule

If a run fails, decide whether the missing piece was:

- wrong case chosen
- no case retrieved when one should have been
- case copied too literally
- correct case found but not compiled into the final prompt

Add that finding to the next acceptance record.

## Short User-Facing Rule

Compress the method to:

- use examples first when precedent exists
- use principles to adapt the example, not to replace it
