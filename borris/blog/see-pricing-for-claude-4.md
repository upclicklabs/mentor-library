---
title: "See pricing for Claude 4"
source_url: "https://docs.anthropic.com/en/docs/about-claude/pricing"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# See pricing for Claude 4

All prices are in USD. For the most current pricing, visit claude.com/pricing.

## Model pricing

| Model | Base Input Tokens | 5m Cache Writes | 1h Cache Writes | Cache Hits & Refreshes | Output Tokens |
|---|---|---|---|---|---|
| Claude Opus 4.6 | $5/MTok | $6.25/MTok | $10/MTok | $0.50/MTok | $25/MTok |
| Claude Opus 4.5 | $5/MTok | $6.25/MTok | $10/MTok | $0.50/MTok | $25/MTok |
| Claude Opus 4.1 | $15/MTok | $18.75/MTok | $30/MTok | $1.50/MTok | $75/MTok |
| Claude Opus 4 | $15/MTok | $18.75/MTok | $30/MTok | $1.50/MTok | $75/MTok |
| Claude Sonnet 4.6 | $3/MTok | $3.75/MTok | $6/MTok | $0.30/MTok | $15/MTok |
| Claude Sonnet 4.5 | $3/MTok | $3.75/MTok | $6/MTok | $0.30/MTok | $15/MTok |
| Claude Sonnet 4 | $3/MTok | $3.75/MTok | $6/MTok | $0.30/MTok | $15/MTok |
| Claude Haiku 4.5 | $1/MTok | $1.25/MTok | $2/MTok | $0.10/MTok | $5/MTok |
| Claude Haiku 3.5 | $0.80/MTok | $1/MTok | $1.6/MTok | $0.08/MTok | $4/MTok |
| Claude Haiku 3 | $0.25/MTok | $0.30/MTok | $0.50/MTok | $0.03/MTok | $1.25/MTok |

Cache pricing multipliers:
- 5-minute cache write tokens: 1.25x base input price
- 1-hour cache write tokens: 2x base input price
- Cache read tokens: 0.1x base input price

## Third-party platform pricing

Claude models are available on AWS Bedrock, Google Vertex AI, and Microsoft Foundry. Starting with Claude Sonnet 4.5 and Haiku 4.5, regional endpoints include a 10% premium over global endpoints. The Claude API (1P) is global by default and unaffected.

## Feature-specific pricing

### Data residency pricing

For Claude Opus 4.6 and newer, specifying US-only inference via `inference_geo` incurs a 1.1x multiplier on all token pricing categories.

### Fast mode pricing

Fast mode for Claude Opus 4.6 (research preview) provides significantly faster output at premium pricing (6x standard rates):

| Context window | Input | Output |
|---|---|---|
| <= 200K input tokens | $30/MTok | $150/MTok |
| > 200K input tokens | $60/MTok | $225/MTok |

### Batch processing

50% discount on both input and output tokens:

| Model | Batch input | Batch output |
|---|---|---|
| Claude Opus 4.6 | $2.50/MTok | $12.50/MTok |
| Claude Sonnet 4.6 | $1.50/MTok | $7.50/MTok |
| Claude Haiku 4.5 | $0.50/MTok | $2.50/MTok |

### Long context pricing

When exceeding 200K input tokens with 1M context window enabled:

| Model | <= 200K input | > 200K input |
|---|---|---|
| Claude Opus 4.6 | $5/MTok input, $25/MTok output | $10/MTok input, $37.50/MTok output |
| Claude Sonnet 4.6/4.5/4 | $3/MTok input, $15/MTok output | $6/MTok input, $22.50/MTok output |

### Tool use pricing

Priced based on total input tokens (including tools parameter) plus output tokens. Server-side tools may incur additional charges.

### Specific tool pricing

- **Web search**: $10 per 1,000 searches plus standard token costs
- **Web fetch**: No additional cost beyond standard token costs
- **Code execution**: Free when used with web search or web fetch; otherwise billed by execution time ($0.05/hour/container after 1,550 free hours/month)
- **Text editor**: Standard tool pricing plus 700 additional input tokens
- **Bash tool**: Adds 245 input tokens
- **Computer use**: Standard tool pricing plus 735 tokens per tool definition

## Rate limits

Rate limits vary by usage tier (Tier 1 through Enterprise). For higher rate limits or custom pricing, contact sales.
