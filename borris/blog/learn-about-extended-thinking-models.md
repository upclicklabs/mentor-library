---
title: "Learn about extended thinking models"
source_url: "https://docs.anthropic.com/en/docs/about-claude/models/extended-thinking-models"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Learn about extended thinking models

Extended thinking gives Claude enhanced reasoning capabilities for complex tasks, providing varying levels of transparency into its step-by-step thought process before delivering its final answer.

Note: For Claude Opus 4.6, use adaptive thinking (`thinking: {type: "adaptive"}`) with the effort parameter instead of manual thinking mode. The manual `thinking: {type: "enabled", budget_tokens: N}` is deprecated on Opus 4.6.

## Supported models

- Claude Opus 4.6 - adaptive thinking only; manual mode deprecated
- Claude Opus 4.5
- Claude Opus 4.1
- Claude Opus 4
- Claude Sonnet 4.6 - supports both manual extended thinking with interleaved mode and adaptive thinking
- Claude Sonnet 4.5
- Claude Sonnet 4
- Claude Haiku 4.5

## How extended thinking works

When enabled, Claude creates `thinking` content blocks with internal reasoning, then incorporates insights before crafting a final response. The response includes `thinking` blocks followed by `text` blocks.

## How to use extended thinking

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{
        "role": "user",
        "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
    }],
)
```

The `budget_tokens` parameter determines maximum tokens for internal reasoning. Larger budgets can improve response quality for complex problems.

## Summarized thinking

Claude 4 models return a summary of Claude's full thinking process (not the raw thinking). Key points:
- You're charged for full thinking tokens, not the summary tokens
- The billed output token count will NOT match the visible count
- First few lines are more verbose, useful for prompt engineering
- Summarization preserves key ideas with minimal added latency

Claude Sonnet 3.7 continues to return full thinking output.

## Streaming thinking

Stream extended thinking responses using server-sent events (SSE). Thinking content arrives via `thinking_delta` events.

## Extended thinking with tool use

When using tools with thinking:
- Tool choice only supports `auto` or `none` (not `any` or forced tool use)
- You must pass `thinking` blocks back to the API for the last assistant message
- Include complete unmodified blocks to maintain reasoning continuity

### Interleaved thinking

Claude 4 models support thinking between tool calls:
- **Opus 4.6**: Automatically enabled with adaptive thinking
- **Sonnet 4.6**: Supports the `interleaved-thinking-2025-05-14` beta header or adaptive thinking
- **Other Claude 4 models**: Add the beta header to enable

With interleaved thinking, `budget_tokens` can exceed `max_tokens` as it represents total budget across all thinking blocks within one assistant turn.

## Extended thinking with prompt caching

- Thinking blocks from previous turns are removed from context, affecting cache breakpoints
- Changes to thinking parameters invalidate message cache breakpoints
- System prompts and tools remain cached despite thinking parameter changes

## Context window with extended thinking

- Thinking blocks from previous turns are stripped (not counted towards context window)
- Current turn thinking counts towards `max_tokens`
- `max_tokens` is enforced as a strict limit -- validation error if prompt tokens + max_tokens exceeds context window

## Thinking encryption

Full thinking content is encrypted in the `signature` field for verification. Occasionally, safety systems may flag internal reasoning, returning `redacted_thinking` blocks with encrypted content that is decrypted when passed back to the API.

## Differences across model versions

| Feature | Claude Sonnet 3.7 | Claude 4 (pre-4.5) | Claude Opus 4.5 | Claude Sonnet 4.6 | Claude Opus 4.6 |
|---|---|---|---|---|---|
| Thinking Output | Full | Summarized | Summarized | Summarized | Summarized |
| Interleaved Thinking | No | Beta header | Beta header | Beta header or adaptive | Automatic with adaptive |
| Thinking Block Preservation | Not preserved | Not preserved | Preserved by default | Preserved by default | Preserved by default |

## Best practices

### Working with thinking budgets
- Minimum budget: 1,024 tokens
- Start with larger budgets (16k+) for complex tasks
- For budgets above 32k, use batch processing
- Monitor thinking token usage to optimize costs

### Performance considerations
- Be prepared for longer response times
- SDKs require streaming when `max_tokens` > 21,333
- Handle both thinking and text content blocks when streaming

### Feature compatibility
- Not compatible with `temperature` or `top_k` modifications
- Can set `top_p` to values between 1 and 0.95 when enabled
- Cannot pre-fill responses when thinking is enabled
