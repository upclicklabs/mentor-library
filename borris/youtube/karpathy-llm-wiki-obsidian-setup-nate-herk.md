---
title: "Karpathy's LLM Wiki in Obsidian - Practical Setup Guide - Nate Herk"
source_url: "https://www.youtube.com/watch?v=karpathy-llm-wiki-obsidian-nate-herk"
source_type: youtube
mentor: "Borris"
date_synced: "2026-04-08T00:00:00Z"
word_count: 7000
---

# Karpathy's LLM Wiki in Obsidian - Practical Setup Guide - Nate Herk

## Overview

Nate Herk demonstrates a practical implementation of Andrej Karpathy's LLM Knowledge Base concept. He shows how to set up an Obsidian vault, use Claude Code to ingest and organize content, and build a queryable knowledge system - with two real examples: a YouTube transcript knowledge system (36 videos) and a personal second brain for business.

## The Setup in Action

Nate has two separate Obsidian vaults:
1. **YouTube Knowledge System** - 36 recent YouTube videos organized into a knowledge system with nodes, patterns, and relationships between tools, skills, MCP servers, techniques, and concepts mentioned across all videos.
2. **Personal Brain** - Personal life, business (UpAI), YouTube channel, employees, Q2 initiatives - a personal second brain.

These can be combined or kept separate, and more knowledge systems can be built and plugged into different AI agents as needed.

## Core Architecture

The vault structure is simple:

```
my-wiki/
  raw/          # Source documents (articles, transcripts, PDFs)
  wiki/         # LLM-compiled knowledge
    index.md    # Master index of all content
    log.md      # Operation history
    sources/    # Source summaries
    concepts/   # Concept articles
    entities/   # People, organizations
    analysis/   # Analysis and comparisons
  CLAUDE.md     # Instructions for AI agent navigation
```

### Index File
The index organizes all content by category:
- Tools (clickable links to each tool's page)
- Techniques (agent teams, sub-agents, permission modes, WAT framework)
- Concepts (MCP servers, RAG, vibe coding)
- Sources (YouTube videos, articles)
- People
- Comparisons

### Log File
Operation history tracking every update. For single-batch ingestion, the log is small. For ongoing additions, it records every wiki update with timestamps.

### CLAUDE.md
Explains how the project works - how to search, how to update, how to navigate the wiki structure.

## Step-by-Step Setup

### 1. Install Obsidian
Download from obsidian.md (free). Create a new vault with a name and folder location.

### 2. Initialize with Claude Code
Open the vault folder in VS Code or terminal. Run Claude Code. Paste in Karpathy's LLM wiki concept (from his gist) along with instructions like:

"You are now my LLM wiki agent. Implement this exact idea file as my complete second brain. Guide me step by step. Create the CLAUDE.md schema."

Claude Code creates the raw/ and wiki/ folders with initial structure.

### 3. Customize the Context
Tell Claude Code what this project is for:
- "This is my second brain for personal things and business things"
- "This is a research project for AI articles"
- "This is a YouTube knowledge base"

The project structure adapts based on context provided.

### 4. Ingest Content
Use the Obsidian Web Clipper extension to capture web articles directly into the raw/ folder. Or paste in transcripts, PDFs, etc.

Tell Claude Code: "I just threw in an article called AI 2027 into the raw. Can you please go ahead and ingest that?"

Claude Code will:
- Read through the article
- Ask clarifying questions about emphasis, granularity, and focus
- Create multiple wiki pages (not just one - it does its own chunking)
- Build relationships between sections
- Update the index

### 5. Watch Relationships Form
In Obsidian's graph view, you can watch in real time as wiki pages are created and relationships form between concepts, people, organizations, and sources.

## Ingestion Examples

### Single Article (AI 2027)
- Created 23 wiki pages from one article
- Categories: 1 source, 6 people, 5 organizations, 1 AI systems page, multiple concepts (technical alignment, geopolitical), analysis
- Took about 10 minutes
- Automatic relationship building between all entities

### Batch Upload (36 YouTube Transcripts)
- Took about 14 minutes
- Created relationships between every tool, skill, MCP server mentioned across all videos
- Emergent patterns visible in graph view showing which concepts are hubs vs isolated nodes

## Navigation and Querying

Click through relationships in Obsidian:
- Source article -> OpenAI link -> OpenAI page -> model spec reference -> LLM psychology model
- Each click reveals more connections and context

Query options:
- Inside the Obsidian environment directly
- From a different project that points at the vault folder
- Share the CLAUDE.md so any new project understands the wiki structure

## The Hot Cache Pattern

For executive assistant use cases, add a hot.md file in the wiki:
- ~500 words/characters of the most recent context
- Saves the most recent thing discussed or given
- Prevents unnecessary crawling of wiki pages for recent queries
- Not needed for static knowledge bases (like YouTube transcripts)

## Practical Integration Example

Nate's executive assistant (Herk 2) has a CLAUDE.md that includes:

```
Wiki path: /path/to/herkbrain/vault
When you need context about me and my business:
1. Read the hot cache first
2. Read the index
3. Read the domain subindex
4. Search through the wiki
Don't read from the wiki unless you actually need it.
```

This replaced context files inside the project and actually reduced token usage.

## Wiki vs RAG Comparison

| Aspect | Karpathy Wiki | Semantic Search RAG |
|--------|--------------|-------------------|
| How it finds data | Reads indexes, follows links | Similarity search |
| Understanding | Deeper relationships via links | Chunk similarity |
| Infrastructure | Just markdown files | Embedding model + vector DB + chunking pipeline |
| Cost | Basically free (only tokens) | Ongoing compute and storage |
| Maintenance | Run a lint, add articles | Re-embed when things change |
| Scale limit | Hundreds of pages with good indexes | Millions of documents |

### When to Use Wiki
- Hundreds of pages with good indexes
- Personal or small team knowledge bases
- Projects where relationships matter more than volume

### When to Use RAG
- Millions of documents
- Enterprise scale
- When token costs exceed embedding/storage costs

## Linting

Run LLM health checks to:
- Find inconsistent data
- Impute missing data with web searches
- Find interesting connections for new article candidates
- Ensure scalability and structure

Can be run daily, weekly, or whenever needed. The LLM may ask for more information or suggest additional articles to fill gaps.

## Flat vs Structured Wiki

Karpathy prefers keeping things simple and flat (no subfolders, minimal over-organizing). But for some projects, subfolders make more sense:
- **YouTube transcript project**: Subfolders for tools, techniques, concepts, sources - makes sense due to categorical nature
- **Personal brain**: Flat markdown files with no structure - works when content is more free-form

Let the structure evolve naturally based on the project's needs.

## Token Efficiency

One X user turned 383 scattered files and over 100 meeting transcripts into a compact wiki and dropped token usage by 95% when querying with Claude. The compiled wiki with indexes is far more token-efficient than raw source documents.

## Key Takeaways

1. **5-minute setup** - Create vault, run Claude Code with Karpathy's prompt, start ingesting
2. **The LLM does the heavy lifting** - all relationship building is automatic
3. **Start with one source** - the system grows naturally as you add more
4. **Multiple vaults for different purposes** - YouTube knowledge, personal brain, research topics
5. **Hot cache for active use cases** - saves tokens on frequently-accessed context
6. **CLAUDE.md is portable** - share it with any project that needs vault access
7. **Linting keeps quality high** - periodic health checks maintain data integrity
8. **Wiki beats RAG at small scale** - simpler, cheaper, deeper relationships
9. **Context is the moat** - the knowledge base becomes more valuable over time
10. **This is how 2026 AI software gets built** - give it a high-level idea and it builds it out
