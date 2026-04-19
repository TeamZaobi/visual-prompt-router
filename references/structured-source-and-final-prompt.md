# Structured Source vs Final Prompt

Use this file when the question is not "can JSON exist", but "where should the
JSON live".

The short answer:

- structured metadata is good as an internal source of truth
- raw JSON is usually bad as the final prompt sent to Gemini website image
  generation

## Core Rule

Keep structure on the source side.

Keep the final image prompt on the render side.

That means:

- use JSON or metadata to separate facts, layout, forbidden links, role colors,
  and text budget
- do not assume those braces, keys, quotes, and schema labels should be pasted
  into the model as the final browser prompt

## What Structured Source Is Good For

Use structured source when you need durable separation between:

- source facts
- visible labels
- non-visible constraints
- layout relationships
- semantic tiers
- role-color mapping
- negative constraints
- route metadata

This is especially useful for leadership-briefing architecture explainers where
the prompt must keep these apart:

- current visible primary surface
- operational hinge
- backstage formal service
- forbidden direct links

Structured source helps prevent the common failure where requirement language,
governance language, and on-image text all get blended together.

## What Raw JSON Is Bad For

For Gemini website image generation, raw JSON is usually a poor final prompt
because:

1. keys and braces consume attention without improving the rendered picture
2. schema words can dilute the main scene objective
3. long multi-line payloads make browser input and send behavior more fragile
4. the model may latch onto a stray salient phrase instead of the intended
   layout
5. prompt readability for a human reviewer gets worse right when fast prompt
   diagnosis matters most

Practical implication:

- use JSON to think
- use compact natural language to render

## Compiler Contract

When the source is structured, compile it into a final prompt with these steps:

1. Convert semantic tiers into direct image instructions.
2. Convert visible text into the exact labels that may appear on the image.
3. Convert relationships into directional layout sentences.
4. Convert forbidden states into negative prompt clauses.
5. Convert color-role mapping into explicit card or node color wording.
6. Remove schema noise such as braces, key names, quotes, and container labels.
7. Compress into a compact browser-friendly prompt when the target route is a
   website textbox.

## Recommended Source Shape

Internal source can look like this:

```json
{
  "task": "leadership briefing architecture explainer",
  "render_text": {
    "title": "省平台P2试点架构图",
    "labels": ["研究前台", "MCP 受控接入", "审核与回执中枢", "人工服务台", "真实数据"]
  },
  "semantic_tiers": {
    "primary_surface": "研究前台与当前演示主面",
    "operational_hinge": "审核与回执中枢",
    "backstage_formal_service": "人工服务台与真实数据"
  },
  "relations": [
    "研究前台 -> MCP 受控接入",
    "MCP 受控接入 -> 审核与回执中枢",
    "审核与回执中枢 -> 人工服务台 -> 真实数据"
  ],
  "forbid": [
    "前台直连真实数据",
    "把后台正式服务画成全图最大主角"
  ]
}
```

This is good source material.

It is not automatically a good final Gemini prompt.

## Recommended Final Prompt Shape

The compiled final prompt should read like image instructions, not like a data
schema.

Good pattern:

```text
领导汇报型中文架构解释图。标题“省平台P2试点架构图”。16:9，白底或极浅暖白底。第一眼看到研究前台与当前演示主面，第二眼看到审核与回执中枢作为正式受理和服务编排枢纽，第三眼看到人工服务台与真实数据作为后台正式服务，显式存在但视觉次于主面。前台不能直接连真实数据，必须经过审核与回执中枢和人工服务台。保留短标签、圆角卡片、低饱和分区色、细线、轻阴影，不要工程流程图，不要 giant database。
```

## Browser Input Rule

If the final route is a browser create-image textbox:

- prefer a compact prompt over a sprawling multi-line block
- if the site input is fragile, prefer a single compact paragraph
- do not keep diagnostic JSON in the send buffer after you already know the
  model does not benefit from it

## Keep JSON Where It Helps

JSON is still strongly recommended for:

- browser adapter decision metadata
- route cards
- resumable download state
- prompt source facts
- prompt compiler inputs

Do not collapse those good internal uses just because raw JSON was a bad final
render prompt.

## User-Facing Compression

When explaining the rule to the user, compress it to:

- JSON is good as source truth
- natural language is better as the final Gemini image prompt
