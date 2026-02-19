---
title: "Tool Use GA"
source_url: "https://www.anthropic.com/news/tool-use-ga"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Tool Use GA

Tool use is now generally available across Claude 3 models on the Anthropic Messages API, Amazon Bedrock, and Google Cloud's Vertex AI. This capability enables Claude to interact with external tools and APIs for dynamic, accurate responses.

## Key Capabilities

The feature supports several use cases:

- **Data extraction**: Pulling structured information like names and dates from unstructured documents to minimize manual entry
- **API integration**: Converting natural language requests into structured API calls for self-service actions
- **Information retrieval**: Searching databases and web APIs to provide accurate customer support responses
- **Task automation**: Reducing errors through software API integration for data entry and file management
- **Multi-agent orchestration**: Using fast Claude subagents to solve granular tasks like scheduling optimization

## Developer Improvements

New features enhance the developer experience:

- **Streaming support**: Real-time responses in applications like customer support chatbots enable smoother interactions
- **Forced tool use**: Developers can specify which tools Claude should use or allow Claude to decide
- **Image compatibility**: Claude incorporates image inputs in applications

Opus now includes reasoning tags to clarify Claude's decision-making process. Note: The Claude 3 family currently doesn't support parallel tool calls.

## Customer Examples

**StudyFetch** integrated tools into their AI tutor Spark.E, observing a 42% increase in positive human feedback after implementation.

**Intuned** uses Claude 3 Haiku for data extraction, praising the quality, speed, and price combination.

**Hebbia** leverages Haiku for metadata extraction and real-time suggestions across complex workflows.
