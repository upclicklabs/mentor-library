---
title: "Explore Anthropic's tool use documentation"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Explore Anthropic's tool use documentation

Claude is capable of interacting with tools and functions, allowing you to extend Claude's capabilities to perform a wider variety of tasks.

## How tool use works

Claude supports two types of tools:

1. **Client tools**: Tools that execute on your systems, including:
   - User-defined custom tools you create and implement
   - Anthropic-defined tools like computer use and text editor that require client implementation

2. **Server tools**: Tools that execute on Anthropic's servers, like web search and web fetch. These must be specified in the API request but don't require implementation on your part.

### Client tools workflow

1. **Provide Claude with tools and a user prompt**: Define tools with names, descriptions, and input schemas
2. **Claude decides to use a tool**: Claude assesses if any tools can help, constructs a tool use request. Response has `stop_reason` of `tool_use`
3. **Execute the tool and return results**: Extract tool name and input, execute on your system, return results in a `tool_result` content block
4. **Claude uses tool result to formulate a response**: Claude analyzes results to craft its final response

### Server tools workflow

1. **Provide Claude with tools and a user prompt**: Server tools like web search and web fetch have their own parameters
2. **Claude executes the server tool**: Results are automatically incorporated
3. **Claude uses results to formulate a response**: No additional user interaction needed

Note: When the server-side sampling loop reaches its 10-iteration limit, the API returns `stop_reason="pause_turn"`. Continue the conversation by sending the response back.

## Using MCP tools with Claude

When building an MCP client, convert MCP tool definitions by renaming `inputSchema` to `input_schema`:

```python
async def get_claude_tools(mcp_session):
    mcp_tools = await mcp_session.list_tools()
    claude_tools = []
    for tool in mcp_tools.tools:
        claude_tools.append({
            "name": tool.name,
            "description": tool.description or "",
            "input_schema": tool.inputSchema,
        })
    return claude_tools
```

## Tool use patterns

### Single tool

Define a tool with name, description, and input_schema. Claude returns a `tool_use` block with the tool name and input. Execute the tool and return results in a `tool_result` block.

### Parallel tool use

Claude can call multiple tools in parallel within a single response. All `tool_use` blocks are in a single assistant message, and all corresponding `tool_result` blocks must be provided in the subsequent user message.

### Multiple tools

Provide Claude with multiple tools to choose from. Claude may use them sequentially or in parallel depending on the task.

### Sequential tools

Some tasks require calling multiple tools in sequence, using the output of one as input to another. Claude will call one tool at a time in this case.

### Missing information

If the user's prompt doesn't include enough information for required parameters:
- Claude Opus is more likely to ask for clarification
- Claude Sonnet may attempt to infer reasonable values

### Chain of thought tool use

For Sonnet or Haiku, use a prompt instructing Claude to analyze before making tool calls: assess which tool is relevant, check if required parameters are present, and only invoke if all requirements are met.

## Structured Outputs

Add `strict: true` to tool definitions to ensure Claude's tool calls always match your schema exactly, eliminating type mismatches or missing fields.

## Pricing

Tool use requests are priced based on:
1. Total input tokens sent (including the `tools` parameter)
2. Output tokens generated
3. For server-side tools, additional usage-based pricing

Tool use system prompt token counts vary by model and tool choice (auto/none: 346 tokens, any/tool: 313 tokens for Claude 4.x models).
