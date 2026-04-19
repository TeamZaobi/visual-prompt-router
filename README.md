# visual-prompt-router

`visual-prompt-router` is a lightweight skill for image-task orchestration.

It helps an agent decide:

- what visual deliverable is actually needed
- how to build a medium-first prompt
- which generation path fits the job
- when to refine the prompt versus reroute the workflow

This repo is designed for image-generation prompt work across tasks such as:

- concept art
- standing character illustrations
- design sheets
- technical infographics and architecture explainers
- figurine or product-shot style composites
- multi-round review, redo, and reroute decisions

## What It Contains

- [SKILL.md](./SKILL.md): the main skill contract
- [references/task-triage.md](./references/task-triage.md): deliverable classification rules
- [references/prompt-assembly.md](./references/prompt-assembly.md): medium-first prompt method
- [references/patterns-and-examples.md](./references/patterns-and-examples.md): reusable prompt patterns
- [references/backend-routing.md](./references/backend-routing.md): routing logic across image workflows
- [references/browser-adapter-best-practices.md](./references/browser-adapter-best-practices.md): when to use `playwright`, `chrome-devtools`, or `computer-use`
- [references/browser-adapter-decision-tree.md](./references/browser-adapter-decision-tree.md): JSON metadata and deterministic adapter choice
- [references/structured-source-and-final-prompt.md](./references/structured-source-and-final-prompt.md): keep JSON or metadata on the source side, then compile into the final image prompt
- [references/file-driven-visual-ops.md](./references/file-driven-visual-ops.md): file roles, run-pack layout, and the default stable operating path
- [references/case-driven-prompting.md](./references/case-driven-prompting.md): retrieve similar approved cases before writing the new prompt
- [references/gold-standard-image-registry.md](./references/gold-standard-image-registry.md): concrete benchmark images and assembled benchmark boards for each recurring deliverable family
- [references/evaluation-and-reflection-loop.md](./references/evaluation-and-reflection-loop.md): per-round evaluation, diagnosis, and sedimentation rules for iterative image work
- [references/shandong-replay-validation.md](./references/shandong-replay-validation.md): first offline replay showing which parts of the evaluation standard actually held up
- [references/execution-preflight.md](./references/execution-preflight.md): route preflight before promising execution
- [references/dispatch-contract.md](./references/dispatch-contract.md): the route-card contract and artifact fields
- [references/state-capture-and-resume.md](./references/state-capture-and-resume.md): persistence rules for browser or CLI image runs
- [references/acceptance-and-reroute.md](./references/acceptance-and-reroute.md): review, acceptance, and reroute criteria
- [assets/file-driven-run-pack/README.md](./assets/file-driven-run-pack/README.md): copyable run-pack templates for repeatable execution
- [assets/gold-standard-benchmarks/README.md](./assets/gold-standard-benchmarks/README.md): stored benchmark images used by case-first retrieval
- [scripts/visual_route_probe.py](./scripts/visual_route_probe.py): local shell probe for route readiness
- [agents/openai.yaml](./agents/openai.yaml): compact agent-facing launcher metadata

## Design Principles

1. Medium before style.
2. Purpose before adjectives.
3. Layout before decoration.
4. Source facts before generated artifacts.
5. Route changes matter as much as prompt changes.
6. Execution state has to be externalized if the route spans turns.
7. Chinese-first image tasks should default to a Gemini-family route, not the
   built-in image path.
8. Structured metadata is a good source format, but raw JSON is usually a bad
   final Gemini website prompt.
9. If the job will be executed or revisited, use a file-driven run pack instead
   of relying on chat memory.
10. If a similar approved case already exists, use case-first compilation
   instead of hoping for a clean zero-shot hit.
11. In visual work, the strongest case is the approved image itself. Prompt-only
   precedent is secondary evidence, not the primary example.
12. Each recurring deliverable family should resolve to one concrete benchmark
   image or one concrete assembled benchmark board before case-first work is
   considered complete.
13. In iterative runs, evaluation and reflection must stay separate: round
   verdict first, failure attribution and next-change hypothesis second.
14. Stochastic image work must be judged on a small batch, not a single lucky
    image. One strong image can promote an artifact, but not the prompt or
    route behind it.

## Technical Infographic Guidance

This skill includes a dedicated path for technical infographics and architecture explainers.

The core rule is simple:

- for text-heavy diagrams, layout map and text budget matter more than style adjectives

If exact labels, spelling accuracy, or downstream editability are hard requirements, treat raster generation as an exploration path rather than assuming it is the final publishable output.

## License

MIT
