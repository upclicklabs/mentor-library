---
title: "Use Skills in the API"
source_url: "https://docs.claude.com/en/api/skills-guide"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use Skills in the API

Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows how to use both pre-built and custom Skills with the Claude API.

This feature is in beta and is not covered by Zero Data Retention (ZDR) arrangements.

## Overview

Skills integrate with the Messages API through the code execution tool. Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical: both require code execution and use the same container structure.

### Skill Sources Comparison

| Aspect | Anthropic Skills | Custom Skills |
|--------|------------------|---------------|
| Type value | anthropic | custom |
| Skill IDs | Short names: pptx, xlsx, docx, pdf | Generated: skill_01AbCdEfGhIjKlMnOpQrStUv |
| Version format | Date-based: 20251013 or latest | Epoch timestamp: 1759178010641129 or latest |
| Management | Pre-built and maintained by Anthropic | Upload and manage via Skills API |
| Availability | Available to all users | Private to your workspace |

### Prerequisites

1. Claude API key from the Console
2. Beta headers: code-execution-2025-08-25, skills-2025-10-02, files-api-2025-04-14
3. Code execution tool enabled in requests

## Using Skills in Messages

### Container Parameter

Skills are specified using the container parameter in the Messages API. You can include up to 8 Skills per request. Specify the required type and skill_id, and optionally include version to pin to a specific version.

### Downloading Generated Files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return file_id attributes in the response. Use the Files API to download these files:

1. Skills create files during code execution
2. Response includes file_id for each created file
3. Use Files API to download the actual file content
4. Save locally or process as needed

### Multi-Turn Conversations

Reuse the same container across multiple messages by specifying the container ID from the first response.

### Long-Running Operations

Skills may perform operations that require multiple turns. Handle pause_turn stop reasons by providing the response back in a subsequent request to let Claude continue its turn.

### Using Multiple Skills

Combine multiple Skills in a single request to handle complex workflows (e.g., data analysis with Excel + presentation creation with PowerPoint).

## Managing Custom Skills

### Creating a Skill

Requirements:
- Must include a SKILL.md file at the top level
- All files must specify a common root directory in their paths
- Total upload size must be under 8MB
- YAML frontmatter: name (max 64 chars, lowercase letters/numbers/hyphens), description (max 1024 chars)

### Versioning

- Anthropic-Managed Skills: Date format versions (20251013), use "latest" for most recent
- Custom Skills: Auto-generated epoch timestamps, create new versions when updating

### How Skills Are Loaded

1. Metadata Discovery: Claude sees metadata for each Skill in the system prompt
2. File Loading: Skill files are copied into the container at /skills/{directory}/
3. Automatic Use: Claude automatically loads and uses Skills when relevant
4. Composition: Multiple Skills compose together for complex workflows

## Use Cases

### Organizational Skills
- Brand & Communications: Company-specific formatting, templates, brand guidelines
- Project Management: Company-specific formats, team conventions, meeting recaps
- Business Operations: Standard reports, analytical procedures, financial models

### Personal Skills
- Content Creation: Custom document templates, specialized formatting
- Data Analysis: Custom data processing, specialized visualizations
- Development & Automation: Code generation templates, testing frameworks

## Limits and Constraints

### Request Limits
- Maximum Skills per request: 8
- Maximum Skill upload size: 8MB
- YAML frontmatter restrictions apply

### Environment Constraints
- No network access
- No runtime package installation
- Isolated environment per request

## Best Practices

- Pin to specific versions for production stability
- Use "latest" for active development
- Keep Skills list consistent for prompt caching performance
- Avoid including unused Skills (impacts performance)
- Implement error handling for Skill-related errors
