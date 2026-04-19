# Shandong Replay Validation

This file records the first offline replay used to test whether the current
visual evaluation standard is stable enough to keep.

## Goal

Test whether the evaluation standard can do three things consistently:

1. select the better version
2. attribute the dominant failure to the right layer
3. produce one stable next action instead of vague aesthetic advice

This replay was useful for structural judgment, but it did not test stochastic
generation variance across repeated samples of the same prompt.

## Scope

- Family under test:
  `Leadership Briefing Architecture Explainer`
- Fixed benchmark:
  [leadership-briefing-architecture-explainer--shandong-p1.jpeg](../assets/gold-standard-benchmarks/images/leadership-briefing-architecture-explainer--shandong-p1.jpeg)
- Replay set:
  [P1-架构图.png](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/P1-架构图.png)
  [省平台-P1-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P1-Gemini-20260419.jpeg)
  [省平台-P2-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P2-Gemini-20260419.jpeg)
  [省平台-P3-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P3-Gemini-20260419.jpeg)
  [省平台-P4-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P4-Gemini-20260419.jpeg)

## Minimal Standard Under Test

Only these checks were treated as mandatory:

1. fixed benchmark
2. replay set as the evaluation batch available for this validation
3. four hard gates:
   - source accuracy
   - medium fit
   - semantic hierarchy
   - text fidelity
4. round delta:
   - better / same / worse
5. single next change

Anything beyond that was treated as optional commentary, not part of the core
standard.

## Replay Results

### 1. Old P1 Candidate

- Artifact:
  [P1-架构图.png](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/P1-架构图.png)
- Hard gates:
  - source accuracy: fail
  - medium fit: borderline pass
  - semantic hierarchy: fail
  - text fidelity: pass
- Delta against benchmark:
  - worse
- Dominant failure layer:
  `prompt compilation / source drift`
- Why:
  it brings `P2` semantics into `P1` by drawing a real-data formal service
  surface as if it already belongs to the stage
- Stable next change:
  fix stage scope and semantic tiers first, do not reroute and do not polish
  style first

### 2. Approved P1 Benchmark

- Artifact:
  [省平台-P1-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P1-Gemini-20260419.jpeg)
- Hard gates:
  - source accuracy: pass
  - medium fit: pass
  - semantic hierarchy: pass
  - text fidelity: pass
- Delta against old P1:
  - better
- Dominant success reason:
  it makes the visible primary surface, MCP bridge, validation surface, and
  review/receipt hinge legible without smuggling in the later-stage formal
  service
- Verdict:
  the standard stably selects this version as the stronger one

### 3. P2 Check

- Artifact:
  [省平台-P2-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P2-Gemini-20260419.jpeg)
- Hard gates:
  - source accuracy: pass
  - medium fit: pass
  - semantic hierarchy: pass
  - text fidelity: pass
- Main note:
  the standard keeps the review focused on the correct family problem:
  controlled introduction of real data and manual service, not generic beauty
  advice

### 4. P3 Check

- Artifact:
  [省平台-P3-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P3-Gemini-20260419.jpeg)
- Hard gates:
  - source accuracy: pass
  - medium fit: pass
  - semantic hierarchy: pass
  - text fidelity: pass
- Main note:
  the standard still holds when the visible primary surface shifts from local
  terminal to cloud workbench

### 5. P4 Check

- Artifact:
  [省平台-P4-Gemini-20260419.jpeg](/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P4-Gemini-20260419.jpeg)
- Hard gates:
  - source accuracy: pass
  - medium fit: pass
  - semantic hierarchy: pass
  - text fidelity: pass
- Main note:
  the standard still catches the right message hierarchy:
  provincial workbench as primary surface, approval and controlled execution as
  governed hinges, automation as auxiliary not protagonist

## What Held Up

These parts were stable in replay:

1. fixed benchmark first
2. evaluate against a visible set, not pure one-off intuition
3. four hard gates first
4. better / same / worse delta
5. one next change only

## What Did Not Need To Be Mandatory

These proved useful but did not need to be part of the minimal core:

- long soft-scoring grids
- extended stylistic commentary
- multiple simultaneous hypotheses

## Conclusion

The standard is not validated because it is long.
It is validated because, on this replay:

1. it rejected the older wrong `P1` version for the right reason
2. it selected the approved `P1` benchmark consistently
3. it stayed stable across `P2-P4` without drifting into unrelated aesthetic
   talk

But this replay only validated the structural review core.
It did not validate prompt stability under stochastic generation.
Therefore future live runs should record a small batch, plus `top hit` and
`hit rate`, before claiming a prompt or route is stable.

Therefore the stable core should remain:

1. fixed benchmark
2. small batch
3. four hard gates
4. `top hit` and `hit rate`
5. round delta
6. single next change
