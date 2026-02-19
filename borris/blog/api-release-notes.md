---
title: "API Release Notes"
source_url: "https://docs.anthropic.com/en/release-notes/api"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# API Release Notes

Updates to the Claude Developer Platform, including the Claude API, client SDKs, and the Claude Console.

For release notes on Claude Apps, see the Release notes for Claude Apps in the Claude Help Center. For updates to Claude Code, see the complete CHANGELOG.md in the claude-code repository.

## February 19, 2026

- Launched automatic caching for the Messages API. Add a single cache_control field to your request body and the system automatically caches the last cacheable block, moving the cache point forward as conversations grow. No manual breakpoint management required. Works alongside existing block-level cache control for fine-grained optimization. Available on the Claude API and Azure AI Foundry (preview).
- Retired the Claude Sonnet 3.7 model (claude-3-7-sonnet-20250219) and the Claude Haiku 3.5 model (claude-3-5-haiku-20241022). All requests to these models will now return an error. Recommended upgrades: Claude Sonnet 4.6 and Claude Haiku 4.5 respectively.
- Announced the deprecation of the Claude Haiku 3 model (claude-3-haiku-20240307), with retirement scheduled for April 19, 2026.

## February 17, 2026

- Launched Claude Sonnet 4.6, the latest balanced model combining speed and intelligence for everyday tasks. Sonnet 4.6 delivers improved agentic search performance while consuming fewer tokens. Supports extended thinking and a 1M token context window (beta).
- API code execution is now free when used with web search or web fetch.
- The web search tool and programmatic tool calling are now generally available (no beta header required). Web search and web fetch now support dynamic filtering.
- The code execution tool, web fetch tool, tool search tool, tool use examples, and memory tool are now generally available (no beta header required).

## February 7, 2026

- Launched fast mode in research preview for Opus 4.6, providing significantly faster output token generation via the speed parameter. Fast mode is up to 2.5x as fast at premium pricing.

## February 5, 2026

- Launched Claude Opus 4.6, the most intelligent model for complex agentic tasks and long-horizon work. Opus 4.6 recommends adaptive thinking; manual thinking with budget_tokens is deprecated. Opus 4.6 does not support prefilling assistant messages.
- The effort parameter is now generally available and supports Claude Opus 4.6. Effort replaces budget_tokens for controlling thinking depth on new models.
- Launched the compaction API in beta, providing server-side context summarization for effectively infinite conversations. Available on Opus 4.6.
- Introduced data residency controls, allowing you to specify where model inference runs with the inference_geo parameter. US-only inference is available at 1.1x pricing for models released after February 1, 2026.
- The 1M token context window is now available in beta for Claude Opus 4.6.
- Fine-grained tool streaming is now generally available on all models and platforms.

## January 29, 2026

- Structured outputs are now generally available on the Claude API for Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5. GA includes expanded schema support, improved grammar compilation latency, and a simplified integration path.

## January 12, 2026

- console.anthropic.com now redirects to platform.claude.com.

## January 5, 2026

- Retired the Claude Opus 3 model (claude-3-opus-20240229). Recommended upgrade: Claude Opus 4.5.

## December 19, 2025

- Announced the deprecation of the Claude Haiku 3.5 model.

## December 4, 2025

- Structured outputs now supports Claude Haiku 4.5.

## November 24, 2025

- Launched Claude Opus 4.5, the most intelligent model combining maximum capability with practical performance.
- Launched programmatic tool calling in public beta.
- Launched the tool search tool in public beta.
- Launched the effort parameter in public beta for Claude Opus 4.5.
- Added client-side compaction to Python and TypeScript SDKs.

## November 21, 2025

- Search result content blocks are now generally available on Amazon Bedrock.

## November 19, 2025

- Launched a new documentation platform at platform.claude.com/docs.

## November 18, 2025

- Launched Claude in Microsoft Foundry, bringing Claude models to Azure customers with Azure billing and OAuth authentication.

## November 14, 2025

- Launched structured outputs in public beta, providing guaranteed schema conformance for Claude's responses.

## October 28, 2025

- Announced the deprecation of the Claude Sonnet 3.7 model.
- Retired the Claude Sonnet 3.5 models.
- Expanded context editing with thinking block clearing.

## October 16, 2025

- Launched Agent Skills (skills-2025-10-02 beta), a new way to extend Claude's capabilities. Skills are organized folders of instructions, scripts, and resources that Claude loads dynamically.

## October 15, 2025

- Launched Claude Haiku 4.5, the fastest and most intelligent Haiku model with near-frontier performance.

## September 29, 2025

- Launched Claude Sonnet 4.5, the best model for complex agents and coding.
- Introduced global endpoint pricing for AWS Bedrock and Google Vertex AI.
- Introduced a new stop reason model_context_window_exceeded.
- Launched the memory tool in beta.
- Launched context editing in beta.

## September 17, 2025

- Launched tool helpers in beta for the Python and TypeScript SDKs.

## September 16, 2025

- Unified developer offerings under the Claude brand with updated naming and URLs.

## September 10, 2025

- Launched the web fetch tool in beta.
- Launched the Claude Code Analytics API.

## September 8, 2025

- Launched a beta version of the C# SDK.

## September 5, 2025

- Launched rate limit charts in the Console Usage page.

## September 3, 2025

- Launched support for citable documents in client-side tool results.

## September 2, 2025

- Launched v2 of the Code Execution Tool in public beta, replacing the original Python-only tool with Bash command execution.

## August 27, 2025

- Launched a beta version of the PHP SDK.

## August 26, 2025

- Increased rate limits on the 1M token context window for Claude Sonnet 4 on the Claude API.
- The 1M token context window is now available on Google Cloud's Vertex AI.

## August 19, 2025

- Request IDs are now included directly in error response bodies.

## August 18, 2025

- Released the Usage & Cost API.
- Added a new endpoint to the Admin API for retrieving organization information.

## August 13, 2025

- Announced the deprecation of the Claude Sonnet 3.5 models.
- The 1-hour cache duration for prompt caching is now generally available.

## August 12, 2025

- Launched beta support for a 1M token context window in Claude Sonnet 4 on the Claude API and Amazon Bedrock.

## August 8, 2025

- Search result content blocks are now generally available on the Claude API and Google Cloud's Vertex AI.

## August 5, 2025

- Launched Claude Opus 4.1, an incremental update to Claude Opus 4.

## July 28, 2025

- Released text_editor_20250728, an updated text editor tool.

## July 24, 2025

- Increased rate limits for Claude Opus 4 on the Claude API.

## July 21, 2025

- Retired the Claude 2.0, Claude 2.1, and Claude Sonnet 3 models.

## July 17, 2025

- Increased rate limits for Claude Sonnet 4 on the Claude API.

## July 3, 2025

- Launched search result content blocks in beta, enabling natural citations for RAG applications.

## June 30, 2025

- Announced the deprecation of the Claude Opus 3 model.

## June 23, 2025

- Console users with the Developer role can now access the Cost page.

## June 11, 2025

- Launched fine-grained tool streaming in public beta.

## May 22, 2025

- Launched Claude Opus 4 and Claude Sonnet 4, latest models with extended thinking capabilities.
- Default behavior of extended thinking returns a summary with full thinking encrypted in the signature field.
- Launched interleaved thinking in public beta.
- Launched the Files API in public beta.
- Launched the Code execution tool in public beta.
- Launched the MCP connector in public beta.
- Changed the default value for the top_p parameter from 0.999 to 0.99 for all models.
- Moved Go SDK from beta to GA.

## May 21, 2025

- Moved Ruby SDK from beta to GA.

## May 7, 2025

- Launched a web search tool in the API.

## May 1, 2025

- Cache control must now be specified directly in the parent content block of tool_result and document.source.

## April 9, 2025

- Launched a beta version of the Ruby SDK.

## March 31, 2025

- Moved Java SDK from beta to GA.
- Moved Go SDK from alpha to beta.

## February 27, 2025

- Added URL source blocks for images and PDFs in the Messages API.
- Added support for a none option to the tool_choice parameter.
- Launched an OpenAI-compatible API endpoint.

## February 24, 2025

- Launched Claude Sonnet 3.7 with extended thinking step-by-step capability.
- Added vision support to Claude Haiku 3.5.
- Released a token-efficient tool use implementation.
- Released updated tool versions decoupling text edit and bash tools from computer use.

## February 10, 2025

- Added the anthropic-organization-id response header to all API responses.

## January 31, 2025

- Moved Java SDK from alpha to beta.

## January 23, 2025

- Launched citations capability in the API.
- Added support for plain text and custom content documents.

## January 21, 2025

- Announced the deprecation of the Claude 2, Claude 2.1, and Claude Sonnet 3 models.

## January 15, 2025

- Updated prompt caching to be easier to use with automatic longest prefix matching.

## January 10, 2025

- Optimized support for prompt caching in the Message Batches API.

## December 19, 2024

- Added support for a delete endpoint in the Message Batches API.

## December 17, 2024

- Models API, Message Batches API, Token counting API, Prompt Caching, and PDF support are now generally available.
- Released new official Java SDK (alpha) and Go SDK (alpha).

## December 4, 2024

- Added the ability to group by API key to the Usage and Cost pages.
- Added Last used at and Cost columns to the API keys page.

## November 21, 2024

- Released the Admin API.

## November 20, 2024

- Updated rate limits with new input and output tokens per minute rate limits.
- Added support for tool use in the Workbench.

## November 13, 2024

- Added PDF support for all Claude Sonnet 3.5 models.

## November 6, 2024

- Retired the Claude 1 and Instant models.

## November 4, 2024

- Claude Haiku 3.5 is now available on the Claude API as a text-only model.

## November 1, 2024

- Added PDF support for the new Claude Sonnet 3.5.
- Added token counting for Messages.

## October 22, 2024

- Added computer use tools to the API.
- Claude Sonnet 3.5 upgraded and available on the Claude API.

## October 8, 2024

- Message Batches API is now available in beta (50% less cost).
- Loosened restrictions on user/assistant turn ordering.
- Deprecated Build and Scale plans.

## October 3, 2024

- Added the ability to disable parallel tool use in the API.

## September 10, 2024

- Added Workspaces to the Developer Console.

## September 4, 2024

- Announced the deprecation of the Claude 1 models.

## August 22, 2024

- Added support for usage of the SDK in browsers by returning CORS headers.

## August 19, 2024

- Moved 8,192 token outputs from beta to general availability for Claude Sonnet 3.5.

## August 14, 2024

- Prompt caching is now available as a beta feature.

## July 15, 2024

- Generate outputs up to 8,192 tokens in length from Claude Sonnet 3.5 with a new beta header.

## July 9, 2024

- Automatically generate test cases for prompts in the Developer Console.
- Compare outputs from different prompts side by side.

## June 27, 2024

- View API usage and billing in new Usage and Cost tabs.
- View current API rate limits in new Rate Limits tab.

## June 20, 2024

- Claude Sonnet 3.5, the most intelligent model at the time, is now generally available.

## May 30, 2024

- Tool use is now generally available across the Claude API, Amazon Bedrock, and Google Vertex AI.

## May 10, 2024

- Prompt Generator tool is now available in the Developer Console.
