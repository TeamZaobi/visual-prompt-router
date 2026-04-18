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
