---
title: "Optimize your results with Claude 4 prompting best practices"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Optimize your results with Claude 4 prompting best practices

This guide provides prompt engineering techniques for Claude's latest models, including Claude Opus 4.6, Claude Sonnet 4.6, and Claude Haiku 4.5. These models have been trained for more precise instruction following than previous generations.

## General Principles

### Be Explicit with Your Instructions

Claude responds well to clear, explicit instructions. Being specific about your desired output can help enhance results. If you want "above and beyond" behavior, explicitly request it rather than relying on the model to infer from vague prompts.

### Add Context to Improve Performance

Providing context or motivation behind your instructions can help Claude better understand your goals and deliver more targeted responses. Claude is smart enough to generalize from the explanation.

### Be Vigilant with Examples and Details

Claude pays close attention to details and examples as part of its precise instruction following capabilities. Ensure that your examples align with the behaviors you want to encourage.

### Long-Horizon Reasoning and State Tracking

Claude's latest models excel at long-horizon reasoning tasks with exceptional state tracking capabilities. Claude maintains orientation across extended sessions by focusing on incremental progress.

#### Multi-Context Window Workflows

For tasks spanning multiple context windows:

1. Use a different prompt for the very first context window to set up a framework
2. Have the model write tests in a structured format
3. Set up quality of life tools (e.g., setup scripts)
4. Consider starting with a brand new context window rather than using compaction
5. Provide verification tools
6. Encourage complete usage of context

#### State Management Best Practices

- Use structured formats (JSON) for state data
- Use unstructured text for progress notes
- Use git for state tracking
- Emphasize incremental progress

### Communication Style

Claude's latest models have a more concise and natural communication style: more direct and grounded, more conversational, and less verbose.

## Guidance for Specific Situations

### Balance Verbosity

Claude's latest models tend toward efficiency and may skip verbal summaries after tool calls. If you want Claude to provide updates as it works, explicitly request it.

### Tool Usage Patterns

For Claude to take action, be explicit. "Can you suggest some changes" may result in suggestions only, while "Change this function" will make the changes.

### Balancing Autonomy and Safety

Without guidance, Claude may take actions that are difficult to reverse. Add guidance about confirming before potentially risky actions.

### Overthinking and Excessive Thoroughness

Claude 4.6 models do significantly more upfront exploration than previous models. To address:

- Remove anti-laziness prompts
- Soften tool-use language
- Remove explicit think tool instructions
- Use effort as the primary control lever

### Control the Format of Responses

- Tell Claude what to do instead of what not to do
- Use XML format indicators
- Match your prompt style to the desired output
- Use detailed prompts for specific formatting preferences

### Research and Information Gathering

Claude's latest models demonstrate exceptional agentic search capabilities. For optimal results: provide clear success criteria, encourage source verification, and use a structured approach for complex research.

### Subagent Orchestration

Claude's latest models demonstrate significantly improved native subagent orchestration capabilities. Ensure well-defined subagent tools, let Claude orchestrate naturally, and watch for overuse.

### Leverage Thinking and Interleaved Thinking Capabilities

Claude Opus 4.6 uses adaptive thinking where Claude dynamically decides when and how much to think. Claude Sonnet 4.6 supports both adaptive and manual extended thinking with interleaved mode.

### Optimize Parallel Tool Calling

Claude's latest models excel at parallel tool execution: running multiple speculative searches during research, reading several files at once, and executing bash commands in parallel.

### Reduce File Creation in Agentic Coding

Claude's latest models may sometimes create new files for testing and iteration purposes. If you prefer to minimize file creation, instruct Claude to clean up temporary files.

### Frontend Design

Claude excels at building complex, real-world web applications with strong frontend design. Without guidance, models can default to generic patterns. Provide specific aesthetic guidance for distinctive frontends.

### Avoid Focusing on Passing Tests and Hard-Coding

Claude can sometimes focus too heavily on making tests pass at the expense of more general solutions. Provide explicit guidance for robust, generalizable solutions.

### Minimizing Hallucinations in Agentic Coding

Claude's latest models are less prone to hallucinations. Encourage investigating and reading relevant files before answering questions about the codebase.

### Migrating Away from Prefilled Responses

Starting with Claude 4.6 models, prefilled responses on the last assistant turn are no longer supported. Use structured outputs, direct instructions, or tool calling as alternatives.

## Migration Considerations

When migrating to Claude 4.6 models from earlier generations:

1. Be specific about desired behavior
2. Frame your instructions with modifiers
3. Request specific features explicitly
4. Update thinking configuration to adaptive thinking
5. Migrate away from prefilled responses
6. Tune anti-laziness prompting (dial back aggressive language)
