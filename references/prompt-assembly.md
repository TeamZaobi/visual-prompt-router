# Prompt Assembly

This file holds the core method for writing strong image prompts.

## Core Principle

Do not start from subject nouns alone.

Start from:

1. what kind of image this is
2. what the image is for
3. what the viewer notices first
4. only then the subject details

## Medium-First Ten-Block Method

### 1. Deliverable Medium

Name the image type directly.

Examples:

- `彩色电影概念精细草图`
- `干净克制的角色基准立绘`
- `角色装配卡概念设计页`
- `二维立绘 + Q版收藏手办棚拍`
- `二维立绘 + 写实 1/7 收藏级 3D 手办桌面开发展示`

### 2. Image Purpose

State why the image exists.

Examples:

- `影视前期开发稿，不是海报`
- `角色设计锚点，用于后续一致性复用`
- `商业产品展示图，用于同时展示二维原画与三维手办`

### 3. Composition And Viewing Order

Lock:

- subject size in frame
- camera angle
- whether the subject looks at camera
- what is seen first, second, and third

Rule:

Emotion is not only adjectives. It is also viewing order.

### 4. Subject And Design System

Write the subject as a design system, not a noun bag.

Include:

- identity or role
- body language
- silhouette logic
- costume structure
- hair and makeup logic
- tools, weapons, or accessories

### 5. Material And Lighting

Be specific about real material behavior.

Examples:

- matte silk
- aged bronze
- resin
- acrylic
- glossy PVC
- wind-lifted outer layer
- soft studio light plus rim light

### 6. Creator Stance

How is the creator looking at the subject.

Examples:

- restrained respect
- sharp admiration
- protective sorrow
- cold observation

This should guide selection, not become empty slogan words.

### 7. Viewer Impression Sequence

Write the emotional order.

Example pattern:

- first feels presence
- then notices damage or fatigue
- finally understands the hidden precision or danger

### 8. Environment Role

State whether the environment is:

- minimal support
- atmospheric backdrop
- structural scene
- information-bearing prop system

### 9. Consistency Constraints

Use when the frame contains several linked artifacts.

Typical cases:

- box art must match the figurine
- 2D art, 3D figure, and modeling screen must be the same design
- prop sheet variants must share the same base system

### 10. Negative Constraints

Negative prompts should prevent the most common drift for that medium.

Examples:

- no poster finish
- no mobile-game splash art
- no random overdesigned glow effects
- no cheap blind-box look
- no unrelated background clutter

## Special Case: Technical Infographic Or Architecture Explainer

For this medium, do not lead with "beautiful", "futuristic", or "high-end".

Lead with:

1. the deliverable being an infographic or architecture explainer
2. the purpose being education or explanation, not poster polish
3. the section map
4. the column or row relationships
5. the text budget

### What To Lock First

- overall section count
- top, middle, bottom, or left-right split
- whether the structure is column-based or lane-based
- exact card counts when they matter
- which labels must be verbatim
- whether the background is clean support or information-bearing

### Prompting Priorities For This Medium

Order of importance:

1. layout map
2. section relationships
3. label budget
4. diagram posture
5. icon language
6. palette and finish

Rule:

For technical infographics, layout nouns beat style adjectives.

### Diagram Posture: Dead Diagram vs Teaching Infographic

Do not collapse every architecture prompt into the same corporate box diagram.

Choose the posture explicitly:

- strict enterprise schematic
- friendly teaching infographic
- sketchnote-like explainer with clean vector discipline

For community-style technical explainers, the default should usually be
`friendly teaching infographic`, not `enterprise schematic`.

If the user gives only relationship facts, infer the missing visual system
instead of repeating vague words like "clean", "modern", and "professional".

### From Relationship Facts To Visual System

When the input only provides process or architecture relationships, synthesize
the visual layer in concrete terms:

- title treatment
  - top title band, pill badge, or highlighted section label
- section rhythm
  - top architecture zone and bottom support zone, or other clearly separated
    teaching bands
- card language
  - rounded containers, light outlines, subtle shadows, generous padding
- arrow language
  - dashed teaching arrows, clear directional connectors, not dense network-map
    spaghetti
- icon metaphors
  - literal, friendly symbols for apps, servers, filesystems, databases,
    internet, tools, prompts
- palette role
  - one color family per major region, not random decorative color splashing
- micro-ornament
  - a small amount of warmth such as badges, divider ribbons, tiny supportive
    glyphs, or soft paper-like calmness without turning the image into a poster

If these are absent, image models tend to fall back to a dead corporate diagram
even when the structure is correct.

### Role-Based Node Anatomy

Do not describe every node as just a "box" or "module".

For friendly architecture explainers, assign each role a distinct visual form:

- host zone
  - one larger parent panel containing smaller app-like tiles
- client zone
  - smaller bridge cards, labels, or connector blocks
- server zone
  - repeated server-stack cards or service tower icons
- resource zone
  - literal target cards with one dominant icon plus a short label
- bottom components zone
  - mini cards, pills, or badges arranged as a secondary teaching band

This creates visual rhythm and keeps the diagram from flattening into one visual
temperature.

### Concrete Visual Primitives Are Mandatory

For protocol or architecture teaching infographics, do not stop at generic
phrases such as:

- clean modern infographic
- friendly technical diagram
- readable structure
- polished editorial style

Those phrases are too weak by themselves.

The prompt should explicitly name at least these concrete visual primitives:

- title badge, title ribbon, or highlighted title band
- dashed teaching arrows or equally explicit explanatory connector language
- literal icon metaphors for resource targets
- role-based color mapping for host, client, server, resource, and lower band
- lighter, secondary treatment for the bottom support band

If these are missing, the model often falls back to a static corporate diagram
even when the relationship map is correct.

Treat these as pass-fail items for higher-bar protocol explainers, not as
optional polish.

### Color Role Mapping

When the user wants a community-style explainer, avoid saying only "soft
colors".

Instead, assign color roles:

- one warm section color for the host group
- one cooler or contrast color for clients
- one stable service color for servers
- one distinct support color for resources
- a lighter calmer treatment for the bottom components band

The goal is not rainbow noise. The goal is instantly readable section identity.

### Title And Section Badge Treatment

For community-style explainers, the title and section headers usually need more
than plain text:

- top title band, pill, or highlighted title ribbon
- a visible `Key Components` badge or divider
- section labels that feel like curated teaching markers, not default slide
  headers

These details help the image feel authored instead of auto-laid-out.

### Protocol Explainer Specificity

For protocol, system, or workflow explainers, do not stop at naming the roles.

Also specify:

- what each role looks like
  - app tile, bridge card, server stack, target card, badge chip
- what each role is trying to communicate at a glance
  - source, translation layer, service layer, destination, reference component
- whether the relationship lines should feel
  - direct and mechanical
  - or teaching-oriented and explanatory
- what the title treatment is
  - badge-style, ribbon-style, highlighted band
- what each named resource target uses as its icon metaphor
  - not just `simple icon`, but the actual metaphor

Good prompt language:

- `host zone is a larger parent panel with three app-like source tiles`
- `clients are smaller bridge cards between host and servers`
- `servers are repeated service-stack cards`
- `resource targets are literal icon cards with one large symbol and one short label`
- `bottom components are compact chips or mini cards in a lighter support band`
- `title uses a highlighted badge or ribbon rather than plain floating text`
- `use dashed teaching arrows so the flow reads like an explanation, not raw topology`
- `Local Filesystem uses laptop-plus-folder, Database uses cylinder, Internet / Web APIs uses globe with API badges`
- `host uses warm tones, clients use contrast tones, servers use stable service tones, resources use clean support tones`

Weak prompt language:

- `several modules`
- `some boxes`
- `clean sections`
- `clear arrows`
- `nice icons`
- `soft colors`
- `top title area`
- `recognizable icons`

The stronger version gives the model a visual casting decision instead of
leaving every role to the same default rectangle.

### Column-Based vs Lane-Based Guidance

If the reference rhythm is organized by vertical stacks, prompt the columns
first.

Typical pattern:

- left column: source or host
- middle-left column: client or bridge
- middle-right column: server or processing layer
- right column: external systems or targets

Use explicit lane counts only when the lane structure is itself the message.
Over-constraining the layout as "strict lanes" can push image models toward a
fake presentation-template look.

### Text Budget Rule

For image models:

- prefer short labels
- prefer repeated labels over many unique phrases
- keep paragraphs out of the frame
- ask for readable text, but do not trust the model with dense copy

If exact wording is a hard requirement, treat generated raster output as a style
or composition draft unless proven otherwise.

### Liveliness Layer For Teaching Infographics

If the quality bar is "clear but more alive than a normal box diagram", specify
the liveliness in visual primitives, not empty adjectives.

Good examples of concrete liveliness cues:

- friendly pastel section headers
- app-like tiles for host tools
- small server-stack icons instead of anonymous rectangles
- literal resource symbols such as laptop-plus-folder, database cylinder, globe
  or API/service badges
- dashed connectors that read like explanation lines
- soft off-white or paper-clean background instead of pure product-dashboard UI
- repeated card anatomy so the image feels designed, not randomly assembled

Bad examples:

- "beautiful"
- "high-end"
- "futuristic"
- "more vivid"

Those words rarely create the intended teaching-graphic warmth by themselves.

### Technical Infographic Skeleton

```text
[交付介质：技术信息图 / 架构解释图]
[画面用途：教学解释，不是海报]
[版式总图：上下分区 / 四列结构 / 底部组件区]
[列关系或行关系：左列是什么，中间是什么，右列是什么]
[每个区域的卡片数量与主要标签]
[图的姿态：企业框图 / 友好教学信息图 / 轻量 sketchnote explainer]
[标题处理：顶部标题带 / highlighted title badge / title ribbon，避免只写 top title area]
[卡片语言与箭头语言：圆角卡片、轻描边、虚线箭头、清晰分组，避免只写 clean connectors]
[关键图标隐喻：主机、客户端、服务器、文件、数据库、网络各是什么]
[资源区显式图标：Local Filesystem = laptop-plus-folder，Database = cylinder，Internet / Web APIs = globe plus API/service badges]
[图标语言：扁平、圆角、轻描边、友好]
[文字策略：短标签、英文或中文、少字、大字]
[颜色角色：host/client/server/resource/bottom band 各是什么颜色职责]
[底部区姿态：更轻、更浅、更像辅助说明，不与主结构抢重心]
[颜色与完成度]
[一致性要求：不要合并面板，不要乱加框，不要打乱箭头关系]
[负向约束]
```

## Default Chinese Prompt Skeleton

```text
[交付介质]
[画面用途]
[构图与观看顺序]
[主体设定与设计系统]
[服饰、发型、妆造、道具]
[材料与光线]
[创作视角]
[读者或观者的第一印象顺序]
[环境职责]
[一致性要求]
```

If execution is requested for a Chinese-first image task, default to a
Gemini-family route unless the user explicitly wants a rough built-in draft.

If the selected route is the host-native image path, and the user explicitly
asks to make the image, do not expand route-analysis chatter first. Generate
first, then review whether rerouting is necessary.

## Negative Prompt Skeleton

```text
不要[错误介质]，不要[错误风格默认值]，不要[错误比例语言]，不要[错误材质感]，
不要[错误妆造]，不要[错误背景职责]，不要[与主设计不一致的元素]
```

## Short Repair Checklist

If a prompt keeps failing, check whether it is missing:

1. medium
2. purpose
3. viewing order
4. costume or design structure
5. material specificity
6. linked-artifact consistency

For technical infographics, also check:

7. section map
8. column or row relationships
9. text budget
10. whether the prompt describes a dead schematic instead of a teaching graphic
11. whether title badge, resource icon metaphors, dashed teaching arrows, and
    role-based color mapping were made explicit
12. whether the route should switch to a vector or diagram tool
