# MCP Imagegen Render Pack

Use this pack when the runtime exposes the built-in `image_gen` tool and the
goal is to validate whether `visual-prompt-router` can now produce
community-quality protocol explainer images for MCP-style architecture
infographics.

## Test Goal

Render two prompt variants through the same image-generation channel.

Hold constant:

- same subject
- same relationship facts
- same backend
- same reviewer rubric

Change only:

- prompt wording

## Shared Brief

Create a beginner-friendly technical infographic that explains the Model
Context Protocol (MCP). It is not a poster and not a dead enterprise diagram.

Required content:

- top title area
- upper relationship map
- lower `Key Components` band
- left `MCP Host` zone with `Claude Desktop`, `IDE`, `AI Tools`
- three `MCP Client` nodes
- three `MCP Server` nodes
- right-side resource targets: `Local Filesystem`, `Database`,
  `Internet / Web APIs`
- lower `Key Components`: `Transport Layers`, `Notification`, `Sampling`,
  `Tools`, `Resources`, `Prompts`

Desired outcome:

- clearly structured
- warm, friendly, and lively
- close to community-style teaching infographic quality

## Prompt A

```text
Use case: infographic-diagram
Asset type: protocol explainer image
Primary request: Model Context Protocol (MCP) explained as a friendly technical teaching infographic, not a poster, not a sterile enterprise architecture box diagram. Wide landscape layout. Top title band with a highlighted badge-style title and a short explanatory subtitle. The upper main zone is a left-to-right protocol relationship map. The far-left host zone is one larger rounded parent panel containing three app-like source tiles: Claude Desktop, IDE, AI Tools. The next column contains three smaller bridge cards labeled MCP Client. The next column contains three repeated service-stack cards labeled MCP Server. The far-right column contains three literal target cards: Local Filesystem shown as laptop-plus-folder, Database shown as a cylinder icon, Internet / Web APIs shown as a globe with tiny API/service badges. Use neat dashed teaching arrows and clear directional connectors so the flow Host -> Client -> Server -> Resource is obvious at a glance. Add a separate lower band with a visible Key Components badge, containing compact mini cards or chips for Transport Layers, Notification, Sampling, Tools, Resources, Prompts. Use role-based color identity: warm host group, contrasting client bridge group, stable server group, clean support color for resources, lighter calmer band for bottom components. Rounded cards, light outlines, subtle shadow depth, soft off-white background, clean spacing, high readability, curated educational infographic rhythm, approachable but professional.
Style/medium: friendly technical infographic, educational explainer, vector-like polished raster
Composition/framing: wide 16:9 landscape, title zone on top, upper architecture zone, lower components band
Lighting/mood: bright, calm, friendly, clean, editorial
Color palette: soft off-white base, warm yellow host accents, cool violet or blue client accents, stable amber or gold server accents, light cyan or blue resource accents, pale green or mint lower component band
Text (verbatim): "Model Context Protocol (MCP)", "MCP Host", "Claude Desktop", "IDE", "AI Tools", "MCP Client", "MCP Server", "Local Filesystem", "Database", "Internet / Web APIs", "Key Components", "Transport Layers", "Notification", "Sampling", "Tools", "Resources", "Prompts"
Constraints: preserve exact role counts and left-to-right hierarchy; keep the lower band clearly separate; make each role visually distinct by card anatomy and color role; prioritize readability and teaching rhythm
Avoid: poster composition, dashboard UI, dark cyberpunk style, network-topology spaghetti lines, identical anonymous rectangles for all roles, clutter, photorealism, dense paragraphs, tiny unreadable labels
```

## Prompt B

```text
Use case: infographic-diagram
Asset type: protocol architecture explainer
Primary request: A beginner-friendly MCP protocol explainer infographic for developers, designed like a polished course handout rather than a corporate flowchart. The image should feel authored, warm, and easy to scan. At the top, place a soft title ribbon or pill-shaped title badge for "Model Context Protocol (MCP)" with a short subtitle beneath it. In the upper main section, build a strict four-column teaching layout from left to right. Column one is the MCP Host area: one larger rounded panel containing three small app-like tiles for Claude Desktop, IDE, and AI Tools. Column two is a bridge layer of three MCP Client cards, smaller and lighter than the host panel. Column three is a service layer of three MCP Server stack cards with repeated visual anatomy. Column four contains three literal destination cards: Local Filesystem with a laptop-and-folder symbol, Database with a cylinder symbol, Internet / Web APIs with a globe and tiny API badges. Connect the columns with clean explanatory arrows, slightly curved or dashed, so the relationship reads instantly. At the bottom, add a clearly separated Key Components strip with compact mini cards for Transport Layers, Notification, Sampling, Tools, Resources, and Prompts. Give the whole graphic a soft paper-clean background, generous spacing, rounded cards, light outlines, gentle shadowing, section labels, and role-specific color identity. The result should be lively and approachable, like a community-loved technical explainer image, not a stiff enterprise schematic.
Style/medium: educational technical infographic with friendly iconography and clean vector-like forms
Composition/framing: balanced horizontal infographic, title ribbon, upper four-column architecture map, lower chip-based component strip
Lighting/mood: light, calm, friendly, handout-like, approachable but precise
Color palette: warm cream background, butter-yellow host panel, lavender client bridges, honey or orange server stacks, sky-blue resource targets, mint or pale green lower component strip
Text (verbatim): "Model Context Protocol (MCP)", "MCP Host", "Claude Desktop", "IDE", "AI Tools", "MCP Client", "MCP Server", "Local Filesystem", "Database", "Internet / Web APIs", "Key Components", "Transport Layers", "Notification", "Sampling", "Tools", "Resources", "Prompts"
Constraints: keep the layout highly legible; use different node anatomy for host, client, server, resource, and component rows; preserve the exact protocol chain; keep the image more lively than a standard architecture chart
Avoid: marketing poster look, slide-template look, dark high-tech glow, too many lines, flat monochrome corporate boxes, chaotic layout, inaccurate text, extra narrative objects, photoreal 3D rendering
```

## Review Rubric

Score each image from 1 to 5 on:

1. layout integrity
2. role clarity and node anatomy
3. pedagogical warmth and visual liveliness
4. title and section rhythm
5. icon metaphor clarity
6. text fidelity
7. closeness to a community-style explainable infographic rather than a dead
   enterprise chart

## Decision Rule

- If both prompts still render as dead diagrams, patch the skill again.
- If one prompt clearly wins, promote its visual primitives into the skill.
- If the structure is right but labels fail repeatedly, treat that as a backend
  or raster-medium limit and escalate reroute guidance.
