---
title: "Client SDKs Reference"
source_url: "https://docs.anthropic.com/en/api/client-sdks"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Client SDKs Reference

Official SDKs for building with the Claude API. Anthropic provides official client SDKs in multiple languages with idiomatic interfaces, type safety, and built-in support for features like streaming, retries, and error handling.

This page covers the following SDK sections:
- [Python SDK](https://docs.anthropic.com/en/api/client-sdks#python)
- [TypeScript SDK](https://docs.anthropic.com/en/api/client-sdks#typescript)
- [Java SDK](https://docs.anthropic.com/en/api/client-sdks#java)
- [Go SDK](https://docs.anthropic.com/en/api/client-sdks#go)
- [Ruby SDK](https://docs.anthropic.com/en/api/client-sdks#ruby)

## Quick Installation

### Python
```bash
pip install anthropic
```
- Sync and async clients, Pydantic models
- Minimum version: Python 3.9+
- GitHub: [anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python)

### TypeScript
```bash
npm install @anthropic-ai/sdk
```
- Node.js, Deno, Bun, and browser support
- Minimum version: TypeScript 4.9+ (Node.js 20+)
- GitHub: [anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript)

### Java

Gradle:
```groovy
implementation("com.anthropic:anthropic-java:2.11.1")
```

Maven:
```xml
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java</artifactId>
    <version>2.11.1</version>
</dependency>
```
- Builder pattern, CompletableFuture async
- Minimum version: Java 8+
- GitHub: [anthropic-sdk-java](https://github.com/anthropics/anthropic-sdk-java)

### Go
```bash
go get github.com/anthropics/anthropic-sdk-go
```
- Context-based cancellation, functional options
- Minimum version: Go 1.22+
- GitHub: [anthropic-sdk-go](https://github.com/anthropics/anthropic-sdk-go)

### Ruby
```bash
bundler add anthropic
```
- Sorbet types, streaming helpers
- Minimum version: Ruby 3.2.0+
- GitHub: [anthropic-sdk-ruby](https://github.com/anthropics/anthropic-sdk-ruby)

## Additional SDKs

Anthropic also provides official SDKs for:

### C#
```bash
dotnet add package Anthropic
```
- .NET Standard 2.0+, IChatClient integration
- GitHub: [anthropic-sdk-csharp](https://github.com/anthropics/anthropic-sdk-csharp)

### PHP
```bash
composer require anthropic-ai/sdk
```
- Value objects, builder pattern
- Minimum version: PHP 8.1.0+
- GitHub: [anthropic-sdk-php](https://github.com/anthropics/anthropic-sdk-php)

## Platform Support

All SDKs support multiple deployment options:

| Platform | Description |
|----------|-------------|
| Claude API | Connect directly to Claude API endpoints |
| Amazon Bedrock | Use Claude through AWS |
| Google Vertex AI | Use Claude through Google Cloud |
| Microsoft Foundry | Use Claude through Microsoft Azure |

## Beta Features

Access beta features using the `beta` namespace in any SDK. See the source documentation for language-specific examples.
