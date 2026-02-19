---
title: "Prompt Caching"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Prompt Caching

Prompt caching optimizes your API usage by allowing resuming from specific prefixes in your prompts. This significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements.

There are two ways to enable prompt caching:

- **Automatic caching**: Add a single `cache_control` field at the top level of your request. The system automatically applies the cache breakpoint to the last cacheable block and moves it forward as conversations grow. Best for multi-turn conversations where the growing message history should be cached automatically.
- **Explicit cache breakpoints**: Place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached.

## How Prompt Caching Works

When you send a request with prompt caching enabled:

1. The system checks if a prompt prefix, up to a specified cache breakpoint, is already cached from a recent query.
2. If found, it uses the cached version, reducing processing time and costs.
3. Otherwise, it processes the full prompt and caches the prefix once the response begins.

This is especially useful for:
- Prompts with many examples
- Large amounts of context or background information
- Repetitive tasks with consistent instructions
- Long multi-turn conversations

By default, the cache has a 5-minute lifetime. The cache is refreshed for no additional cost each time the cached content is used.

## Pricing

Prompt caching introduces a new pricing structure. Cache write tokens cost 1.25x the base input token price (for 5-minute TTL) or 2x for 1-hour TTL. Cache read tokens cost 0.1x the base input token price.

## Supported Models

Prompt caching is currently supported on Claude Opus 4.6, Claude Opus 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Sonnet 4, Claude Haiku 4.5, Claude Haiku 3.5, and Claude Haiku 3.

## Automatic Caching

Automatic caching is the simplest way to enable prompt caching. Instead of placing `cache_control` on individual content blocks, add a single `cache_control` field at the top level of your request body. The system automatically applies the cache breakpoint to the last cacheable block.

With automatic caching, the cache point moves forward automatically as conversations grow. Each new request caches everything up to the last cacheable block, and previous content is read from cache.

## Explicit Cache Breakpoints

For more control over caching, you can place `cache_control` directly on individual content blocks. This is useful when you need to cache different sections that change at different frequencies, or need fine-grained control over exactly what gets cached.

You can define up to 4 cache breakpoints. Cache breakpoints themselves don't add any cost.

## Cache Limitations

The minimum cacheable prompt length varies by model:
- 4096 tokens for Claude Opus 4.6, Claude Opus 4.5
- 1024 tokens for Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4
- 4096 tokens for Claude Haiku 4.5
- 2048 tokens for Claude Haiku 3.5 and Claude Haiku 3

## What Can Be Cached

- Tools: Tool definitions in the `tools` array
- System messages: Content blocks in the `system` array
- Text messages: Content blocks in the `messages.content` array
- Images and Documents: Content blocks in the `messages.content` array, in user turns
- Tool use and tool results: Content blocks in the `messages.content` array

## 1-Hour Cache Duration

For prompts used less frequently than every 5 minutes but more than every hour, a 1-hour cache TTL is available at 2x the base input token price. Specify with `"ttl": "1h"` in the cache_control definition.

## Best Practices

- Start with automatic caching for multi-turn conversations
- Use explicit block-level breakpoints when caching sections with different change frequencies
- Cache stable, reusable content like system instructions and background information
- Place cached content at the prompt's beginning for best performance
- Regularly analyze cache hit rates and adjust strategy as needed

## Tracking Cache Performance

Monitor cache performance using these API response fields:
- `cache_creation_input_tokens`: Number of tokens written to the cache
- `cache_read_input_tokens`: Number of tokens retrieved from the cache
- `input_tokens`: Number of input tokens not read from or used to create a cache
