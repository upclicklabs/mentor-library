---
title: "Prompt Engineering Overview"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Prompt Engineering Overview

## Before Prompt Engineering

This guide assumes that you have:
1. A clear definition of the success criteria for your use case
2. Some ways to empirically test against those criteria
3. A first draft prompt you want to improve

## When to Prompt Engineer

This guide focuses on success criteria that are controllable through prompt engineering. Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can sometimes be more easily improved by selecting a different model.

### Prompting vs. Finetuning

Prompt engineering is far faster than other methods of model behavior control, such as finetuning, and can often yield leaps in performance in far less time. Reasons to consider prompt engineering over finetuning:

- **Resource efficiency**: Fine-tuning requires high-end GPUs and large memory, while prompt engineering only needs text input
- **Cost-effectiveness**: For cloud-based AI services, fine-tuning incurs significant costs. Prompt engineering uses the base model, which is typically cheaper
- **Maintaining model updates**: When providers update models, fine-tuned versions might need retraining. Prompts usually work across versions without changes
- **Time-saving**: Fine-tuning can take hours or even days. Prompt engineering provides nearly instantaneous results
- **Minimal data needs**: Fine-tuning needs substantial task-specific, labeled data. Prompt engineering works with few-shot or even zero-shot learning
- **Flexibility and rapid iteration**: Quickly try various approaches, tweak prompts, and see immediate results
- **Domain adaptation**: Easily adapt models to new domains by providing domain-specific context in prompts
- **Comprehension improvements**: Prompt engineering is far more effective than finetuning at helping models better understand and utilize external content such as retrieved documents
- **Preserves general knowledge**: Fine-tuning risks catastrophic forgetting. Prompt engineering maintains the model's broad capabilities
- **Transparency**: Prompts are human-readable, showing exactly what information the model receives

## How to Prompt Engineer

The prompt engineering techniques are organized from most broadly effective to more specialized. When troubleshooting performance, try these techniques in order:

1. **Prompt generator** - Use the prompt generator in the Claude Console
2. **Be clear and direct** - Write unambiguous instructions
3. **Use examples (multishot)** - Provide example inputs and outputs
4. **Let Claude think (chain of thought)** - Encourage step-by-step reasoning
5. **Use XML tags** - Structure your prompts with XML tags
6. **Give Claude a role (system prompts)** - Set context with system prompts
7. **Chain complex prompts** - Break complex tasks into steps
8. **Long context tips** - Optimize for long context windows

## Prompt Engineering Tutorial

Interactive tutorials are available:
- GitHub prompting tutorial: An example-filled tutorial covering prompt engineering concepts
- Google Sheets prompting tutorial: A lighter weight version via an interactive spreadsheet
