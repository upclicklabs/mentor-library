---
title: "MCP Development Roadmap"
source_url: "https://modelcontextprotocol.io/development/roadmap"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# MCP Development Roadmap

Our plans for evolving Model Context Protocol.

Last updated: 2025-10-31

The Model Context Protocol is rapidly evolving. This page outlines priorities for the next release on November 25th, 2025, with a release candidate available on November 11th, 2025. To see what's changing in the upcoming release, check out the specification changelog.

The ideas presented here are not commitments -- they may be solved differently than described, or some may not materialize at all. This is also not an exhaustive list.

## Priority Areas for the Next Release

### Asynchronous Operations

Currently, MCP is built around mostly synchronous operations. Async support is being added to allow servers to kick off long-running tasks while clients can check back later for results. This will enable operations that take minutes or hours without blocking.

Follow the progress in SEP-1686.

### Statelessness and Scalability

As organizations deploy MCP servers at enterprise scale, challenges around horizontal scaling are being addressed. While Streamable HTTP provides some stateless support, rough edges around server startup and session handling are being smoothed out to make it easier to run MCP servers in production.

The current focus point for this effort is SEP-1442.

### Server Identity

Servers will be able to advertise themselves through .well-known URLs -- an established standard for providing metadata. This will allow clients to discover what a server can do without having to connect to it first, making discovery much more intuitive and enabling systems like the registry to automatically catalog capabilities. Work is being done across multiple projects in the industry to rely on a common standard on agent cards.

### Official Extensions

As MCP has grown, valuable patterns have emerged for specific industries and use cases. Rather than leaving everyone to reinvent the wheel, the most popular protocol extensions are being officially recognized and documented. This curated collection will give developers building for specialized domains like healthcare, finance, or education a solid starting point.

### SDK Support Standardization

A clear tiering system for SDKs is being introduced based on factors like specification compliance speed, maintenance responsiveness, and feature completeness. This will help developers understand exactly what level of support they're getting before committing to a dependency.

### MCP Registry General Availability

The MCP Registry launched in preview in September 2025 and is progressing toward general availability. The v0.1 API is being stabilized through real-world integrations and community feedback, with plans to transition from preview to a production-ready service.

## Validation

To foster a robust developer ecosystem, plans include:

- **Reference Client Implementations**: demonstrating protocol features with high-quality AI applications
- **Reference Server Implementation**: showcasing authentication patterns and remote deployment best practices
- **Compliance Test Suites**: automated verification that clients, servers, and SDKs properly implement the specification

## Get Involved

Community contributions to MCP's future are welcomed. Join the GitHub Discussions to share ideas, provide feedback, or participate in the development process.
