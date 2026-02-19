---
title: "Code execution tool"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Code execution tool

Claude can analyze data, create visualizations, perform complex calculations, run system commands, create and edit files, and process uploaded files directly within the API conversation. The code execution tool allows Claude to run Bash commands and manipulate files in a secure, sandboxed environment.

Code execution is free when used with web search or web fetch. When `web_search_20260209` or `web_fetch_20260209` is included in your request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.

Code execution is a core primitive for building high-performance agents. It enables dynamic filtering in web search and web fetch tools, allowing Claude to process results before they reach the context window.

This feature is not covered by Zero Data Retention (ZDR) arrangements.

## Model compatibility

The code execution tool (`code_execution_20250825`) is available on Claude Opus 4.6, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Opus 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4, Claude Sonnet 3.7 (deprecated), Claude Haiku 4.5, and Claude Haiku 3.5 (deprecated).

## Platform availability

Code execution is available on Claude API (Anthropic) and Microsoft Azure AI Foundry. It is not currently available on Amazon Bedrock or Google Vertex AI.

## How code execution works

When you add the code execution tool to your API request:
1. Claude evaluates whether code execution would help answer your question
2. The tool automatically provides Bash commands and file operations capabilities
3. Claude can use any combination of these capabilities in a single request
4. All operations run in a secure sandbox environment
5. Claude provides results with any generated charts, calculations, or analysis

## Key capabilities

- Execute Bash commands for system operations and package management
- Create, view, and edit files directly, including writing code
- Upload and analyze files (CSV, Excel, JSON, XML, images, text files) via the Files API
- Retrieve generated files using the Files API

## Containers

The code execution tool runs in a secure, containerized environment:
- Python version 3.11.12
- Linux-based container, x86_64 (AMD64)
- 5GiB RAM, 5GiB workspace storage, 1 CPU
- No internet access (completely disabled for security)
- Pre-installed libraries: pandas, numpy, scipy, scikit-learn, matplotlib, seaborn, and many more

You can reuse containers across multiple API requests by providing the container ID from a previous response. Containers expire 30 days after creation.

## Tool definition

```json
{
  "type": "code_execution_20250825",
  "name": "code_execution"
}
```

When provided, Claude automatically gains access to `bash_code_execution` and `text_editor_code_execution` sub-tools.

## Usage and pricing

When used without web search/fetch tools, code execution is billed by execution time:
- Execution time has a minimum of 5 minutes
- Each organization receives 1,550 free hours per month
- Additional usage: $0.05 per hour, per container

## Programmatic tool calling

The code execution tool powers programmatic tool calling, which allows Claude to write code that calls your custom tools programmatically within the execution container.

## Using code execution with Agent Skills

The code execution tool enables Claude to use Agent Skills -- modular capabilities consisting of instructions, scripts, and resources that extend Claude's functionality.
