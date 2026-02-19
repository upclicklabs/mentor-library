---
title: "Messages API"
source_url: "https://docs.anthropic.com/en/api/messages"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Messages API

## Overview

Endpoint: POST /v1/messages

The Messages API allows you to send structured lists of input messages with text and/or image content, and the model will generate the next message in the conversation. It supports both single queries and stateless multi-turn conversations.

## Core Parameters

### Required Parameters

#### max_tokens (number)
The maximum number of tokens to generate before stopping. Different models have different maximum values.

#### messages (array of MessageParam)
Input messages for the conversation. Claude models are trained to operate on alternating user and assistant conversational turns.

Message Structure:
- Each message must be an object with a role and content
- role: Either "user" or "assistant"
- content: Either a string or array of content blocks

#### model (Model)
The model that will complete your prompt. Available models include:

Premium Models:
- claude-opus-4-6: Most intelligent model for agents and coding
- claude-opus-4-5: Premium intelligence with practical performance

High-Performance Models:
- claude-sonnet-4-6: Frontier intelligence for coding, agents, and enterprise workflows
- claude-sonnet-4-5: Best model for real-world agents and coding

Fast Models:
- claude-3-5-haiku-20241022: Fastest and most compact model
- claude-haiku-4-5: Hybrid model with instant responses and extended thinking

### Optional Parameters

#### system (string or array of TextBlockParam)
System prompt providing context and instructions to Claude. Use the top-level system parameter rather than a "system" role in messages.

#### temperature (number)
Amount of randomness. Defaults to 1.0, ranges from 0.0 to 1.0. Closer to 0.0 for analytical tasks, closer to 1.0 for creative tasks.

#### stop_sequences (array of string)
Custom text sequences that cause the model to stop generating.

#### stream (boolean)
Whether to incrementally stream the response using server-sent events.

#### top_p (number)
Nucleus sampling. Either alter temperature or top_p, but not both.

#### top_k (number)
Only sample from the top K options for each subsequent token.

#### cache_control (optional CacheControlEphemeral)
Top-level cache control with type "ephemeral" and TTL of "5m" or "1h".

#### thinking (ThinkingConfigParam)
Configuration for enabling Claude's extended thinking:
- ThinkingConfigEnabled: {"type": "enabled", "budget_tokens": number}
- ThinkingConfigDisabled: {"type": "disabled"}
- ThinkingConfigAdaptive: {"type": "adaptive"}

#### tools (array of ToolUnion)
Definitions of tools that the model may use. Includes client tools and server tools.

Available Server Tools: web_search, web_fetch, code_execution, bash_code_execution, text_editor_code_execution, tool_search_tool_regex, tool_search_tool_bm25

#### tool_choice (ToolChoice)
Options: auto, any, tool (specific), none. Add disable_parallel_tool_use: true to output at most one tool use.

#### metadata (Metadata)
Object describing request metadata including user_id.

#### output_config (OutputConfig)
Configuration for model output format including json_schema and effort levels (low/medium/high/max).

#### service_tier (string)
"auto" for priority capacity if available, "standard_only" for standard capacity only.

## Content Block Types

### TextBlockParam
Text content with optional cache control and citations.

### ImageBlockParam
Supports base64 and URL image sources. Media types: image/jpeg, image/png, image/gif, image/webp.

### DocumentBlockParam
Supports PDF and text documents via base64, URL, or content blocks.

### ToolUseBlockParam
Tool use with id, name, and input parameters.

### ToolResultBlockParam
Tool results with tool_use_id, content, and optional is_error flag.

## Response Format

```json
{
  "id": "msg_1234567890",
  "content": [{"type": "text", "text": "Response text...", "citations": []}],
  "model": "claude-opus-4-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 100,
    "output_tokens": 50,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  }
}
```

## Key Constraints

- Maximum of 100,000 messages in a single request
- Models may stop before reaching the specified max_tokens
- Consecutive user or assistant turns are combined into single turns
- If final message uses assistant role, response content continues from that message
