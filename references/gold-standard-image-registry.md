# Gold-Standard Image Registry

Use this file when `visual-prompt-router` needs a concrete visual benchmark
before writing prompts.

This registry exists to prevent a recurring failure mode:

- the skill says `case-first`
- but the actual case is only an old prompt, a vague memory, or a search query

The rule here is stricter:

- every recurring deliverable family should resolve to one concrete benchmark
  image or one concrete assembled benchmark board
- if no exact single public exemplar exists, build an assembled board from the
  strongest public clues and record the provenance explicitly

## Benchmark Classes

- `direct_public_benchmark`
  - a single public image that is already strong enough to anchor posture and
    composition
- `assembled_benchmark_board`
  - an internal board assembled from several public clues because no single
    public image was exact enough
- `project_local_approved_benchmark`
  - an approved local project image that already matches the required subtype

## Registry

### 1. Clean Standing Illustration

- Benchmark asset:
  [clean-standing-illustration--edward.png](../assets/gold-standard-benchmarks/images/clean-standing-illustration--edward.png)
- Benchmark class: `direct_public_benchmark`
- Deliverable family: `Clean Standing Illustration`
- Source page:
  `https://www.behance.net/gallery/159296413/Edward-Character-Design-Sheet-%28Personal-Work%29`
- Why it fits:
  stable full-character anchor, clear costume structure, readable silhouette,
  sheet posture instead of poster posture
- Teaches:
  character sheet posture, readable outfit breakdown, restrained background
- Do not inherit blindly:
  this specific fantasy costume language or sheet layout density

### 2. Cinematic Concept Sketch

- Benchmark asset:
  [cinematic-concept-sketch--cod-bo6.jpg](../assets/gold-standard-benchmarks/images/cinematic-concept-sketch--cod-bo6.jpg)
- Benchmark class: `direct_public_benchmark`
- Deliverable family: `Cinematic Concept Sketch`
- Source page:
  `https://www.behance.net/gallery/211216031/Call-of-Duty-Black-Ops-6-Cinematic-Concept-Art`
- Why it fits:
  clearly cinematic, atmosphere-first, frame-driven, not a poster and not a
  flat character sheet
- Teaches:
  keyframe mood, cinematic staging, production-art posture
- Do not inherit blindly:
  military realism, 1990s palette, or this exact darkness level

### 3. Design Sheet Or Equipment Card

- Benchmark asset:
  [design-sheet-or-equipment-card--blade-of-enervation.jpg](../assets/gold-standard-benchmarks/images/design-sheet-or-equipment-card--blade-of-enervation.jpg)
- Benchmark class: `direct_public_benchmark`
- Deliverable family: `Design Sheet Or Equipment Card`
- Source page:
  `https://www.behance.net/gallery/244875587/Project-2-PropWeapon-Concept`
- Why it fits:
  structure-first equipment sheet, readable main object, supporting detail
  views, process posture
- Teaches:
  prop anatomy, detail callouts, concept-sheet rhythm
- Do not inherit blindly:
  this specific fantasy weapon, its palette, or sheet ornament

### 4. Technical Infographic Or Architecture Explainer

- Benchmark asset:
  [technical-infographic-or-architecture-explainer--contentful.jpg](../assets/gold-standard-benchmarks/images/technical-infographic-or-architecture-explainer--contentful.jpg)
- Benchmark class: `direct_public_benchmark`
- Deliverable family: `Technical Infographic Or Architecture Explainer`
- Source page:
  `https://www.behance.net/gallery/246203003/Contentful-Multi-Platform-Integration-Infographic`
- Why it fits:
  real technical mapping, multi-zone hierarchy, system relationships explained
  through infographic structure rather than dead enterprise boxes
- Teaches:
  architecture-as-infographic posture, icon-plus-node mapping, section rhythm,
  readable system topology
- Do not inherit blindly:
  this exact isometric perspective, vendor-specific labels, or platform logic

### 5. Leadership Briefing Architecture Explainer

- Benchmark asset:
  [leadership-briefing-architecture-explainer--shandong-p1.jpeg](../assets/gold-standard-benchmarks/images/leadership-briefing-architecture-explainer--shandong-p1.jpeg)
- Benchmark class: `project_local_approved_benchmark`
- Deliverable family: `Leadership Briefing Architecture Explainer`
- Source origin:
  local approved project image promoted from
  `/Users/jixiaokang/Agents/OxNCourser/docs/diagrams/省平台-P1-Gemini-20260419.jpeg`
- Why it fits:
  it already encodes the exact subtype this skill kept missing: visible primary
  surface, controlled hinge, secondary backstage formal service, concise
  executive-reading posture
- Teaches:
  message hierarchy, explicit but secondary backstage node treatment, compact
  Chinese leadership-briefing posture
- Do not inherit blindly:
  the Shandong domain labels or this one project's node names

### 6. Illustration Plus Chibi Figurine Product Shot

- Benchmark asset:
  [illustration-plus-chibi-figurine-product-shot--assembled-board.jpg](../assets/gold-standard-benchmarks/images/illustration-plus-chibi-figurine-product-shot--assembled-board.jpg)
- Benchmark class: `assembled_benchmark_board`
- Deliverable family: `Illustration Plus Chibi Figurine Product Shot`
- Source pages:
  `https://www.behance.net/gallery/64481935/ASAP-Rocky-x-MINDstyle`
  `https://www.behance.net/gallery/222761503/wwiinngg-x-Jinart-Chibi-Figure-`
- Why it fits:
  no single public image was exact enough, so this board combines the two
  strongest clues:
  `A$AP Rocky x MINDstyle` supplies the box-plus-figure same-frame product-shot
  anatomy; `wwiinngg x Jinart` supplies the chibi ratio and collectible-poster
  language
- Teaches:
  same-frame packaging plus figure composition, design consistency between box
  art and object, chibi proportion cues
- Do not inherit blindly:
  celebrity IP, the scooter prop, or the animal-collection styling from Jinart

### 7. Illustration Plus Realistic Figurine Development Shot

- Benchmark asset:
  [illustration-plus-realistic-figurine-development-shot--assembled-board.jpg](../assets/gold-standard-benchmarks/images/illustration-plus-realistic-figurine-development-shot--assembled-board.jpg)
- Benchmark class: `assembled_benchmark_board`
- Deliverable family: `Illustration Plus Realistic Figurine Development Shot`
- Source pages:
  `https://www.behance.net/gallery/171902265/Rigan-Cyclop-Ghost-Collectible-Art-Toy`
  `https://www.behance.net/gallery/234849969/SKYTEAR-Kumaya-Character-Redesign`
- Why it fits:
  exact single-frame public exemplar was still weak, so this board assembles the
  development chain explicitly:
  concept sketches, digital sculpt stage, packaging plus illustration, and
  physical collectible context
- Teaches:
  concept-to-sculpt-to-object chain, collectible-development posture, product
  context without collapsing into a plain ad shot
- Do not inherit blindly:
  horror toy sketch language from `Rigan` or the fantasy card-game branding
  from `SKYTEAR`

### 8. Environment Or Scene Beat Image

- Benchmark asset:
  [environment-or-scene-beat-image--laurin-klement.jpg](../assets/gold-standard-benchmarks/images/environment-or-scene-beat-image--laurin-klement.jpg)
- Benchmark class: `direct_public_benchmark`
- Deliverable family: `Environment Or Scene Beat Image`
- Source page:
  `https://www.behance.net/gallery/243060563/Laurin-Klement-Concept-Art-Keyframes`
- Why it fits:
  the scene carries the story beat, not just the object; atmosphere and moment
  lead composition
- Teaches:
  narrative environment posture, scene scale, cinematic environment keyframe
- Do not inherit blindly:
  the automotive historical setting or sepia industrial palette

## How To Use

1. Start with project-local approved images if they already exist.
2. If none exist, pick the closest benchmark asset from this registry.
3. If the registry entry is an `assembled_benchmark_board`, read the listed
   clues separately before compiling the new prompt.
4. Record the selected benchmark asset in `01b-case-references.md`.
5. Treat this registry as strong visual precedent; prompt-only precedent is
   still secondary.

## Promotion Rule

If a new project-local image clearly beats the current registry entry for the
same family:

1. promote the new image into `assets/gold-standard-benchmarks/images/`
2. update this registry
3. explain why the benchmark changed

Do not silently replace a benchmark image without writing the reason.
