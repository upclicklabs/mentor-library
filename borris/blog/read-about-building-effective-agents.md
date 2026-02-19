---
title: "Read about building effective agents"
source_url: "https://www.anthropic.com/engineering/building-effective-agents"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Read about building effective agents

## Core Message

Anthropic recommends using simple, composable patterns rather than complex frameworks when building LLM agents. Success comes from choosing the right approach for your needs, not from building the most sophisticated system.

## Key Distinction

The article defines two types of agentic systems:

- **Workflows**: LLMs and tools operate through predefined code paths
- **Agents**: LLMs dynamically direct their own processes and maintain control over task accomplishment

## When to Build Agents

Agents suit open-ended problems where the required steps cannot be predicted and fixed paths cannot be hardcoded. However, simpler solutions -- optimized single LLM calls with retrieval and examples -- often suffice.

## Five Workflow Patterns

1. **Prompt Chaining**: Decompose tasks into sequential steps where each LLM processes previous output
2. **Routing**: Classify inputs and direct them to specialized handlers
3. **Parallelization**: Run tasks simultaneously (sectioning) or run identical tasks multiple times (voting)
4. **Orchestrator-Workers**: Central LLM dynamically breaks down tasks and synthesizes worker results
5. **Evaluator-Optimizer**: One LLM generates responses while another provides iterative feedback

## Three Implementation Principles

1. Maintain **simplicity** in agent design
2. Prioritize **transparency** by showing planning steps explicitly
3. Craft **agent-computer interfaces** through thorough tool documentation and testing

## Tool Design Guidance

Invest effort in tool definitions matching human-computer interface standards. Use formats naturally occurring in training data and minimize formatting overhead.
