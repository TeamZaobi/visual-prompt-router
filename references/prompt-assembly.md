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
4. icon language
5. palette and finish

Rule:

For technical infographics, layout nouns beat style adjectives.

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

### Technical Infographic Skeleton

```text
[交付介质：技术信息图 / 架构解释图]
[画面用途：教学解释，不是海报]
[版式总图：上下分区 / 四列结构 / 底部组件区]
[列关系或行关系：左列是什么，中间是什么，右列是什么]
[每个区域的卡片数量与主要标签]
[图标语言：扁平、圆角、轻描边、友好]
[文字策略：短标签、英文或中文、少字、大字]
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
10. whether the route should switch to a vector or diagram tool
