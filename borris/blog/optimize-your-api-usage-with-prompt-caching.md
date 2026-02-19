---
title: "Optimize your API usage with prompt caching"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Optimize your API usage with prompt caching

Prompt caching optimizes your API usage by allowing resuming from specific prefixes in your prompts. This significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements.

Prompt caching stores KV cache representations and cryptographic hashes of cached content, but does not store the raw text of prompts or responses.

## Two ways to enable prompt caching

- **Automatic caching**: Add a single `cache_control` field at the top level of your request. The system automatically applies the cache breakpoint to the last cacheable block. Best for multi-turn conversations.
- **Explicit cache breakpoints**: Place `cache_control` directly on individual content blocks for fine-grained control.

## How prompt caching works

1. The system checks if a prompt prefix is already cached from a recent query.
2. If found, it uses the cached version, reducing processing time and costs.
3. Otherwise, it processes the full prompt and caches the prefix.

Especially useful for prompts with many examples, large context, repetitive tasks, and long multi-turn conversations.

By default, the cache has a 5-minute lifetime, refreshed each time cached content is used. A 1-hour cache duration is also available at additional cost.

## Pricing

| Model | Base Input | 5m Cache Writes | 1h Cache Writes | Cache Hits | Output |
|-------|-----------|-----------------|-----------------|------------|--------|
| Claude Opus 4.6 | $5/MTok | $6.25/MTok | $10/MTok | $0.50/MTok | $25/MTok |
| Claude Sonnet 4.6 | $3/MTok | $3.75/MTok | $6/MTok | $0.30/MTok | $15/MTok |
| Claude Haiku 4.5 | $1/MTok | $1.25/MTok | $2/MTok | $0.10/MTok | $5/MTok |

Cache write tokens are 1.25x base price (5-minute) or 2x base price (1-hour). Cache read tokens are 0.1x base price.

## Supported models

Claude Opus 4.6, Claude Opus 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Sonnet 4, Claude Sonnet 3.7, Claude Haiku 4.5, Claude Haiku 3.5, Claude Haiku 3.

## Automatic caching

Add `"cache_control": {"type": "ephemeral"}` at the top level of your request body. The cache point moves forward automatically as conversations grow.

## Explicit cache breakpoints

Place `cache_control` directly on individual content blocks. You can define up to 4 cache breakpoints. Cache prefixes are created in order: tools, system, then messages.

The system uses a 20-block lookback window to check for cache hits backwards from each explicit breakpoint.

## Cache limitations

Minimum cacheable prompt length:
- 4096 tokens for Claude Opus 4.6, Claude Opus 4.5
- 1024 tokens for Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4, and Claude Sonnet 3.7
- 4096 tokens for Claude Haiku 4.5
- 2048 tokens for Claude Haiku 3.5 and Claude Haiku 3

## What can be cached

Tools, system messages, text messages (user and assistant turns), images and documents, tool use and tool results.

## What invalidates the cache

- Modifying tool definitions invalidates the entire cache
- Enabling/disabling web search or citations modifies the system prompt
- Switching speed settings invalidates system and message caches
- Changes to tool_choice only affect message blocks
- Adding/removing images affects message blocks
- Changes to extended thinking settings affect message blocks

## Tracking cache performance

Monitor using these API response fields:
- `cache_creation_input_tokens`: Tokens written to cache
- `cache_read_input_tokens`: Tokens retrieved from cache
- `input_tokens`: Tokens after the last cache breakpoint (not cached)

Total input tokens = cache_read_input_tokens + cache_creation_input_tokens + input_tokens

## Best practices

- Start with automatic caching for multi-turn conversations
- Cache stable, reusable content at the prompt's beginning
- Use up to 4 breakpoints strategically
- Regularly analyze cache hit rates
- Optimize for your use case (conversational agents, coding assistants, large document processing, etc.)
