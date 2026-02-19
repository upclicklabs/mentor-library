---
title: "Explore agent patterns with the Anthropic Cookbook"
source_url: "https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Explore agent patterns with the Anthropic Cookbook

This is a reference implementation repository for "Building Effective Agents" by Erik Schluntz and Barry Zhang from Anthropic. The repository contains minimal example implementations of common agent workflows.

## Content Structure

The `/patterns/agents` directory includes:

- **README.md** - Documentation
- **basic_workflows.ipynb** - Jupyter notebook with basic patterns
- **evaluator_optimizer.ipynb** - Advanced workflow implementation
- **orchestrator_workers.ipynb** - Advanced workflow implementation
- **util.py** - Utility functions
- **prompts/** - Directory containing prompt templates

## Agent Patterns Covered

### Basic Building Blocks

1. **Prompt Chaining** - Sequential prompts where output feeds into the next
2. **Routing** - Directing requests to different processing paths
3. **Multi-LLM Parallelization** - Running multiple LLM calls in parallel

### Advanced Workflows

1. **Orchestrator-Subagents** - One agent orchestrating multiple specialized subagents
2. **Evaluator-Optimizer** - Iterative improvement through evaluation and optimization loops

## Getting Started

The repository provides Jupyter notebooks for hands-on learning:

- Basic Workflows notebook
- Evaluator-Optimizer Workflow notebook
- Orchestrator-Workers Workflow notebook

## Repository Details

- **Owner**: Anthropics
- **License**: Public repository
- **Primary Language**: Python (Jupyter notebooks)

This is part of a larger Anthropic Cookbook repository with additional resources for various Claude API use cases.
