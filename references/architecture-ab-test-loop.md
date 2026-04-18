# Architecture Infographic A/B Loop

Use this loop when improving the skill's ability to write prompts for
architecture explainers, protocol explainers, and flowchart-like teaching
infographics.

## Purpose

Separate two questions cleanly:

1. Is the skill producing a strong enough prompt under isolated context
2. If the prompt is already strong, is the image backend still underperforming

Do not mix these layers.

## Standard Test Brief

Use one stable brief across iterations.

Example brief:

- beginner-friendly technical infographic
- protocol or architecture explainer
- not a poster
- top title area
- upper relationship map
- lower component/support band
- roles, counts, and relationships explicitly listed
- desired outcome: more alive than a dead enterprise diagram

## Phase 1: Prompt-Only Isolation

Subagents should:

- run in isolated context
- read only the skill and required local references
- receive relationship facts but not the strong example image
- produce prompt only, not images

Judge the prompt on these criteria:

1. does it lock the layout map
2. does it lock teaching-infographic posture instead of enterprise diagram posture
3. does it define role-based node anatomy
4. does it define section rhythm and title treatment
5. does it define icon metaphors
6. does it define color-role mapping
7. does it constrain text budget and readability
8. does it explicitly lock title badge treatment and dashed teaching arrows
9. does it explicitly lock literal resource icons instead of vague icon wording

If the answer is no on several of these, fix the skill before rendering images.

Fail the prompt if it still uses vague substitutions such as:

- `top title area` instead of badge or ribbon treatment
- `clean connectors` instead of dashed teaching arrows
- `simple icons` or `recognizable icons` instead of explicit target metaphors

## Phase 2: Same-Channel Rendering

Only after prompt quality is acceptable:

- use one consistent image-generation channel
- render the isolated prompt outputs through the same channel
- compare the images against the same rubric

Do not compare outputs from different channels and blame the skill first.

## Gap Classification

If the prompt is weak:

- patch the skill
- rerun isolation
- do not waste rendering budget

If the prompt is strong but the image is weak:

- inspect whether the backend is flattening node anatomy
- inspect whether the backend is losing text fidelity
- inspect whether the backend is drifting from teaching infographic to poster or
  dashboard
- then decide whether to patch prompt guidance, reroute backend, or both

## Good Prompt Signals

Strong isolated prompts usually contain language like:

- top title band or title badge
- upper architecture zone and lower components band
- host as parent panel with app-like source tiles
- clients as bridge cards
- servers as repeated service-stack cards
- resources as literal icon target cards
- compact chips or mini cards for components
- dashed teaching arrows
- role-based color identity
- soft off-white or paper-clean background

Weak isolated prompts usually contain language like:

- clean and modern
- professional
- structured layout
- several modules
- some boxes
- readable arrows

Those phrases are not wrong, but they are too generic to reach the higher
quality bar by themselves.

## Exit Criteria

The loop is ready to move on only when isolated prompts consistently:

1. avoid the dead corporate diagram fallback
2. encode role-specific node anatomy
3. encode section rhythm and title rhythm
4. encode enough visual warmth to plausibly reach community-style explainer
   quality

Then run image rendering and continue iterating from actual image failures.
