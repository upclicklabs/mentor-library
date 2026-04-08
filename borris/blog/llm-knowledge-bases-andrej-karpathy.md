---
title: "LLM Knowledge Bases - Andrej Karpathy"
source_url: "https://x.com/karpathy/status/llm-knowledge-bases"
source_type: blog
mentor: "Borris"
date_synced: "2026-04-08T00:00:00Z"
word_count: 1200
---

# LLM Knowledge Bases - Andrej Karpathy

## Overview

Andrej Karpathy shared his approach to using LLMs to build personal knowledge bases for research topics. A large fraction of his recent token throughput goes into manipulating knowledge (stored as markdown and images) rather than code. The latest LLMs are quite good at it.

## Data Ingest

Index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory. Then use an LLM to incrementally "compile" a wiki - a collection of .md files in a directory structure.

The wiki includes:
- Summaries of all data in raw/
- Backlinks between related content
- Categorization of data into concepts
- Articles written for each concept
- Links connecting everything together

To convert web articles into .md files, Karpathy uses the Obsidian Web Clipper extension, plus a hotkey to download all related images to local so the LLM can easily reference them.

## IDE

Obsidian serves as the IDE "frontend" to view raw data, the compiled wiki, and derived visualizations. Important: the LLM writes and maintains all of the data of the wiki - Karpathy rarely touches it directly. He has experimented with Obsidian plugins to render and view data in other ways (e.g., Marp for slides).

## Q&A

Once the wiki is big enough (e.g., ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki. It will research the answers across the knowledge base.

Key insight: "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this small scale."

At this scale (~100 articles, ~400K words), auto-maintained indexes and summaries are sufficient for navigation without needing vector search or embeddings.

## Output

Instead of getting answers in text/terminal, have the LLM render:
- Markdown files
- Slide shows (Marp format)
- Matplotlib images

All viewable again in Obsidian. Many other visual output formats are possible depending on the query.

Critical pattern: Filing outputs back into the wiki to enhance it for further queries. Your own explorations and queries always "add up" in the knowledge base. This creates a compounding effect.

## Linting

Run LLM "health checks" over the wiki to:
- Find inconsistent data
- Impute missing data (with web searchers)
- Find interesting connections for new article candidates
- Incrementally clean up the wiki and enhance data integrity

The LLMs are quite good at suggesting further questions to ask and look into.

## Extra Tools

Develop additional tools to process the data. For example, a small naive search engine over the wiki that works both:
- Directly via web UI
- As a CLI tool handed off to an LLM for larger queries

## Further Explorations

As the repo grows, the natural desire is to think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.

## Architecture Summary

```
raw/ (source documents)
  -> LLM compiles into wiki/
    -> wiki/ contains .md files with:
      - index.md (auto-maintained)
      - summaries
      - concept articles
      - backlinks
      - categorization
    -> operated on by CLI tools
    -> Q&A queries
    -> outputs filed back into wiki (compounding)
    -> periodic linting for data integrity
  -> all viewable in Obsidian
```

## Key Principles

1. **LLM owns the wiki** - you rarely ever write or edit the wiki manually, it's the domain of the LLM
2. **Raw data stays raw** - source documents go in raw/, the wiki is the compiled output
3. **Auto-maintained indexes** - no fancy RAG needed at small scale (~400K words)
4. **Compounding knowledge** - query outputs get filed back into the wiki
5. **Linting for integrity** - periodic health checks keep the wiki consistent
6. **Tool extensibility** - build CLI tools the LLM can use for larger queries
7. **Left intentionally vague** - designed to be customized per project and use case

## Notable Quote

"There is room here for an incredible new product instead of a hacky collection of scripts."
