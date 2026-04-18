---
name: visual-prompt-router
description: >
  Use when the user wants strong image-generation prompts or needs to choose the
  right image workflow. Covers prompt writing, deliverable triage, medium-first
  prompt assembly, and routing across prompt-only, built-in image tools, Gemini
  CLI or Nano Banana, and browser create-image flows. Works for concept art,
  standing illustrations, design sheets, technical infographics or architecture
  explainers, illustration-plus-figurine product shots, and image redo or
  reroute decisions. 适用于做图提示词优化、介质判断、作图路径调度、比稿重做与通道切换。
---

# Visual Prompt Router

This skill is the orchestration layer for image work.

It solves five questions:

1. What image is actually needed
2. What source material should anchor it
3. How the prompt should be structured
4. Which generation path should be used
5. Whether a bad result needs prompt edits or a route change

## What This Skill Owns

- deliverable triage
- source-material reading order
- prompt assembly
- backend routing
- redo, reroute, and acceptance decisions

## What This Skill Does Not Own

- It does not invent source facts that the user did not provide.
- It does not treat generated images as truth.
- It does not make one backend canonical.
- It does not force execution when the user only wants prompts.

## Use This Skill When

- The user wants a better image prompt
- The user wants to convert vague aesthetic intent into a usable prompt
- The user needs to decide between concept sketch, clean standing illustration,
  design sheet, technical infographic, architecture explainer, product shot,
  figurine display, or another image type
- The user wants to choose between prompt-only, built-in image generation,
  Gemini CLI or Nano Banana, or browser create-image flows
- The user wants to review a generated image and decide whether to refine,
  reroute, or redo

## Jump Table

- Need to classify the job before writing prompts: [references/task-triage.md](./references/task-triage.md)
- Need the prompt-building method and reusable skeleton: [references/prompt-assembly.md](./references/prompt-assembly.md)
- Need common deliverable templates and examples: [references/patterns-and-examples.md](./references/patterns-and-examples.md)
- Need routing rules across prompt-only, built-in, CLI, and browser paths:
  [references/backend-routing.md](./references/backend-routing.md)
- Need acceptance, reroute, and redo rules:
  [references/acceptance-and-reroute.md](./references/acceptance-and-reroute.md)

## Hard Rules

1. Medium before style. If the deliverable is unclear, the prompt will drift.
2. Use before adjectives. Say what the image is for before piling on mood words.
3. Viewing order before detail piles. Decide what the viewer sees first, second,
   and third.
4. Source facts beat generated images. Read the user's provided material before
   "improving" anything.
5. Prompt-only means prompt-only. Do not silently escalate into generation.
6. Same-site browser generation defaults to serial execution unless the user
   explicitly accepts the risk of parallel work.
7. If two rounds fail in the same direction, consider rerouting instead of
   endlessly rewriting the prompt.
8. For text-heavy diagrams, layout map and text budget beat style adjectives.
9. If exact labels or later editability are hard requirements, do not pretend a
   raster image is automatically the final deliverable.

## Core Workflow

### 1. Classify the Job

Choose one primary mode:

- `prompt-only`
- `single image`
- `anchor image then expand`
- `batch production`
- `review, redo, reroute, or cleanup`

If the user did not specify the deliverable clearly, resolve that first.

### 2. Read the Best Available Inputs

Read inputs in this order:

1. user goal and acceptance language
2. character, object, brand, or world facts
3. attached images or referenced visuals
4. earlier approved prompt or image versions
5. backend-specific constraints if execution is required

Do not let a reference image silently override explicit textual facts unless the
user says the image should lead.

### 3. Lock the Deliverable

Before writing the main prompt, answer:

- What kind of image is this
- What is it used for
- What should the viewer feel first
- What is the main focus
- Is the background structural, atmospheric, or minimal
- Does text accuracy or later editability matter enough to affect route choice

### 4. Build the Prompt

Use the medium-first structure:

1. deliverable medium
2. image purpose
3. composition and viewing order
4. subject and design system
5. material and lighting
6. creator stance
7. viewer impression sequence
8. environment role
9. consistency constraints
10. negative constraints

Detailed guidance and templates live in
[references/prompt-assembly.md](./references/prompt-assembly.md).

### 5. Pick the Route

- If the user wants only wording, stop at prompt delivery
- If the host image tool is enough, use the built-in path
- If the task depends on Gemini CLI or Nano Banana strengths, use that route
- If the task depends on browser-only create-image flow or high-res downloads,
  use browser automation

Detailed routing rules live in
[references/backend-routing.md](./references/backend-routing.md).

### 6. Review The Result

Check the result against the acceptance dimensions, especially:

1. accuracy to source
2. fit to the requested medium
3. layout integrity
4. text fidelity when labels matter
5. design and aesthetic quality
6. usefulness as a downstream anchor

If the image is wrong, decide whether the fault is:

- source mismatch
- prompt mismatch
- medium mismatch
- backend mismatch
- text-fidelity mismatch
- low-quality random variation

### 7. Close Cleanly

- keep the approved image, prompt, and any required notes
- drop expendable failed candidates and temporary files
- promote methods into reusable guidance, not project facts into the skill

## Default Output Shape

When the user asks only for a prompt, prefer this format:

1. `正向提示词`
2. `负向提示词`
3. `补充说明`

When the user asks for routing help, prefer this format:

1. recommended route
2. why this route fits
3. fallback route
4. any execution constraints

## Writing Standard

- Match the user's language unless they request otherwise
- Prefer concrete visual instructions over abstract hype
- Keep prompts dense but readable
- Use negative constraints to prevent medium drift, not to dump random bans
- When a task has multiple valid deliverables, name the chosen one explicitly
