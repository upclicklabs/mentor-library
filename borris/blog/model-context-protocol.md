---
title: "Introducing the Model Context Protocol"
source_url: "https://www.anthropic.com/news/model-context-protocol"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Introducing the Model Context Protocol

Published: November 25, 2024

## Overview

Anthropic has open-sourced the Model Context Protocol (MCP), a new standard designed to connect AI assistants with data systems. This protocol aims to help advanced models produce better, more relevant responses by bridging the gap between AI systems and their information sources.

## The Problem MCP Addresses

Despite significant advances in AI capabilities, models remain isolated from critical data. Even the most sophisticated models are constrained by their isolation from data, trapped behind information silos and legacy systems. Each new data connection requires custom implementation, making scalable, connected systems difficult to achieve.

## How MCP Works

The protocol provides a universal, open standard for connecting AI systems with data sources. Developers can either expose data through MCP servers or build AI applications (MCP clients) that connect to these servers, using one unified protocol rather than maintaining separate integrations.

## Key Components

Three major components were introduced:

- The Model Context Protocol specification and SDKs (available on GitHub)
- Local MCP server support in Claude Desktop applications
- An open-source repository of pre-built MCP servers

Pre-built servers are available for popular enterprise platforms including Google Drive, Slack, GitHub, Git, Postgres, and Puppeteer.

## Early Adoption

Organizations like Block and Apollo have already integrated MCP. Development tool companies including Zed, Replit, Codeium, and Sourcegraph are collaborating to enhance their platforms, enabling AI agents to better retrieve contextual information for coding tasks.

## Getting Started

Developers can immediately begin building and testing MCP connectors. All Claude.ai plans support connecting MCP servers to the Claude Desktop app, while Claude for Work customers can test locally with internal systems.

To begin:
- Install pre-built servers through Claude Desktop
- Follow the quickstart guide
- Contribute to open-source connector repositories

## Community Vision

Anthropic emphasizes building MCP as a collaborative, open-source project and ecosystem, inviting developers, enterprises, and early adopters to participate in advancing context-aware AI systems.
