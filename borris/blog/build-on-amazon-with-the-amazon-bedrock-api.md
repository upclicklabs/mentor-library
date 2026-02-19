---
title: "Build on Amazon with the Amazon Bedrock API"
source_url: "https://docs.anthropic.com/en/api/claude-on-amazon-bedrock"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Build on Amazon with the Amazon Bedrock API

Anthropic's Claude models are generally available through Amazon Bedrock. This guide walks through completing an API call to Claude on Bedrock.

## Install and configure the AWS CLI

1. Install AWS CLI version 2.13.23 or newer
2. Configure your AWS credentials using `aws configure`
3. Verify credentials: `aws sts get-caller-identity`

## Install an SDK for accessing Bedrock

Anthropic's client SDKs support Bedrock. You can also use `boto3` directly.

```bash
# Python
pip install -U "anthropic[bedrock]"

# TypeScript
npm install @anthropic-ai/bedrock-sdk

# Go
go get github.com/anthropics/anthropic-sdk-go/bedrock
```

## Accessing Bedrock

### Subscribe to Anthropic models

Go to AWS Console > Bedrock > Model Access and request access. Availability varies by region.

### API model IDs

| Model | Base Bedrock model ID |
|---|---|
| Claude Opus 4.6 | anthropic.claude-opus-4-6-v1 |
| Claude Sonnet 4.6 | anthropic.claude-sonnet-4-6 |
| Claude Sonnet 4.5 | anthropic.claude-sonnet-4-5-20250929-v1:0 |
| Claude Sonnet 4 | anthropic.claude-sonnet-4-20250514-v1:0 |
| Claude Opus 4.5 | anthropic.claude-opus-4-5-20251101-v1:0 |
| Claude Haiku 4.5 | anthropic.claude-haiku-4-5-20251001-v1:0 |

### Making requests

```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    aws_access_key="<access key>",
    aws_secret_key="<secret key>",
    aws_region="us-west-2",
)

message = client.messages.create(
    model="global.anthropic.claude-opus-4-6-v1",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
print(message.content)
```

### Bearer token authentication

Supported in C#, Go, and Java SDKs. Set the `AWS_BEARER_TOKEN_BEDROCK` environment variable or provide a token programmatically.

## Activity logging

Bedrock provides an invocation logging service for logging prompts and completions. Anthropic recommends logging activity on at least a 30-day rolling basis.

## Feature support

### PDF Support on Bedrock

PDF support is available through both the Converse API and InvokeModel API. Visual PDF analysis requires citations to be enabled with the Converse API.

### 1M token context window

Claude Opus 4.6, Sonnet 4.5, and Sonnet 4 support the 1M token context window on Bedrock. Include the `context-1m-2025-08-07` beta header.

## Global vs regional endpoints

Starting with Claude Sonnet 4.5 and future models:

- **Global endpoints**: Dynamic routing for maximum availability, no pricing premium
- **Regional endpoints**: Guaranteed data routing through specific geographic regions, 10% pricing premium

Use global endpoints by prefixing model IDs with `global.` (e.g., `global.anthropic.claude-opus-4-6-v1`). Use regional endpoints by removing the `global.` prefix.
