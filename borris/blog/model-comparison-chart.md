---
title: "Model Comparison Chart"
source_url: "https://docs.anthropic.com/en/docs/about-claude/models/overview"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Model Comparison Chart

Claude is a family of state-of-the-art large language models developed by Anthropic. All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available via the Claude API, AWS Bedrock, and Google Vertex AI.

## Latest Models Comparison

| Feature | Claude Opus 4.6 | Claude Sonnet 4.6 | Claude Haiku 4.5 |
|:--------|:----------------|:------------------|:-----------------|
| Description | The most intelligent model for building agents and coding | The best combination of speed and intelligence | The fastest model with near-frontier intelligence |
| Claude API ID | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5-20251001 |
| Claude API alias | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5 |
| AWS Bedrock ID | anthropic.claude-opus-4-6-v1 | anthropic.claude-sonnet-4-6 | anthropic.claude-haiku-4-5-20251001-v1:0 |
| GCP Vertex AI ID | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5@20251001 |
| Pricing | $5 / input MTok, $25 / output MTok | $3 / input MTok, $15 / output MTok | $1 / input MTok, $5 / output MTok |
| Extended thinking | Yes | Yes | Yes |
| Adaptive thinking | Yes | Yes | No |
| Priority Tier | Yes | Yes | Yes |
| Comparative latency | Moderate | Fast | Fastest |
| Context window | 200K tokens / 1M tokens (beta) | 200K tokens / 1M tokens (beta) | 200K tokens |
| Max output | 128K tokens | 64K tokens | 64K tokens |
| Reliable knowledge cutoff | May 2025 | Aug 2025 | Feb 2025 |
| Training data cutoff | Aug 2025 | Jan 2026 | Jul 2025 |

Notes:
- Claude Opus 4.6 and Sonnet 4.6 support a 1M token context window when using the context-1m-2025-08-07 beta header. Long context pricing applies to requests exceeding 200K tokens.
- Models with the same snapshot date are identical across all platforms and do not change.
- Starting with Claude Sonnet 4.5 and all subsequent models, AWS Bedrock and Google Vertex AI offer global endpoints (dynamic routing) and regional endpoints (guaranteed data routing) with different pricing.

## Legacy Models

| Feature | Claude Sonnet 4.5 | Claude Opus 4.5 | Claude Opus 4.1 | Claude Sonnet 4 | Claude Opus 4 | Claude Haiku 3 (deprecated) |
|:--------|:------------------|:----------------|:----------------|:----------------|:--------------|:----------------------------|
| Claude API ID | claude-sonnet-4-5-20250929 | claude-opus-4-5-20251101 | claude-opus-4-1-20250805 | claude-sonnet-4-20250514 | claude-opus-4-20250514 | claude-3-haiku-20240307 |
| Claude API alias | claude-sonnet-4-5 | claude-opus-4-5 | claude-opus-4-1 | claude-sonnet-4-0 | claude-opus-4-0 | -- |
| Pricing | $3/$15 MTok | $5/$25 MTok | $15/$75 MTok | $3/$15 MTok | $15/$75 MTok | $0.25/$1.25 MTok |
| Extended thinking | Yes | Yes | Yes | Yes | Yes | No |
| Context window | 200K / 1M (beta) | 200K | 200K | 200K / 1M (beta) | 200K | 200K |
| Max output | 64K | 64K | 32K | 64K | 32K | 4K |

Claude Haiku 3 (claude-3-haiku-20240307) is deprecated and will be retired on April 19, 2026. Migrate to Claude Haiku 4.5 before the retirement date.

## Performance

Claude 4 models excel in:
- Performance: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing
- Engaging responses: Ideal for applications requiring rich, human-like interactions
- Output quality: Larger improvements in overall performance when migrating from previous model generations

## Migrating to Claude 4.6

If you're currently using older Claude models, consider migrating to Claude Opus 4.6 to take advantage of improved intelligence and enhanced capabilities.
