# Acceptance And Reroute

Use this file after generation or when reviewing an existing image.

## Acceptance Checklist

Score the image against these dimensions:

1. source accuracy
2. medium fit
3. design consistency
4. layout integrity
5. role clarity and node anatomy
6. pedagogical warmth and visual liveliness
7. text fidelity
8. material quality
9. emotional order
10. downstream usefulness

## Typical Failure Modes

### 1. Source Accuracy Failure

Signs:

- wrong costume structure
- wrong hair or makeup logic
- wrong props
- wrong identity signals

Default action:

- fix source reading or prompt specificity first

### 2. Medium Failure

Signs:

- concept sketch becomes a polished poster
- design sheet becomes a glamour shot
- product shot becomes a character illustration

Default action:

- rewrite the opening blocks of the prompt
- if repeated, change route

### 3. Consistency Failure

Signs:

- box art does not match the figurine
- screen model is unrelated to the physical figure
- multiple views do not feel like the same design system

Default action:

- strengthen consistency constraints

### 4. Quality Failure

Signs:

- cheap material look
- muddy face
- accidental clutter
- bad lighting hierarchy

Default action:

- decide whether the backend is the wrong fit before adding more adjectives

### 5. Dead Diagram Failure

Signs:

- the structure is technically correct but the image feels like a sterile
  corporate box diagram
- there is no title rhythm, section rhythm, or icon warmth
- every node becomes the same anonymous rectangle
- different roles do not have distinct card anatomy or color identity
- the output reads like documentation scaffolding, not a teaching graphic

Default action:

- strengthen diagram posture first
- add concrete icon metaphors, title treatment, card language, and arrow
  language instead of adding more abstract style words

### 6. Layout Failure

Signs:

- columns collapse into the wrong reading order
- separate resource cards get merged into one big panel
- arrows no longer describe the intended relationship
- the bottom component band turns into decorative clutter

Default action:

- rewrite the section map and layout relationships first
- prefer column language over rigid lanes when the reference is column-based

### 7. Text Fidelity Failure

Signs:

- labels are misspelled
- too many unique labels appear in one frame
- the model invents extra text or paragraphs
- the output looks fine visually but cannot be published as-is

Default action:

- reduce text budget and shorten labels first
- if Chinese wording or Chinese labels still degrade, reroute to a
  Gemini-family path before piling on more prompt detail
- if exact wording still matters, reroute instead of piling on more prompt
  detail
- if the chosen route was host-native, do not retroactively invent route
  analysis before the first native round; inspect the actual failure first

## When To Reroute

Reroute when:

1. two rounds fail in the same way
2. the prompt is already specific enough
3. the current backend keeps reverting to its own defaults
4. text-heavy diagrams keep missing label accuracy
5. editability or publishable correctness matters more than fast image variation
6. a built-in image path keeps losing Chinese prompt intent, Chinese label
   quality, or Chinese copy fidelity

## Closeout Rule

After review:

- keep approved assets
- keep the final prompt
- keep one representative failed variant when it proves why rerouting happened
- keep only necessary failed variants for comparison
- remove disposable previews, duplicates, and scratch files
