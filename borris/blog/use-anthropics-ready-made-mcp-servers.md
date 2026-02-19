---
title: "Use Anthropic's ready-made MCP servers"
source_url: "https://github.com/modelcontextprotocol/servers"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use Anthropic's ready-made MCP servers

## Overview

This repository contains reference implementations for the Model Context Protocol (MCP), along with references to community-built servers and additional resources. The servers showcase how MCP can provide LLMs with secure, controlled access to tools and data sources.

## Important Notice

The MCP Registry at registry.modelcontextprotocol.io contains the comprehensive list of published servers. This repository focuses on housing reference server implementations maintained by the MCP steering group.

## Available SDK Languages

MCP servers are typically implemented using official SDKs in multiple languages:
- C#
- Go
- Java
- Kotlin
- PHP
- Python
- Ruby
- Rust
- Swift
- TypeScript

## Reference Servers

Reference servers demonstrate MCP features and SDK usage:

- **Everything** - Test server with prompts, resources, and tools
- **Fetch** - Web content fetching and conversion for LLM usage
- **Filesystem** - Secure file operations with access controls
- **Git** - Git repository reading, searching, and manipulation
- **Memory** - Knowledge graph-based persistent memory
- **Sequential Thinking** - Dynamic problem-solving through thought sequences
- **Time** - Time and timezone conversion capabilities

## Archived Servers

Archived reference servers located at modelcontextprotocol/servers-archived include:
- AWS KB Retrieval
- Brave Search (replaced by official server)
- EverArt
- GitHub
- GitLab
- Google Drive
- Google Maps
- PostgreSQL
- Puppeteer
- Redis
- Sentry
- Slack
- SQLite

## Third-Party Integrations

Official integrations are maintained by companies building production-ready MCP servers. The ecosystem includes integrations with platforms like Atlassian, Auth0, AWS, Azure, and many others across various industries and use cases.
