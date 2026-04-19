# Task Triage

Use this file when the user wants image work but the actual deliverable is still
blurred.

## First Questions

Ask or infer these in order:

1. Is the user asking for prompt-only or actual image generation
2. What is the deliverable type
3. What is the image used for
4. What is the main focus of the frame
5. Is this a one-off image or part of a larger pack

## Native Execute Shortcut

If all of these are true:

- the selected route is the host-native image path
- the user is asking for actual image generation
- the user says `做图`, `出图`, `生成图片`, `generate image`, or similar direct
  execution language

Then:

- treat the request as immediate execution intent
- do not open tool-routing analysis first
- only reopen routing if the native route is unavailable or the first native
  round clearly shows a backend mismatch

## Common Deliverable Types

### 1. Clean Standing Illustration

Use when the user wants a stable character anchor for later reuse.

Typical signals:

- "立绘"
- "基准图"
- "人物全身"
- "角色要先锁定"

### 2. Cinematic Concept Sketch

Use when the image is for development, mood, or pre-production, not a polished
poster.

Typical signals:

- "电影概念图"
- "草图"
- "前期开发稿"
- "要有起稿线和试色感"

### 3. Design Sheet Or Equipment Card

Use when the goal is to freeze structure, gear, variants, or mechanism logic.

Typical signals:

- "装配卡"
- "概念设计页"
- "配件页"
- "三视图"
- "武器设计"

### 4. Technical Infographic Or Architecture Explainer

Use when the user wants a clean explanatory diagram with boxes, arrows, labels,
sections, or a polished slide-like teaching graphic.

Typical signals:

- "架构图"
- "信息图"
- "解释图"
- "MCP 图"
- "框图"
- "技术社区常见那种图"

Important split:

- If the user wants a plain enterprise architecture schematic, optimize for
  strict structure and reserve visual personality.
- If the user wants "社区常见那种清楚又好看"的解释图, infer a friendly teaching
  infographic with icon metaphors, section rhythm, and warmer card language
  rather than a dead corporate diagram.

Leadership-briefing split:

- If the user says `汇报`, `给领导看`, `交付文档`, `30 秒讲清`, `示意图`,
  `不要工程流程图`, or equivalent language, treat it as a leadership briefing
  architecture explainer.
- For this subtype, optimize for message hierarchy before exhaustive node
  coverage.
- Lock these semantic tiers explicitly:
  - current visible primary surface
  - operational hinge such as review, approval, receipt, or governance
  - backstage formal service or formal destination
- If one of those tiers remains implicit only, the prompt is still
  underspecified even when the box count looks correct.

### 5. Illustration Plus Chibi Figurine Product Shot

Use when the frame must show both the 2D character art and a stylized chibi
collectible.

Typical signals:

- "Q版手办"
- "棚拍"
- "包装盒"
- "立绘加手办"

### 6. Illustration Plus Realistic Figurine Development Shot

Use when the frame must show the 2D art, the realistic figurine, and the
development chain.

Typical signals:

- "1/7 手办"
- "桌面开发"
- "ZBrush"
- "建模界面"

### 7. Environment Or Scene Beat Image

Use when the scene itself or a narrative moment is primary.

Typical signals:

- "场景图"
- "情节草图"
- "这一幕"
- "地点氛围"

## Triage Rules

### If the user mostly complains about:

- clothing, makeup, hairstyle, or facial details:
  the prompt is underspecified
- "this does not feel like the right kind of image":
  the medium is underspecified
- "same prompt, wrong output style every time":
  the route may be wrong
- "looks fine but not this character":
  the consistency constraints are too weak
- "the boxes/arrows/columns are wrong":
  the layout map is underspecified
- "the words keep spelling wrong":
  the text budget is too ambitious or the route is wrong
- "结构对了但图太死、不生动":
  the prompt is missing diagram posture, icon metaphors, and teaching-graphic
  visual primitives
- "结构对了但主次不对", "后台正式入口没立住", or similar:
  the semantic tiers or policy boundary are underspecified

### If the user says "重新设计"

Do not just rewrite details.

Re-open these:

1. deliverable type
2. image purpose
3. viewing order
4. design language

For technical infographics, also re-open:

5. section map
6. column or row relationships
7. label count and text budget

For leadership-briefing architecture explainers, also re-open:

8. which region is the current visible primary surface
9. which node is the operational hinge
10. which backstage service must be explicit but secondary
11. which arrows or access paths must never appear as direct links

### If the user gives reference images

Decide which role each image plays:

- fact anchor
- style anchor
- composition anchor
- quality bar

Do not let one image silently play all four roles.

For technical infographics, it is often useful to split the reference image into
two roles explicitly:

- style anchor
- layout anchor
