---
title: "Implement extended thinking best practices"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Implement extended thinking best practices

This guide provides advanced strategies and techniques for getting the most out of Claude's extended thinking features. Extended thinking allows Claude to work through complex problems step-by-step, improving performance on difficult tasks.

## Before diving in

This guide presumes you have already decided to use extended thinking mode and have reviewed the extended thinking implementation guide.

### Technical considerations

- Thinking tokens have a minimum budget of 1024 tokens. Start with the minimum and incrementally increase based on your needs.
- For workloads where the optimal thinking budget is above 32K, use batch processing to avoid networking issues.
- Extended thinking performs best in English, though final outputs can be in any supported language.
- If you need thinking below the minimum budget, use standard mode with traditional chain-of-thought prompting using XML tags like `<thinking>`.

## Prompting techniques for extended thinking

### Use general instructions first, then troubleshoot with more step-by-step instructions

Claude often performs better with high level instructions to think deeply rather than step-by-step prescriptive guidance.

Instead of prescriptive steps, consider:

```text
Please think about this math problem thoroughly and in great detail.
Consider multiple approaches and show your complete reasoning.
Try different methods if your first approach doesn't work.
```

Start with generalized instructions, then read Claude's thinking output and iterate to provide more specific instructions.

### Multishot prompting with extended thinking

Multishot prompting works well with extended thinking. You can include few-shot examples using XML tags like `<thinking>` or `<scratchpad>` to indicate canonical patterns. Claude will generalize the pattern to the formal extended thinking process.

### Maximizing instruction following

Claude shows significantly improved instruction following when extended thinking is enabled. To maximize this:
- Be clear and specific about what you want
- For complex instructions, break them into numbered steps
- Allow Claude enough budget to process the instructions fully

### Using extended thinking to debug and steer Claude's behavior

You can use Claude's thinking output to debug logic, though this method is not always perfectly reliable. Tips:
- Avoid passing Claude's extended thinking back in the user text block
- Prefilling extended thinking is explicitly not allowed
- When extended thinking is turned off, standard assistant response text prefill is still allowed

### Making the best of long outputs and longform thinking

- For dataset generation, try prompts such as "Please create an extremely detailed table of..."
- Increase both the maximum extended thinking length AND explicitly ask for longer outputs
- For very long outputs (20,000+ words), request a detailed outline with word counts, then ask Claude to index paragraphs to the outline

### Example use cases for longer extended thinking

**Complex STEM problems** - building mental models, applying specialized knowledge, working through sequential logical steps

**Constraint optimization problems** - satisfying multiple competing requirements simultaneously

**Thinking frameworks** - structured analytical frameworks (Blue Ocean Strategy, Porter's Five Forces, Ansoff Matrix, Three Horizons)

### Have Claude reflect on and check its work

Use natural language prompting to improve consistency and reduce errors:
1. Ask Claude to verify its work with test cases before declaring a task complete
2. Instruct the model to analyze whether its previous step achieved the expected result
3. For coding tasks, ask Claude to run through test cases in its extended thinking

```text
Write a function to calculate the factorial of a number.
Before you finish, please verify your solution with test cases for:
- n=0
- n=1
- n=5
- n=10
And fix any issues you find.
```
