---
title: "Implement best practices when creating Skills"
source_url: "https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Implement best practices when creating Skills

Learn how to write effective Skills that Claude can discover and use successfully.

## Core Principles

### Concise is Key

The context window is a shared resource. Your Skill shares the context window with everything else Claude needs to know. Only add context Claude doesn't already have. Challenge each piece of information: "Does Claude really need this explanation?" and "Can I assume Claude knows this?"

### Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability:

- **High freedom** (text-based instructions): Use when multiple approaches are valid and decisions depend on context
- **Medium freedom** (pseudocode or scripts with parameters): Use when a preferred pattern exists but some variation is acceptable
- **Low freedom** (specific scripts, few or no parameters): Use when operations are fragile, error-prone, or consistency is critical

### Test with All Models You Plan to Use

Skills act as additions to models, so effectiveness depends on the underlying model. What works perfectly for Opus might need more detail for Haiku.

## Skill Structure

### Naming Conventions

Use consistent naming patterns. Consider gerund form (verb + -ing) for Skill names: `processing-pdfs`, `analyzing-spreadsheets`, `managing-databases`.

The `name` field must use lowercase letters, numbers, and hyphens only.

### Writing Effective Descriptions

Always write in third person. The description is injected into the system prompt. Be specific and include key terms. Include both what the Skill does and specific triggers/contexts for when to use it.

### Progressive Disclosure Patterns

SKILL.md serves as an overview that points Claude to detailed materials as needed:

- **Pattern 1: High-level guide with references** - Quick start in SKILL.md, detailed docs in separate files
- **Pattern 2: Domain-specific organization** - Organize content by domain to avoid loading irrelevant context
- **Pattern 3: Conditional details** - Show basic content, link to advanced content

### Avoid Deeply Nested References

Keep references one level deep from SKILL.md. All reference files should link directly from SKILL.md.

### Structure Longer Reference Files with Table of Contents

For reference files longer than 100 lines, include a table of contents at the top.

## Workflows and Feedback Loops

### Use Workflows for Complex Tasks

Break complex operations into clear, sequential steps. For particularly complex workflows, provide a checklist that Claude can track progress against.

### Implement Feedback Loops

Common pattern: Run validator, fix errors, repeat. This pattern greatly improves output quality.

## Content Guidelines

### Avoid Time-Sensitive Information

Don't include information that will become outdated. Use "old patterns" sections for deprecated approaches.

### Use Consistent Terminology

Choose one term and use it throughout the Skill.

## Common Patterns

- **Template pattern**: Provide templates for output format, matching the level of strictness to your needs
- **Examples pattern**: Provide input/output pairs for output quality
- **Conditional workflow pattern**: Guide Claude through decision points

## Evaluation and Iteration

### Build Evaluations First

Create evaluations BEFORE writing extensive documentation. Evaluation-driven development: identify gaps, create evaluations, establish baseline, write minimal instructions, iterate.

### Develop Skills Iteratively with Claude

Work with one instance of Claude ("Claude A") to create a Skill that will be used by other instances ("Claude B"). Claude A helps design and refine instructions, while Claude B tests them in real tasks.

## Advanced: Skills with Executable Code

### Solve, Don't Punt

When writing scripts for Skills, handle error conditions rather than failing and letting Claude figure it out.

### Provide Utility Scripts

Pre-made scripts are more reliable than generated code, save tokens and time, and ensure consistency.

### Create Verifiable Intermediate Outputs

Use the "plan-validate-execute" pattern: create a plan in a structured format, validate that plan with a script before executing.

### Package Dependencies

List required packages in SKILL.md and verify they're available in the code execution environment.

## Checklist for Effective Skills

### Core Quality
- Description is specific and includes key terms
- SKILL.md body is under 500 lines
- Additional details are in separate files (if needed)
- No time-sensitive information
- Consistent terminology throughout
- Examples are concrete, not abstract
- File references are one level deep
- Progressive disclosure used appropriately
- Workflows have clear steps

### Code and Scripts
- Scripts solve problems rather than punt to Claude
- Error handling is explicit and helpful
- No "voodoo constants" (all values justified)
- Required packages listed and verified as available
- Validation/verification steps for critical operations
- Feedback loops included for quality-critical tasks

### Testing
- At least three evaluations created
- Tested with Haiku, Sonnet, and Opus
- Tested with real usage scenarios
- Team feedback incorporated (if applicable)
