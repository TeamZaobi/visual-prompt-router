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
- the user does not require Gemini-specific behavior
- fast iteration matters more than platform-specific workflow

Action:

- generate through the host's built-in image path
- review immediately after each image

Special note for technical infographics:

- use this route for style exploration, composition testing, and rough layout
  comparison
- do not assume it is the best final route when exact labels matter

## Route 3: Gemini CLI Or Nano Banana

Use when:

- the user explicitly wants Gemini CLI or Nano Banana
- the task depends on Gemini-side image behavior
- reference-image control or repeatable CLI execution matters
- the workflow benefits from shell traceability

Action:

- use the local Gemini CLI or Nano Banana route
- preserve the exact prompt used for reruns

## Route 4: Browser Create-Image Flow

Use when:

- the user explicitly wants the website workflow
- the platform's create-image feature is required
- high-resolution download is only available through the site
- browser-only controls matter

Action:

- treat browser actions as the main flow, not as a fake CLI wrapper
- include required download clicks as part of the real workflow

## Serial-By-Default Rule

For same-site browser generation:

- default to serial execution
- only parallelize when the user explicitly allows it and risk is acceptable

Reason:

- lower anti-abuse risk
- lower session collision risk
- easier per-image review

## When To Change Route Instead Of Rewriting Prompt

Change route first when:

- the prompt is already clear but the output keeps collapsing to defaults
- one backend gives the right medium but wrong materials
- one backend preserves identity better than another
- the needed quality step exists only in one path
- the deliverable is a text-heavy technical infographic and spelling keeps
  drifting
- the user needs later editing in a diagram or slide workflow

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
