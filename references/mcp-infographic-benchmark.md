# MCP Infographic Benchmark

Use this file as a stable benchmark case when testing whether
`visual-prompt-router` can write strong prompts for protocol explainers and
technical teaching infographics.

This benchmark is intentionally prompt-first:

- isolated subagents generate prompts only
- the main thread renders images through one consistent image channel
- prompt quality and image quality are judged separately

## Benchmark Brief

Create a beginner-friendly `Model Context Protocol (MCP)` technical infographic
/ architecture explainer.

Hard facts:

- not a poster
- top title area
- upper relationship map
- lower `Key Components` band
- upper relationship map must explain:
  - left `MCP Host` zone with `Claude Desktop`, `IDE`, `AI Tools`
  - middle three `MCP Client` nodes
  - middle-right three `MCP Server` nodes
  - right three resource targets: `Local Filesystem`, `Database`,
    `Internet / Web APIs`
- lower band must include:
  - `Transport Layers`
  - `Notification`
  - `Sampling`
  - `Tools`
  - `Resources`
  - `Prompts`
- quality bar:
  - clear, modern, friendly, teaching-oriented
  - more alive than a dead enterprise box diagram

## What A Strong Prompt Must Encode

1. Title rhythm:
   - top title band, title badge, or highlighted header treatment
2. Section rhythm:
   - upper architecture zone and lower components band
3. Column logic:
   - host -> client -> server -> resource
4. Role-based node anatomy:
   - host as larger parent panel with app-like source tiles
   - clients as smaller bridge cards
   - servers as repeated service-stack cards
   - resources as literal target cards with dominant icons
   - components as chips, pills, or mini cards
5. Teaching-arrow language:
   - directional, explanatory connectors rather than messy network wiring
6. Color-role mapping:
   - distinct but coordinated section identity
7. Low text budget:
   - short labels, no paragraphs

## Selected Benchmark Prompt

```text
Model Context Protocol (MCP) explained as a friendly technical teaching infographic, not a poster, not a sterile enterprise architecture box diagram. Wide landscape layout, clear educational information design, soft off-white background, crisp readable typography, light shadow depth, clean spacing, approachable but professional.

Top title band with a highlighted badge-style title: "Model Context Protocol (MCP)" and a short subtitle explaining how host, client, server, and resources connect. The upper main zone is a left-to-right protocol relationship map. The far-left host zone is one larger rounded parent panel containing three app-like source tiles: Claude Desktop, IDE, AI Tools. The next column contains three smaller bridge cards labeled MCP Client. The next column contains three repeated service-stack cards labeled MCP Server. The far-right column contains three literal target cards: Local Filesystem shown as laptop-plus-folder, Database shown as a cylinder icon, Internet / Web APIs shown as a globe with tiny API/service badges.

Use neat dashed teaching arrows and clear directional connectors so the flow Host -> Client -> Server -> Resource is obvious at a glance. Keep each region clearly grouped, easy to count, and visually distinct. Assign role-based color identity: warm host group, contrasting client bridge group, stable server group, clean support color for resources.

Add a separate lower band with a visible Key Components badge, containing compact mini cards or chips for Transport Layers, Notification, Sampling, Tools, Resources, Prompts. The bottom band should feel lighter and secondary, supporting the main teaching diagram without competing with it.

Overall the image should feel like a high-quality community-style protocol explainer: friendly teaching infographic, not a product dashboard, not a corporate PPT template, not a network topology map, not a marketing poster. Rounded cards, light outlines, curated icon metaphors, clean visual rhythm, exact short labels, strong readability, lively but controlled.
```

## Representative Isolated Prompt A

```text
横版技术信息图 / 架构解释图，面向初学者讲解 Model Context Protocol (MCP)，不是海报，不是 UI 截图，不是死板企业框图。整体是清楚、亲和、现代的教学信息图风格，先锁版式再谈装饰。顶部有明确标题区，标题简洁醒目，可带一个小的说明副标题；主视觉在上半部分，底部是补充组件区。画面第一眼先看到顶部标题和整体四栏结构，第二眼看到从左到右的协议链路，第三眼再看底部 Key Components 说明。

上半部分采用清晰的左到右关系布局，四个区域在同一视线层级上对齐：最左是 `MCP Host` 区，里面有三个来源卡片，分别标注 `Claude Desktop`、`IDE`、`AI Tools`，用应用窗口 / 电脑 / 工具面板图标表示；中间是三个等宽的 `MCP Client` 卡片，作为桥接层；中右是三个等宽的 `MCP Server` 卡片，作为服务层；最右是三个资源目标卡片，分别是 `Local Filesystem`、`Database`、`Internet / Web APIs`，用文件夹、数据库圆柱、地球 / API 图标表示。用清晰的教学箭头连接 Host -> Client -> Server -> Resource，箭头简洁、有方向性，不要网络拓扑式乱线，不要把关系画复杂。每个区块都要像讲义里的模块卡片，圆角、轻描边、轻阴影、留白充足，层级分明，卡片数量准确可数，标签短而清楚，尽量保留英文原文术语，不要大段说明文字。

底部单独一条 `Key Components` 区域，作为协议补充说明带，排成整齐的小组件卡片或胶囊标签，包含 `Transport Layers`、`Notification`、`Sampling`、`Tools`、`Resources`、`Prompts` 等核心组件。底部区块要与上半部分视觉统一，但更轻、更像辅助讲解模块，不抢主结构。整体配色采用温和但有区分度的教学型信息图配色，每个大区块有轻微不同的辅助色带或浅色底板，既能一眼分区，又不会花哨。图标语言要直观、现代、友好，线条简洁，适度拟物但不要写实渲染。整体像高质量技术课程讲义、协议入门图、开发者文档配图，结构关系一眼看懂，同时比普通死板框图更生动。
```

## Representative Isolated Prompt B

```text
A beginner-friendly technical infographic / architecture explainer about the Model Context Protocol (MCP), not a poster, clean educational diagram with modern friendly visual language, clear hierarchy, large readable title area at the top, structured grid layout, white or very light background with subtle gradients and soft shadows, polished but not overly corporate. Top section has a title band and short subtitle area. Main middle section explains MCP relationships left to right: on the far left a distinct “MCP Host” area containing three source cards labeled Claude Desktop, IDE, AI Tools; in the center three separate MCP Client nodes; center-right three separate MCP Server nodes; far right three resource target cards labeled Local Filesystem, Database, Internet / Web APIs. Use directional arrows and connection lines that make the flow obvious at a glance, with the host feeding clients, clients talking to servers, servers reaching resources. Give each role its own visual color family and node anatomy so host, client, server, and resource are easy to distinguish; use rounded rectangles, small icons, subtle layered depth, and consistent spacing. Add a bottom band titled “Key Components” with compact component chips or cards for Transport Layers, Notification, Sampling, Tools, Resources, Prompts, arranged neatly as a supporting reference section. Overall composition should feel like a clear teaching infographic, lively and approachable, balanced whitespace, visual rhythm, professional editorial design, crisp typography, strong readability, exact labels preserved, no clutter, no decorative excess, no poster composition, no photorealism.
```

## How To Use

1. Ask isolated subagents to write prompts from the benchmark brief only.
2. Compare their outputs against the selected benchmark prompt.
3. If they miss title rhythm, section rhythm, node anatomy, icon metaphors, or
   color-role mapping, patch the skill first.
4. Only after the prompt layer is strong, render the selected benchmark prompt
   and the best isolated prompt through the same image channel.
5. Compare image outputs against:
   - layout integrity
   - role clarity
   - pedagogical warmth
   - visual liveliness
   - text fidelity
