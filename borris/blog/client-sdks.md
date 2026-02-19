---
title: "Client SDKs"
source_url: "https://docs.anthropic.com/en/api/client-sdks"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Client SDKs

Official SDKs for building with the Claude API in Python, TypeScript, Java, Go, Ruby, C#, and PHP.

Anthropic provides official client SDKs in multiple languages to make it easier to work with the Claude API. Each SDK provides idiomatic interfaces, type safety, and built-in support for features like streaming, retries, and error handling.

## Quick installation

- Python: `pip install anthropic`
- TypeScript: `npm install @anthropic-ai/sdk`
- Java (Gradle): `implementation("com.anthropic:anthropic-java:2.11.1")`
- Go: `go get github.com/anthropics/anthropic-sdk-go`
- Ruby: `bundler add anthropic`
- C#: `dotnet add package Anthropic`
- PHP: `composer require anthropic-ai/sdk`

## Quick start

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content)
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const message = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Hello, Claude" }
  ]
});
console.log(message.content);
```

## Platform support

| Platform | Description |
|----------|-------------|
| Claude API | Connect directly to Claude API endpoints |
| Amazon Bedrock | Use Claude through AWS |
| Google Vertex AI | Use Claude through Google Cloud |
| Microsoft Foundry | Use Claude through Microsoft Azure |

## Beta features

Access beta features using the beta namespace in any SDK:

```python
message = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["feature-name"],
)
```

## Requirements

| SDK | Minimum Version |
|-----|-----------------|
| Python | 3.9+ |
| TypeScript | 4.9+ (Node.js 20+) |
| Java | 8+ |
| Go | 1.22+ |
| Ruby | 3.2.0+ |
| C# | .NET Standard 2.0 |
| PHP | 8.1.0+ |

## GitHub repositories

- anthropic-sdk-python
- anthropic-sdk-typescript
- anthropic-sdk-java
- anthropic-sdk-go
- anthropic-sdk-ruby
- anthropic-sdk-csharp
- anthropic-sdk-php
