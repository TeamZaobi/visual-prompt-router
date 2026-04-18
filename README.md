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
- [references/acceptance-and-reroute.md](./references/acceptance-and-reroute.md): review, acceptance, and reroute criteria
- [agents/openai.yaml](./agents/openai.yaml): compact agent-facing launcher metadata

## Design Principles

1. Medium before style.
2. Purpose before adjectives.
3. Layout before decoration.
4. Source facts before generated artifacts.
5. Route changes matter as much as prompt changes.

## Technical Infographic Guidance

This skill includes a dedicated path for technical infographics and architecture explainers.

The core rule is simple:

- for text-heavy diagrams, layout map and text budget matter more than style adjectives

If exact labels, spelling accuracy, or downstream editability are hard requirements, treat raster generation as an exploration path rather than assuming it is the final publishable output.

## License

MIT