---
title: "How I Built a Second Brain in Obsidian for AI Agents - Business AI OS"
source_url: "https://www.youtube.com/watch?v=obsidian-second-brain-business-ai-os"
source_type: youtube
mentor: "Borris"
date_synced: "2026-04-08T00:00:00Z"
word_count: 7500
---

# How I Built a Second Brain in Obsidian for AI Agents - Business AI OS

## Overview

This video demonstrates building a second brain in Obsidian that plugs into Claude Co-work, Claude Code, or any AI agent, giving them persistent context and memory about you and your business. Covers the five big advantages, practical setup, file structure templates for business and solo use, and implications for how businesses will be run.

## Five Big Advantages of a Second Brain

### 1. Persistent Context

Most people use AI in isolated conversations, re-explaining everything each chat. With a second brain, your AI agent has persistent access to detailed context around everything - business, strategy, projects, brand, workflows, team, meetings, literally everything.

Example: Opening a new chat with Claude Co-work and asking "What should I focus on today?" - it pulls context and knows priorities are landing page copy changes, recording the Obsidian video, and organizing the Spain offsite in April.

Example: "Write me a LinkedIn post based on AI topics we discussed in our team meetings this week" - it goes through team meetings, finds AI topics discussed, uses a LinkedIn skill to write in your tone of voice.

### 2. AI Can Update the Context

Any decision, rule, or project update made in an AI chat can be logged directly back into the second brain. If you see something you don't like in output (e.g., "never use em dashes when writing content for me"), you say "remember this in my second brain" and it saves and updates as a rule in writing preferences.

This is huge because the more you and your team use AI to do tasks, the more context is built, the more guidelines it has, and the better your AI becomes for yourself and your entire team.

### 3. Better Skills with Shared Context

Skills (saved instructions for AI agents on how to do specific processes) usually have reference files inside the skill folder - ICP documents, voice personality documents, hook templates, etc. It takes a long time to provide all the context every new skill needs.

With a second brain, you only need to lay out the process and point it to the right context. You don't have to give it the exact same context over and over for each new skill.

**New approach to building skills**: Instead of embedding reference files in the skill, save reference files in the second brain and let the skill point towards the right folders. The skill MD only contains process instructions with directions to where specific context files live in the second brain.

Key benefit: Any update to a reference file in the second brain (e.g., the ICP document) instantly updates ALL skills that use it, instead of manually updating dozens of skills.

### 4. Works Across Any AI Provider

Your second brain in Obsidian is just a folder of markdown files. You can give Claude Co-work access, Claude Code access, Codex, Antigravity, or any other AI agent provider access to the same folder.

Example: Asking "What should I focus on today?" in Claude Co-work, Claude Code, or Codex all returns the same contextual answers because they access the same folder.

### 5. Scales Across Teams and Business

The shared second brain means your entire team's AI agents have access to up-to-date strategy documents, ICP documents, etc. An engineer can write a LinkedIn post with an on-point tone of voice using the shared context and skills.

Updates sync across the entire team through Obsidian's sync capabilities.

## How It Actually Works

### What is Obsidian

Obsidian is just a visual overlay of a folder and its files on your computer. All folders visible in Obsidian are also available in the actual folder. You point Claude Co-work, Claude Code, or any AI agent to the same folder.

No syncing, APIs, MCPs, or cloud-based software needed - it's all local.

### The CLAUDE.md Navigation Layer

The CLAUDE.md file is the instruction layer that tells your AI agent how to navigate the second brain folder. It's like a system prompt that explains how the vault is structured and where to retrieve and save data.

When you ask a question like "What did we talk about in our team meeting yesterday?":
1. The AI agent knows it needs more context
2. It reads the CLAUDE.md file to understand where in the vault to find relevant information
3. It reads specific documents (e.g., yesterday's Firefly transcript)
4. It answers the question with full context

### Why Not Just Use Claude's Built-in Memory

Claude's built-in memory is very limited - designed to remember the most essential facts, generally stored in one document. The Obsidian vault has thousands of pieces of context with much greater scope.

### Why Use Obsidian Instead of Just a Folder

You don't strictly need Obsidian - you can set this up in a folder. But Obsidian provides:
- Visual organization and navigation
- Search capabilities
- Graph view showing relationships between context files
- Automatic wiki link connections between documents
- Easy team syncing
- Completely free to use

## File Structure - Business Setup

### context/
General context about who you are, business, strategy, team, brand. Everything your AI agent needs to understand always.
- Team information
- Strategy documents
- Stakeholders and pain points
- Organization structure
- ICP (Ideal Customer Profile)
- Brand guidelines

### daily/
Where your AI agent logs everything that happened each day across sessions and meetings. The most important folder - gives AI agent continuity between conversations.

### departments/
For businesses with different departments (community, content, engineering, partnerships, operations, etc.). Contains SOPs for work in each department.
- Example: YouTube to community repurposing SOP

### intelligence/
Detailed context - meeting transcripts, decisions, competitor research, market insights stored over time. More detailed than the context folder.

### onboarding/
SOPs for onboarding new team members or clients.

### projects/
Highly context-dependent. Could be YouTube videos being worked on, client projects for agencies, etc. Allows ideation and work between different chat sessions.

### resources/
Reusable library of prompts, templates, frameworks, content output examples, good examples.

### skills/
Reference material that skills point to - strategy docs, voice guides, ICP descriptions, additional information that skills reference.

### tasks/
To-do lists and task tracking.

### teams/
Context around each team member's role and responsibilities so the agent always has context around anyone on the team.

### Root Files
- **CLAUDE.md** - The instruction layer (brain file) that tells AI how the file system works and how to navigate it
- Appears in Co-work's folder instruction section

## File Structure - Personal/Solopreneur Setup

Same structure as business but simpler - without departments, team section, and onboarding folders.

## Getting Started

### Key Principles
1. Don't overoptimize - start simple (even 5 files) and let the system evolve naturally
2. No perfect file structure - highly context dependent on your business, goals, projects
3. Many files can be created by your AI agent - don't get overwhelmed
4. Spend 30 minutes to an hour on initial context setup, then it naturally expands

### Setup Steps
1. Download Obsidian (free) from obsidian.md
2. Create a new vault with a name and folder location
3. Point Claude Code/Co-work to that same folder
4. Give it the Karpathy-style LLM wiki instructions or use a setup plugin
5. Start answering context questions to populate initial data

### Important Ongoing Practices
1. Every new task - always point towards the same folder
2. When you want AI to remember something - clearly tell it "remember this in your second brain" and ideally point to the specific file
3. If navigation issues occur - update the CLAUDE.md file with better rules
4. For skills - save reference files in the second brain instead of embedding in the skill, let skills point to the right folders

## Bigger Implications

Multiple developments converging:
- LLMs becoming better at reasoning
- MCPs allowing efficient software/internet navigation
- Skills, plugins, scheduled tasks enabling automation

The missing layer was context. This setup slowly allows people and businesses to adopt AI interfaces (like Claude Co-work/Code) as the main interface instead of hopping between 15 different softwares.

The value isn't in the setup itself - it's in the context that builds over time. Every decision logged, every correction saved, every project documented, every skill made - it all compounds. After 6 months, your AI agent is far more powerful than day one.

Even when better models come out, the same context becomes more powerful. Context will be your actual moat in upcoming months and years.

## Key Takeaways

1. **Start simple** - 5 files is enough to begin, let it grow naturally
2. **CLAUDE.md is the bridge** - it tells AI how to navigate your knowledge
3. **Skills should point to the second brain** - not embed duplicate reference files
4. **Context compounds** - the earlier you start, the more powerful your setup becomes
5. **Works across any AI provider** - just a folder of markdown files
6. **Team scaling** - shared second brain means everyone's AI gets smarter together
7. **Update rules in the second brain** - corrections cascade to all skills automatically
