---
title: "Learn about Skills"
source_url: "https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Learn about Skills

## What are Agent Skills?

Agent Skills are modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.

## Why Use Skills

Skills are reusable, filesystem-based resources that provide Claude with domain-specific expertise: workflows, context, and best practices that transform general-purpose agents into specialists. Unlike prompts (conversation-level instructions for one-off tasks), Skills load on-demand and eliminate the need to repeatedly provide the same guidance across multiple conversations.

**Key benefits**:
- **Specialize Claude**: Tailor capabilities for domain-specific tasks
- **Reduce repetition**: Create once, use automatically
- **Compose capabilities**: Combine Skills to build complex workflows

## Using Skills

Anthropic provides pre-built Agent Skills for common document tasks (PowerPoint, Excel, Word, PDF), and you can create your own custom Skills. Both work the same way -- Claude automatically uses them when relevant to your request.

**Pre-built Agent Skills** are available to all users on claude.ai and via the Claude API.

**Custom Skills** let you package domain expertise and organizational knowledge. They're available across Claude's products: create them in Claude Code, upload them via the API, or add them in claude.ai settings.

## How Skills Work

Skills leverage Claude's VM environment to provide capabilities beyond what's possible with prompts alone. Claude operates in a virtual machine with filesystem access, allowing Skills to exist as directories containing instructions, executable code, and reference materials.

This filesystem-based architecture enables **progressive disclosure**: Claude loads information in stages as needed, rather than consuming context upfront.

### Three Levels of Loading

**Level 1: Metadata (always loaded)** - The Skill's YAML frontmatter provides discovery information (~100 tokens per Skill).

**Level 2: Instructions (loaded when triggered)** - The main body of SKILL.md contains procedural knowledge: workflows, best practices, and guidance (under 5k tokens).

**Level 3: Resources and code (loaded as needed)** - Skills can bundle additional materials: instructions, code, and resources (effectively unlimited, consumed only when accessed).

## Where Skills Work

### Claude API
Supports both pre-built Agent Skills and custom Skills via `skill_id` in the `container` parameter.

### Claude Code
Supports custom Skills as directories with SKILL.md files, automatically discovered and used.

### Claude Agent SDK
Supports custom Skills through filesystem-based configuration in `.claude/skills/`.

### Claude.ai
Supports both pre-built Agent Skills and custom Skills uploaded through Settings > Features.

## Skill Structure

Every Skill requires a `SKILL.md` file with YAML frontmatter containing `name` and `description` fields.

## Available Pre-built Skills

- **PowerPoint (pptx)**: Create presentations, edit slides, analyze presentation content
- **Excel (xlsx)**: Create spreadsheets, analyze data, generate reports with charts
- **Word (docx)**: Create documents, edit content, format text
- **PDF (pdf)**: Generate formatted PDF documents and reports

## Security Considerations

Use Skills only from trusted sources: those you created yourself or obtained from Anthropic. Skills provide Claude with new capabilities through instructions and code, and a malicious Skill can direct Claude to invoke tools or execute code in ways that don't match the Skill's stated purpose. Thoroughly audit any Skills from untrusted sources before use.

## Limitations and Constraints

- Custom Skills do not sync across surfaces (API, Claude.ai, Claude Code)
- Skills have different sharing models depending on the surface
- Runtime environment constraints vary by surface (network access, package installation)
