---
title: "Prompt Caching Launch Post"
source_url: "https://www.anthropic.com/news/prompt-caching"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Prompt Caching Launch Post

## Overview

Claude offers prompt caching, a feature that enables developers to cache frequently used context between API calls. This capability reduces costs by up to 90% and latency by up to 85% for long prompts.

## When to Use Prompt Caching

Prompt caching proves effective in several scenarios:

- Conversational agents: Lower costs and faster responses for extended conversations with long instructions or uploaded documents
- Coding assistants: Enhanced autocomplete and codebase Q&A through cached codebase summaries
- Large document processing: Incorporate complete long-form material and images without increasing response latency
- Detailed instruction sets: Share extensive lists of instructions and numerous high-quality output examples
- Agentic search and tool use: Improve performance across multiple rounds of tool calls and iterative changes
- Knowledge base applications: Embed entire documents into prompts for users to query against books, papers, documentation, and transcripts

## Performance Improvements

Early customers have demonstrated substantial improvements:

| Use Case | TTFT Without | TTFT With | Cost Reduction |
|----------|-------------|-----------|----------------|
| Chat with a book (100K tokens) | 11.5 seconds | 2.4 seconds (-79%) | -90% |
| Many-shot prompting (10K tokens) | 1.6 seconds | 1.1 seconds (-31%) | -86% |
| Multi-turn conversation (10-turn) | ~10 seconds | ~2.5 seconds (-75%) | -53% |

## Pricing Structure

Cached prompts use a tiered pricing model:

- Cache writes: 25% premium over standard input token pricing
- Cache reads: 10% of standard input token pricing

### Rates by Model

Claude 3.5 Sonnet:
- Input: $3/million tokens
- Cache write: $3.75/million tokens
- Cache read: $0.30/million tokens
- Output: $15/million tokens

Claude 3 Opus:
- Input: $15/million tokens
- Cache write: $18.75/million tokens
- Cache read: $1.50/million tokens
- Output: $75/million tokens

Claude 3 Haiku:
- Input: $0.25/million tokens
- Cache write: $0.30/million tokens
- Cache read: $0.03/million tokens
- Output: $1.25/million tokens

## Availability

Prompt caching is generally available on the Anthropic API and available in preview on Amazon Bedrock and Google Cloud's Vertex AI.

## Getting Started

Developers can access documentation and pricing details through the Anthropic API platform to begin implementing prompt caching in their applications.
