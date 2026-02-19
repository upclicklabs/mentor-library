---
title: "Easily switch to Claude 4 models with the model migration checklist"
source_url: "https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Easily switch to Claude 4 models with the model migration checklist

Guide for migrating to Claude 4.6 models from previous Claude versions.

## Migrating to Claude 4.6

Claude Opus 4.6 is a near drop-in replacement for Claude 4.5, with a few breaking changes to be aware of.

### Update your model name

```python
# Opus migration
model = "claude-opus-4-5"  # Before
model = "claude-opus-4-6"  # After
```

### Breaking changes

1. **Prefill removal:** Prefilling assistant messages returns a 400 error on Claude 4.6 models. Use structured outputs, system prompt instructions, or `output_config.format` instead.

2. **Tool parameter quoting:** Claude 4.6 models may produce slightly different JSON string escaping in tool call arguments. Standard JSON parsers handle these differences automatically.

### Recommended changes

1. **Migrate to adaptive thinking:** `thinking: {type: "enabled", budget_tokens: N}` is deprecated on Claude 4.6 models. Switch to `thinking: {type: "adaptive"}` and use the effort parameter to control thinking depth.

```python
# Before
response = client.beta.messages.create(
    model="claude-opus-4-5",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 32000},
    betas=["interleaved-thinking-2025-05-14"],
    messages=[...],
)

# After
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[...],
)
```

2. **Remove effort beta header:** The effort parameter is now GA. Remove `betas=["effort-2025-11-24"]`.

3. **Remove fine-grained tool streaming beta header:** Now GA. Remove `betas=["fine-grained-tool-streaming-2025-05-14"]`.

4. **Remove interleaved thinking beta header (Opus 4.6 only):** Adaptive thinking automatically enables interleaved thinking on Opus 4.6.

5. **Migrate to output_config.format:** Update `output_format={...}` to `output_config={"format": {...}}`.

### Migrating from Claude 4.1 or earlier to Claude 4.6

Additional breaking changes apply:

1. **Update sampling parameters:** Use only `temperature` OR `top_p`, not both.
2. **Update tool versions:** Use `text_editor_20250728` and `code_execution_20250825`.
3. **Handle the `refusal` stop reason.**
4. **Handle the `model_context_window_exceeded` stop reason.**
5. **Verify tool parameter handling (trailing newlines).**
6. **Update prompts for behavioral changes:** Claude 4+ models have a more concise, direct communication style.

### Claude 4.6 migration checklist

- Update model ID to `claude-opus-4-6`
- BREAKING: Remove assistant message prefills (returns 400 error)
- Recommended: Migrate from `thinking: {type: "enabled", budget_tokens: N}` to `thinking: {type: "adaptive"}` with effort parameter
- Verify tool call JSON parsing uses a standard JSON parser
- Remove beta headers (effort, fine-grained-tool-streaming, interleaved-thinking for Opus 4.6)
- Migrate `output_format` to `output_config.format`
- If migrating from Claude 4.1 or earlier: update sampling parameters, tool versions, handle new stop reasons
- Review and update prompts following prompting best practices
- Test in development environment before production deployment

## Migrating to Claude Sonnet 4.6

```python
model = "claude-sonnet-4-5"  # Before
model = "claude-sonnet-4-6"  # After
```

### Breaking changes from Sonnet 4.5

1. **Prefilling assistant messages is no longer supported** - returns 400 error.
2. **Tool parameter JSON escaping may differ.**

### Sonnet 4.6 migration checklist

- Update model ID to `claude-sonnet-4-6`
- BREAKING: Remove assistant message prefilling
- BREAKING: Verify tool parameter JSON parsing
- Remove `fine-grained-tool-streaming-2025-05-14` beta header
- Migrate `output_format` to `output_config.format`
- Consider enabling extended thinking or adaptive thinking for complex reasoning tasks
- Test in development environment before production deployment
