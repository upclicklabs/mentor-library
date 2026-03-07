---
title: "The NEW Way to 10x Your Claude Code Skills"
source_url: "youtube-transcript://the-new-way-to-10x-your-claude-code-skills"
source_type: youtube
mentor: "Borris"
date_synced: "2026-03-07T00:00:00Z"
---

# The NEW Way to 10x Your Claude Code Skills

## Overview

This video covers the new and improved Skill Creator skill from Anthropic — a tool that enables testing, benchmarking, and iterative improvement of Claude Code skills. It solves three key problems: no systematic way to test skills, no way to improve them with data, and Claude Code not triggering the right skill reliably.

## The Core Problem

If you've spent time inside Claude Code, skills are one of its most powerful features. But creating custom skills reveals drawbacks:

- No systematized way to test or improve skills
- Claude Code doesn't always trigger the right skill
- No visibility into whether a skill is actually performing optimally

## What the Skill Creator Does

The Skill Creator skill helps users:

1. **Write evals** — Create evaluation criteria for skills
2. **Run benchmarks** — A/B test skills with and without, or compare versions
3. **Keep skills working** as model capabilities evolve

This brings the rigor of software development — testing, benchmarking, and iterative improvement — without requiring any code.

## Benchmarking Capabilities

The Skill Creator enables:

- **A/B testing** — Compare skill performance vs. baseline Claude Code
- **Parallel agents** — Run multiple tests simultaneously
- **Performance metrics** — Track tokens, pass rates, total time
- **Trigger optimization** — Ensure Claude Code actually uses the right skill

Example: Testing the PDF creation skill showed clear differences in performance with the skill vs. without it, including token usage, pass rates, and total time.

## Two Types of Skills

Understanding skill types matters because each needs different evaluation approaches:

### 1. Capability Uplift Skills

Skills that let Claude Code do something **better** than it otherwise would. Claude Code is weak at something, and the skill helps it improve.

**Example:** The front-end design skill. Without it, Claude Code builds generic websites. With it, the output quality significantly improves.

Most official Anthropic skills fall under this category: PDF, PowerPoint Creator, MCP Builder, DocX, etc.

**Why evals matter for capability uplift:** As models improve (e.g., from Opus 4.6 to Opus 5.0), a capability uplift skill may become unnecessary — or even produce worse outputs. Evals tell you when that happens.

### 2. Encoded Preference Skills

Skills that define a **specific workflow** — Claude Code can already do the tasks, but you want them done in a specific order or way.

**Example:** A YouTube Pipeline skill that chains together:
1. Search YouTube for creators (using YouTube search skill)
2. Send information to Notebook LM (using Notebook LM skill)
3. Analyze information on Notebook LM
4. Create deliverables (PowerPoint, infographics, etc.)

**Why evals matter for encoded preference:** These are only as valuable as their fidelity to your actual workflow. Evals verify that the skill is following all steps in the correct order.

## What the Tests Actually Do

### 1. Catching Regressions in Quality

Detects when model improvements have made a skill less effective or unnecessary. Uses benchmark mode for A/B testing — skill vs. no skill, or version vs. version.

### 2. Multi-Agent Support

Run 5, 6, 7, 8 tests simultaneously. Testing isn't a long, laborious process.

### 3. Trigger Reliability

Skills aren't preloaded into the system prompt. Claude Code maintains a list of all skills with titles and ~100-word descriptions. As the skill list grows, description quality becomes critical:

- **Too broad** → false triggers
- **Too narrow** → never fires

The Skill Creator optimizes these descriptions to thread the needle. The skill description optimization results show dramatic improvement in trigger reliability.

## How to Install

1. Run `/plugin` in Claude Code
2. Search for "skill creator"
3. Install the official Claude Code plugin
4. Exit Claude Code (`/exit`) and restart

## How to Use

- Ask Claude Code: "What can the skill creator skill do for me?"
- Available functions: Create new skills, modify existing skills, run evals and benchmarking, optimize trigger descriptions
- Either tell Claude Code what you want to do, or use `/skill-creator`

## Real Usage Example: YouTube Pipeline Skill

Creating the YouTube Pipeline skill with the Skill Creator:

1. Described the desired workflow (search YouTube → upload to Notebook LM → analyze → create deliverables)
2. Skill Creator designed a 6-step implementation plan
3. Used plan mode for visibility on what would be built
4. Ran evals for fidelity testing (encoded preference skill)
5. Tested 9 criteria — all passed
6. Received additional insights and stats

## Key Takeaways

- Skills are one of the easiest ways to supercharge Claude Code performance
- The Skill Creator supercharges the skills themselves
- Moving away from the "black box" of AI into informed decision-making
- Provides control, consistency, and visibility into what's happening
- Enables users to make informed decisions and guide Claude Code along the correct path rather than blindly accepting outputs
