---
title: "Web search tool"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Web search tool

The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. Claude automatically cites sources from search results as part of its answer.

The latest web search tool version (`web_search_20260209`) supports dynamic filtering with Claude Opus 4.6 and Sonnet 4.6. Claude can write and execute code to filter search results before they reach the context window, keeping only relevant information and discarding the rest. This leads to more accurate responses while reducing token consumption. The previous tool version (`web_search_20250305`) remains available without dynamic filtering.

This feature is Zero Data Retention (ZDR) eligible.

## Supported models

Web search is available on Claude Opus 4.6, Claude Opus 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Sonnet 4, Claude Sonnet 3.7 (deprecated), Claude Haiku 4.5, and Claude Haiku 3.5 (deprecated).

## How web search works

When you add the web search tool to your API request:
1. Claude decides when to search based on the prompt.
2. The API executes the searches and provides Claude with the results. This process may repeat multiple times throughout a single request.
3. At the end of its turn, Claude provides a final response with cited sources.

### Dynamic filtering with Opus 4.6 and Sonnet 4.6

With the `web_search_20260209` tool version, Claude can write and execute code to post-process query results. Instead of reasoning over full HTML files, Claude dynamically filters search results before loading them into context, keeping only what's relevant and discarding the rest.

Dynamic filtering is particularly effective for searching through technical documentation, literature review and citation verification, technical research, and response grounding and verification. It requires the code execution tool to be enabled.

## Tool definition

The web search tool supports the following parameters:
- `max_uses`: Limit the number of searches per request
- `allowed_domains`: Only include results from these domains
- `blocked_domains`: Never include results from these domains
- `user_location`: Localize search results (type, city, region, country, timezone)

### Domain filtering

- Domains should not include the HTTP/HTTPS scheme
- Subdomains are automatically included
- Subpaths are supported
- You can use either `allowed_domains` or `blocked_domains`, but not both
- Only one wildcard (`*`) is allowed per domain entry, in the path

### Response

Search results include: `url`, `title`, `page_age`, `encrypted_content`.

Citations are always enabled for web search, and each `web_search_result_location` includes: `url`, `title`, `encrypted_index`, `cited_text`.

### Errors

Possible error codes: `too_many_requests`, `invalid_input`, `max_uses_exceeded`, `query_too_long`, `unavailable`.

The response may include a `pause_turn` stop reason, indicating the API paused a long-running turn.

## Prompt caching

Web search works with prompt caching. Add at least one `cache_control` breakpoint in your request. The system will automatically cache up until the last `web_search_tool_result` block when executing the tool.

## Streaming

With streaming enabled, you'll receive search events as part of the stream, with a pause while the search executes.

## Batch requests

You can include the web search tool in the Messages Batches API at the same pricing as regular Messages API requests.

## Usage and pricing

Web search is available on the Claude API for $10 per 1,000 searches, plus standard token costs for search-generated content. Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.
