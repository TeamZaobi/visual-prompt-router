# OpenAI-Codex ImageGen Routing

Use this note when a visual task mentions `Codex imagegen`, `CodeX CLI imagegen`, `openai-codex`, or Hermes `image_generate`.

## Lesson

`openai-codex` can be a Hermes `image_generate` provider, not necessarily a reason to launch `codex exec`.

If the user has run commands like:

```bash
hermes config set image_gen.provider openai-codex
hermes config set image_gen.openai-codex.model gpt-image-2-medium
```

or explicitly says "directly call image_generate", the route is fixed:

1. Use the `image_generate` tool directly.
2. Do not run `codex exec` to probe whether the Codex CLI has an imagegen tool.
3. Do not keep retrying Codex model names when CLI auth/model support fails.
4. Generate the requested image(s), copy/save them into the project delivery directory, then validate them.

## Failure Pattern To Avoid

A provider name containing `codex` caused the assistant to route through Codex CLI, hit model/account errors, discover a hidden Codex imagegen skill, and spend time capability-probing. The user corrected the flow: after configuring Hermes image generation to `openai-codex`, the correct executor was Hermes `image_generate`.

## Validation Pattern

For teaching infographics and other text-heavy visuals:

1. Generate with `image_generate`.
2. Save/copy from cache to the project artifact directory.
3. Verify file size and dimensions with PIL or an image metadata tool.
4. Use visual review for content risks, especially formula/text errors.
5. If review finds a pedagogical error, regenerate that asset with a narrower prompt rather than sending it.

## Delivery Note

If downstream chat delivery fails with a stale QQBot target such as `频道不存在`, record the generated image paths and ask for a refreshed QQ target or for the user/group to message the bot first. Do not claim QQ delivery succeeded until the send tool returns success.