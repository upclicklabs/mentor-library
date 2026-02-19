---
title: "Implement prompt caching with a guide from the Anthropic Cookbook"
source_url: "https://github.com/anthropics/anthropic-cookbook/blob/main/misc/prompt_caching.ipynb"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Implement prompt caching with a guide from the Anthropic Cookbook

Prompt caching allows you to store and reuse context within your prompt. This makes it more practical to include additional information in your prompt -- such as detailed instructions and example responses -- which help improve every response Claude generates.

By fully leveraging prompt caching within your prompt, you can reduce latency by >2x and costs up to 90%. This can generate significant savings when building solutions that involve repetitive tasks around detailed book content.

This cookbook demonstrates how to use prompt caching in a single turn and across a multi-turn conversation.

## Setup

First, set up the environment with the necessary imports and initializations:

```python
%pip install anthropic bs4 --quiet
```

```python
import time
import anthropic
import requests
from bs4 import BeautifulSoup

client = anthropic.Anthropic()
MODEL_NAME = "claude-sonnet-4-6"
TIMESTAMP = int(time.time())
```

The cookbook fetches the text from Pride and Prejudice by Jane Austen (~187,000 tokens long) as the example content.

## Example 1: Single Turn

### Part 1: Non-cached API Call (Baseline)

Make a truly non-cached API call without the `cache_control` parameter. This establishes the baseline performance.

```python
def make_non_cached_api_call():
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": str(TIMESTAMP) + "<book>" + book_content + "</book>",
                },
                {"type": "text", "text": "What is the title of this book? Only output the title."},
            ],
        }
    ]
    start_time = time.time()
    response = client.messages.create(model=MODEL_NAME, max_tokens=300, messages=messages)
    end_time = time.time()
    return response, end_time - start_time
```

Result: Non-cached API call time ~6.86 seconds with 187,363 input tokens.

### Part 2: First Cached API Call (Cache Creation)

Enable prompt caching by adding `cache_control: {"type": "ephemeral"}` to the book content.

The first call with `cache_control` creates the cache entry. This initial call has similar timing to the non-cached call because it still needs to process all tokens, but it stores them in the cache for future use.

```python
def make_cached_api_call_create():
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": str(TIMESTAMP) + "<book>" + book_content + "</book>",
                    "cache_control": {"type": "ephemeral"},
                },
                {"type": "text", "text": "What is the title of this book? Only output the title."},
            ],
        }
    ]
    start_time = time.time()
    response = client.messages.create(model=MODEL_NAME, max_tokens=300, messages=messages)
    end_time = time.time()
    return response, end_time - start_time
```

Result: First cached API call ~5.96 seconds. Cache creation tokens: 187,347.

### Part 3: Second Cached API Call (Cache Hit)

The second call with the same `cache_control` parameter reads from the cache instead of processing all tokens again. This is where the real performance benefit shows.

Result: Second cached API call ~3.66 seconds. Speedup from caching: 1.9x faster.

### Summary of Example 1

1. **Non-cached call** - Without `cache_control`, Claude processes all ~187k tokens normally
2. **First cached call** - With `cache_control`, Claude processes all tokens AND stores them in cache (similar timing to non-cached)
3. **Second cached call** - With `cache_control`, Claude reads from the existing cache (2-10x faster)

The key insight: Prompt caching requires two calls to show benefits. The first call creates the cache entry, and subsequent calls read from the cache for dramatic speedups.

This is especially valuable for:
- Large documents or codebases that remain constant across multiple queries
- System prompts with detailed instructions
- Multi-turn conversations

## Example 2: Multi-turn Conversation with Incremental Caching

The cookbook demonstrates a `ConversationHistory` class that manages cache breakpoints as the conversation progresses. The last user turn gets `cache_control: {"type": "ephemeral"}` applied, enabling incremental caching.

```python
class ConversationHistory:
    def __init__(self):
        self.turns = []

    def add_turn_assistant(self, content):
        self.turns.append({"role": "assistant", "content": [{"type": "text", "text": content}]})

    def add_turn_user(self, content):
        self.turns.append({"role": "user", "content": [{"type": "text", "text": content}]})

    def get_turns(self):
        result = []
        user_turns_processed = 0
        for turn in reversed(self.turns):
            if turn["role"] == "user" and user_turns_processed < 1:
                result.append({
                    "role": "user",
                    "content": [{
                        "type": "text",
                        "text": turn["content"][0]["text"],
                        "cache_control": {"type": "ephemeral"},
                    }],
                })
                user_turns_processed += 1
            else:
                result.append(turn)
        return list(reversed(result))
```

The system message containing the book content also gets `cache_control: {"type": "ephemeral"}`.

### Multi-turn Results

- **Turn 1**: 0% cached, 5.79 seconds (creates cache)
- **Turn 2**: 100% cached, 8.29 seconds (reads from cache, longer due to output generation)
- **Turn 3**: 100% cached, 10.14 seconds
- **Turn 4**: 100% cached, 9.53 seconds

Nearly 100% of input tokens were cached in subsequent turns as cache breakpoints were adjusted, allowing the next user message to be read nearly instantly.
