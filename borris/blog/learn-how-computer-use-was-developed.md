---
title: "Learn how Computer Use was developed"
source_url: "https://www.anthropic.com/news/developing-computer-use"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Learn how Computer Use was developed

Anthropic announced that Claude can operate computers by interpreting screenshots, moving cursors, clicking, and entering text -- mimicking human computer interaction. This capability, currently in public beta, represents a significant advancement in AI development.

## Why Computer Use Matters

The capability unlocks applications previously impossible for AI assistants. A vast amount of modern work happens via computers, and enabling AI to interact with software directly rather than through custom tools opens new possibilities.

## Research Development

Claude's computer use builds on previous work in tool use and multimodality. The model learns to interpret screen images and calculate pixel distances for accurate cursor placement. Anthropic trained it on simple software like calculators and text editors, intentionally preventing internet access during training for safety reasons.

Claude generalized rapidly from limited training data, even self-correcting when encountering obstacles.

## Performance Metrics

On the OSWorld evaluation benchmark, Claude achieves 14.9% accuracy -- substantially higher than competing models at 7.7%, though far below human performance (70-75%).

## Safety Considerations

Claude 3.5 Sonnet with computer use remains at AI Safety Level 2. Key concerns include:
- Prompt injection attacks via internet-connected screenshots
- Intentional misuse for social media posting, domain registration, or election interference
- Anthropic implemented monitoring systems and safeguards specific to election-related activities

## Future Outlook

The development represents a completely different approach -- making models fit existing tools rather than designing specialized environments. Current limitations include slowness, error rates, and inability to perform actions like dragging or zooming.
