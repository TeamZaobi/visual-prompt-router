# Evaluation And Reflection Loop

Use this file when a visual task will go through more than one round.

The goal is simple:

- stop saying `looks better` without evidence
- stop mixing evaluation, diagnosis, and ideation into one vague step
- make each new round accountable to one explicit change hypothesis

## Minimal Core

The stable core is intentionally small:

1. fixed benchmark
2. small batch from one fixed prompt and route setup
3. four hard gates
4. `top hit` and `hit rate`
5. round delta
6. single next change

If a workflow cannot execute those lines cleanly, do not add more scoring
layers. Reduce complexity first.

## Split The Loop In Two

Do not merge these:

- `evaluation`
  - decide what passed, what failed, and whether the current result is good
    enough to promote
- `reflection`
  - decide why it failed, which layer caused the failure, and what single thing
    should change next

Rule:

- `05-acceptance.md` is the objective round verdict
- `06-run-notes.md` is the reflective and sedimentation layer

Do not hide evaluation inside free-form notes.
Do not turn reflection into another aesthetic rewrite.

## Required Inputs Per Round

Before evaluating a round, lock these references:

1. current batch under review
2. previous artifact if this is not round one
3. selected benchmark asset from
   `references/gold-standard-image-registry.md` when one exists
4. current `02-final-prompt.txt`
5. current `03-adapter-decision.json` and `04-route-card.json` if execution
   happened

If one of those is missing, the evaluation is incomplete.

## Evaluation Loop

### Step 1. Confirm The Family And Benchmark

Write down:

- deliverable family
- selected benchmark asset
- what the benchmark is teaching in this round
- batch size
- which artifact is the provisional `top hit`

If the chosen benchmark is clearly wrong, fix the benchmark selection first.
Do not keep polishing against the wrong target.

### Step 2. Check Hard Gates First

Hard gates are pass or fail, not vibes.

Default hard gates:

1. source accuracy
2. medium fit
3. semantic hierarchy or policy boundary clarity when relevant
4. text fidelity when labels matter

Family-specific hard gates:

- `Technical Infographic Or Architecture Explainer`
  - section rhythm and role separation must be legible
- `Leadership Briefing Architecture Explainer`
  - visible primary surface, operational hinge, and backstage formal service
    must all be explicit
- `Illustration Plus Chibi Figurine Product Shot`
  - box art and figure must clearly belong to the same design system
- `Illustration Plus Realistic Figurine Development Shot`
  - the development chain must be explicit, not implied

If a hard gate fails:

- do not spend the next round on polish adjectives
- fix the failing layer first

Batch rule:

- check hard gates on the whole batch, not just the prettiest image
- record which artifact is the `top hit`
- record `hit rate` as `passes / total`

Interpretation:

- `top hit` tells you the ceiling
- `hit rate` tells you whether the prompt or route is stable

### Step 3. Score Soft Dimensions

Use `1-5` scoring for soft dimensions:

1. layout integrity
2. role clarity and node anatomy
3. pedagogical warmth or visual liveliness
4. material or finish quality
5. downstream usefulness

Interpretation:

- `1`
  - clearly broken
- `2`
  - weak and not reusable
- `3`
  - workable direction but not stable
- `4`
  - strong enough for serious reuse
- `5`
  - benchmark-level or promotion-level

Do not inflate scores to avoid rerouting.

### Step 4. Record Batch Strength, Then Delta

Every round must answer:

1. did the batch produce a `top hit`
2. what is the `hit rate`
3. better than previous round, same, or worse
4. closer to the benchmark, same distance, or farther away
5. did the round improve the intended thing, or did it trade one failure for
   another

Useful delta language:

- `top hit improved, hit rate still weak`
- `better on hierarchy, worse on text fidelity`
- `same on family fit, better on finish`
- `closer to benchmark posture, still weak on node anatomy`

### Step 5. Make The Verdict

Allowed verdicts:

- `refine source`
- `refine prompt`
- `reroute`
- `promote artifact`
- `stop`

Promotion default:

- all relevant hard gates pass
- soft-dimension average is at least `4`
- no critical publication blocker remains

Promotion nuance:

- `promote artifact`
  - allowed when the batch contains one image that clearly passes the hard
    gates and is good enough for downstream use
- prompt or route stability
  - not allowed from a single-image batch
  - requires a recorded `hit rate` from a small batch

If the image is only a strong exploratory anchor, say that explicitly instead of
pretending it is publish-ready.

## Reflection Loop

Reflection starts only after the evaluation verdict is written.

### Step 1. Attribute The Dominant Failure Layer

Choose one primary cause:

- source truth problem
- wrong benchmark selection
- prompt compilation problem
- route or backend problem
- output quality randomness

If more than one problem exists, still name the dominant one.
Otherwise the next round will sprawl.

### Step 2. Write One Change Hypothesis

A good reflection ends with one testable hypothesis:

- `If we keep the benchmark and rewrite only the opening medium block, the
  image should stop drifting into poster posture`
- `If we keep layout and only repair semantic tiers, the backstage formal
  service should become readable without re-breaking composition`
- `If we reroute to a Chinese-stronger backend, text fidelity should stop being
  the dominant blocker`

Bad reflection:

- `make it clearer, nicer, more premium`

### Step 3. Lock A Single Next Change

Default rule:

- one round, one primary variable

Allowed primary variables:

- benchmark selection
- source constraints
- prompt compilation
- route or backend
- post-promotion rebuild path

Do not change benchmark, prompt, and route all at once unless the current round
was so broken that no narrower diagnosis is meaningful.

### Step 4. Decide What To Keep

Reflection must also record what should survive:

- visual posture to keep
- layout or section rhythm to keep
- exact phrase or instruction block to keep
- route behavior to keep

Without a `keep` section, teams often regress while fixing the next problem.

### Step 5. Decide Whether The Lesson Is Local Or Reusable

Use these buckets:

- `project-local lesson`
  - belongs only to this run or project
- `benchmark lesson`
  - means the benchmark asset or registry should change
- `skill lesson`
  - belongs in `references/`, templates, or routing rules
- `route lesson`
  - belongs in browser or backend behavior guidance

If the same lesson repeats, sediment it into the skill instead of leaving it in
run notes forever.

## Decision Shortcuts

### Refine Source

Use when:

- identity facts are wrong
- labels or forbidden relations were underspecified
- the wrong semantic tier is missing from the truth source

### Refine Prompt

Use when:

- source truth is correct
- benchmark is correct
- route is plausible
- wording still failed to compile the intended posture

### Reroute

Use when:

1. the same failure repeats twice
2. the prompt is already specific enough
3. the backend keeps reverting to its own defaults
4. text fidelity remains a publish blocker

### Promote Artifact

Use when:

- it passes the hard gates
- it is strong enough for its intended downstream role
- the remaining imperfections are acceptable for that role

Do not confuse this with prompt validation.
A promoted artifact can still come from a weak-hit-rate batch.

### Stop

Use when:

- the user no longer wants to iterate
- the current route is blocked and no fallback is allowed
- the image is good enough as an exploratory anchor and further polishing is
  low-value

## Anti-Patterns

Avoid these during iteration:

1. scoring after you already decided the answer
2. changing the benchmark silently
3. evaluating without a previous-round delta
4. treating route failure as prompt failure
5. treating benchmark mismatch as output randomness
6. writing a beautiful reflection with no concrete next-round variable

## Minimal Output Standard

After each round, you should be able to answer these seven lines cleanly:

1. what benchmark was used
2. what batch was evaluated
3. which artifact was the `top hit`
4. what the `hit rate` was
5. which hard gate failed or passed
6. whether this round is better, same, or worse
7. what single thing changes next

If you cannot answer those lines, the iteration loop is not stable yet.
