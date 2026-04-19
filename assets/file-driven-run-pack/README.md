# File-Driven Run Pack Templates

Copy this folder into a run directory when a visual task should be executable,
reviewable, and resumable.

Recommended destination:

```text
./.codex/visual-runs/YYYYMMDD-HHMM-[slug]/
```

Template roles:

- `00-visual-task.md`
  - truth source in prose
- `01-structured-source.json`
  - truth source in structured form
- `01b-case-references.md`
  - precedent retrieval and adaptation notes
- `02-final-prompt.txt`
  - final render prompt only
- `03-adapter-decision.json`
  - route and adapter decision record
- `04-route-card.json`
  - execution state record
- `05-acceptance.md`
  - review result and next action
- `06-run-notes.md`
  - compact operational notes
- `artifacts/`
  - unapproved outputs and working files

Rule:

- source files say what should be made
- case file says what prior precedent is worth reusing
- execution files say how this round is being run
- review files say what happened
- only approved promoted artifacts leave the run pack
