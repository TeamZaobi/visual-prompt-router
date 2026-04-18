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
- It does not make one backend canonical for every task.
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
- Need the controlled improvement loop for architecture or protocol infographic
  prompts: [references/architecture-ab-test-loop.md](./references/architecture-ab-test-loop.md)
- Need routing rules across prompt-only, built-in, CLI, and browser paths:
  [references/backend-routing.md](./references/backend-routing.md)
- Need concrete preflight checks before promising an execution path:
  [references/execution-preflight.md](./references/execution-preflight.md)
- Need the route card and artifact fields that make execution resumable:
  [references/dispatch-contract.md](./references/dispatch-contract.md)
- Need state-capture and resume rules for browser or CLI work:
  [references/state-capture-and-resume.md](./references/state-capture-and-resume.md)
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
7. Do not promise browser create-image execution before confirming the host can
   actually control a browser or browser automation path for that turn.
8. If browser control, app-control permission, session state, or approval
   gating blocks the website route, say so explicitly and downgrade to
   `prompt-only` or another viable backend instead of framing it as a prompt
   failure.
9. Turn-local tool state is not durable memory. If a CLI or browser route may
   span turns, externalize the route state and artifact paths before executing.
10. If a route depends on downloads, tabs, login/session assumptions, or an
    adapter such as `chrome-devtools`, `playwright`, or `computer-use`, record
    those dependencies explicitly instead of assuming the next turn can recover
    them from chat history.
11. If two rounds fail in the same direction, consider rerouting instead of
    endlessly rewriting the prompt.
12. For Chinese-first image tasks, default to a Gemini-family route instead of
    the host built-in image tool unless the user explicitly wants a rough draft
    or explicitly requests another path.
13. Once the selected route is the host's native image tool and the user has
    explicitly asked to make the image such as `做图`, `出图`, `生成图片`,
    `generate image`, or `render`, execute directly instead of expanding route
    analysis first.
14. Route, adapter, and tool-call discussion are primarily for non-native
    execution paths such as `Gemini CLI`, `Nano Banana`, `chrome-devtools`,
    `playwright`, or browser create-image flows.
15. For text-heavy diagrams, layout map and text budget beat style adjectives.
16. If exact labels or later editability are hard requirements, do not pretend a
   raster image is automatically the final deliverable.
17. If the user gives only architecture or flow relationships but the requested
   deliverable is a technical infographic, do not default to a dead enterprise
   diagram. Infer a friendly educational visual system with concrete title
   treatment, section markers, card language, arrow language, and icon
   metaphors.
18. For community-style explainers, give each role its own node anatomy and
    color role. Do not let host, client, server, resource, and component cards
    all collapse into the same anonymous rectangle style.
19. For protocol or architecture teaching infographics, generic words such as
    `clean`, `modern`, `friendly`, or `professional` are not enough by
    themselves. The prompt should explicitly lock concrete visual primitives:
    title badge or title ribbon treatment, dashed teaching arrows, literal icon
    metaphors for resource cards, and role-based color mapping.
20. For protocol explainers that name specific resource targets, do not stop at
    `simple icons` or `recognizable icons`. Name the actual metaphor for each
    target whenever possible, such as `laptop-plus-folder`, `database
    cylinder`, or `globe with API badges`.

## Technical Infographic Minimum

When the deliverable is a protocol explainer, architecture explainer, or
community-style technical infographic, the emitted prompt should explicitly
encode these visual primitives before you consider it done:

1. a highlighted title badge, title ribbon, or title band
2. an upper main relationship map plus a lower support band
3. host as a larger parent panel with app-like child tiles
4. clients as bridge cards
5. servers as repeated service-stack cards
6. dashed teaching arrows
7. resource cards with explicit icon metaphors
8. role-based color mapping across host, client, server, resource, and lower
   band
9. a lighter secondary treatment for the lower band

Default concrete resource metaphors for protocol explainers:

- `Local Filesystem` -> `laptop-plus-folder`
- `Database` -> `database cylinder`
- `Internet / Web APIs` -> `globe with API or service badges`

Do not emit the final prompt with weaker substitutions such as:

- `top title area`
- `clean connectors`
- `simple icons`
- `recognizable icons`
- `soft colors`

Rewrite those into concrete visual primitives before finishing.

Preferred default wording for protocol explainers:

- `top title band with a highlighted badge-style title and short subtitle`
- `upper main zone as a left-to-right relationship map`
- `host as a larger rounded parent panel containing app-like source tiles`
- `clients as smaller bridge cards`
- `servers as repeated service-stack cards`
- `resources as literal target cards`
- `use neat dashed teaching arrows so the flow reads instantly`
- `Local Filesystem as laptop-plus-folder, Database as cylinder, Internet / Web APIs as globe with API badges`
- `warm host tones, contrast client tones, stable server tones, clean support tones for resources, lighter calmer tones for the lower band`

If you are writing a protocol explainer prompt from sparse relationship facts,
start from those phrases and then adapt them to the user's subject.

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
- Is this meant to feel like a strict schematic or a friendly teaching
  infographic
- Is the task Chinese-first enough that route choice should prefer Gemini
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

For technical infographics, also force a concrete visual-system layer:

1. title badge or title ribbon treatment
2. upper main zone and lower support band
3. host as parent panel with app-like child tiles
4. clients as bridge cards
5. servers as repeated service-stack cards
6. resources as literal target cards with explicit icon metaphors
7. dashed teaching arrows
8. role-based color mapping by section
9. lighter secondary treatment for the bottom band

Detailed guidance and templates live in
[references/prompt-assembly.md](./references/prompt-assembly.md).

### 5. Pick the Route

- If the user wants only wording, stop at prompt delivery
- If the task is Chinese-first, prefer a Gemini-family route before the host
  built-in image path unless the user explicitly asks otherwise
- If the host image tool is enough and the chosen route is native, execute
  directly once the user has clearly asked to make the image
- If the task depends on Gemini CLI, Nano Banana, or Gemini website strengths,
  use that route
- If the task depends on browser-only create-image flow or high-res downloads,
  use browser automation only after confirming the host can actually drive a
  browser for that turn; otherwise fall back cleanly

Detailed routing rules live in
[references/backend-routing.md](./references/backend-routing.md).

### 6. Preflight And Externalize State

Before non-native execution, do two things:

1. run a route preflight that verifies the actual adapter or command surface
2. create a small route card that captures prompt source, adapter, artifact
   directory, expected outputs, and current blocker state

For the host-native image route, the rule is simpler: if the native image
surface is available in this turn and the user explicitly asked to make the
image, execute first and only reopen route analysis if that native round fails
for route reasons.

Do not treat a browser tab, MCP session, or previous tool call as durable state
unless you have written the important details down.

Detailed guidance lives in
[references/execution-preflight.md](./references/execution-preflight.md),
[references/dispatch-contract.md](./references/dispatch-contract.md), and
[references/state-capture-and-resume.md](./references/state-capture-and-resume.md).

### 7. Review The Result

Check the result against the acceptance dimensions, especially:

1. accuracy to source
2. fit to the requested medium
3. layout integrity
4. text fidelity when labels matter
5. pedagogical warmth and visual liveliness
6. design and aesthetic quality
7. usefulness as a downstream anchor

If the image is wrong, decide whether the fault is:

- source mismatch
- prompt mismatch
- medium mismatch
- backend mismatch
- text-fidelity mismatch
- low-quality random variation

### 8. Close Cleanly

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
5. whether browser control or approval gating was verified

## Writing Standard

- Match the user's language unless they request otherwise
- Prefer concrete visual instructions over abstract hype
- Keep prompts dense but readable
- Use negative constraints to prevent medium drift, not to dump random bans
- When a task has multiple valid deliverables, name the chosen one explicitly
