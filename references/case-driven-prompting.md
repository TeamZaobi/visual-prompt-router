# Case-Driven Prompting

Use this file when the task has precedent.

The rule is simple:

- if there is a relevant approved case, do not start from zero-shot
- start from case retrieval, then compile the new prompt
- for visual tasks, the image example is the main case signal
- the old prompt is supporting evidence, not the primary precedent

## When Case-First Is Mandatory

Do case retrieval before prompt writing when any of these are true:

1. the user gives a prior approved conversation or prompt
2. the user gives a prior approved image, screenshot, or visual reference and
   says "按这个做" or equivalent
3. the project already contains earlier images in the same family
4. the task is a recurring architecture explainer or leadership-briefing
   diagram
5. the user is clearly optimizing consistency, not novelty
6. the previous round already taught a stable visual or route lesson

Zero-shot is only acceptable when:

- no relevant case exists
- the task is genuinely novel
- the user explicitly wants a fresh exploratory branch

## What Counts As A Case

A usable case is not just "an old prompt".

For visual work, a prompt without a visible result is weak precedent.

Prefer case bundles that include at least two of these:

- approved image
- image-specific review notes
- final prompt
- review outcome
- route choice
- what was intentionally kept or avoided

Best case bundle:

- approved image
- approved or near-final prompt
- review notes that explain what made the image acceptable

Strong case sources:

1. approved project-local images in the same family
2. approved prior runs in `./.codex/visual-runs/` with visible outputs
3. user-provided approved images or screenshots
4. approved project-local prompt and image pairs
5. stable benchmark prompt-and-image examples in this skill

Weak case sources:

- random failed screenshots
- abandoned experiments with no acceptance record
- prompts with no visible outcome
- conversations that describe a target look but do not show what "good" looked
  like

## Weak Visual Precedent, Strong Clue Source

Some materials are not strong visual precedent, but they still carry useful
clues.

Examples:

- a shared conversation that explains how this image family is usually made
- a thread that reveals the route, workflow, or benchmark sources people use
- a post that names the visual posture even when it does not include the final
  approved image itself

Treat these as:

- weak for final look imitation
- strong for method clues, route clues, and retrieval clues

Do not discard them. Record them separately and keep their role explicit.

## Retrieval Order

For a new run, search in this order:

1. same project, same deliverable family, same image posture
2. same semantic tier pattern and same visual anatomy
3. same route and same website behavior
4. general skill benchmark image examples

This matters because:

- a route lesson is transferable
- a visual lesson is transferable
- but only the image itself shows whether hierarchy, density, spacing, and
  posture actually worked

## What To Extract From A Case

Do not clone the case blindly.

Look at the image first.

Extract:

- overall visual posture
- composition pattern
- information density
- semantic hierarchy
- node anatomy pattern
- title treatment
- spacing rhythm
- color hierarchy
- semantic tier language
- route constraint pattern
- negative constraints that actually prevented failure

Do not over-copy:

- image-specific project labels that do not belong to the new task
- old project names
- stale labels
- obsolete route assumptions
- accidental wording that belonged only to the previous task

## File-Driven Recording Rule

For a file-driven run, record retrieved cases in:

- `01b-case-references.md`

Each entry should state:

1. case source
2. case type such as `image precedent`, `prompt precedent`, or `clue source`
3. image reference or path
4. similarity
5. visual lessons to keep
6. prompt or route lessons to keep
7. what not to inherit blindly
8. whether the case teaches image posture, prompt structure, route behavior, or
   several of them

## Compilation Rule

The new prompt should be:

- sourced from current facts
- informed by prior cases
- not a pasted collage of old prompts
- visually anchored by at least one approved image example when precedent
  exists

Good pattern:

1. current task facts from `00-visual-task.md`
2. structured constraints from `01-structured-source.json`
3. reusable visual and route lessons from `01b-case-references.md`
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

- use image examples first when precedent exists
- use principles to adapt the example, not to replace it
