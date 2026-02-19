---
title: "Read the Computer Use launch post"
source_url: "https://www.anthropic.com/news/3-5-models-and-computer-use"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Read the Computer Use launch post

Published: October 22, 2024

Anthropic announced three major developments: an upgraded Claude 3.5 Sonnet, a new Claude 3.5 Haiku model, and a groundbreaking experimental capability called "computer use" now available in public beta.

## Claude 3.5 Sonnet Improvements

The refreshed Sonnet model delivers significant enhancements across benchmarks. On SWE-bench Verified, performance improved from 33.4% to 49.0%, outperforming all publicly accessible models including OpenAI's o1-preview. The model also advanced on TAU-bench, increasing from 62.6% to 69.2% in retail scenarios and from 36.0% to 46.0% in airline domains.

Early adopters reported substantial gains. GitLab observed strengthened reasoning capabilities with no latency increases. Cognition experienced meaningful improvements in coding, planning, and problem-solving. The Browser Company noted it surpassed every previously tested model.

The upgraded version maintains identical pricing and speed to its predecessor.

## Claude 3.5 Haiku

This new fastest-tier model matches Claude 3 Opus performance on numerous benchmarks while operating at comparable speeds to earlier Haiku versions. It particularly excels at coding tasks, achieving 40.6% on SWE-bench Verified.

Pricing: $0.80 per million input tokens and $4 per million output tokens.

## Computer Use Capability

This experimental feature allows Claude to interact with computers like humans do -- viewing screens, positioning cursors, clicking buttons, and typing. Rather than building task-specific tools, Anthropic taught Claude general computer skills applicable across standard software.

On OSWorld benchmarks measuring human-like computer usage, Claude scored 14.9% in screenshot-only scenarios -- significantly outperforming the next-best system at 7.8%.

Current limitations include challenges with scrolling, dragging, and zooming. Developers should begin with low-risk tasks.

Anthropic developed classifiers identifying computer use deployment and potential harms, addressing risks including spam, misinformation, and fraud.

## Early Adopters

Companies like Asana, Canva, Cognition, DoorDash, Replit, and The Browser Company are exploring these capabilities. Replit leverages computer use with UI navigation for developing app evaluation functionality.

## Safety and Evaluation

The US and UK AI Safety Institutes conducted joint pre-deployment testing. Anthropic evaluated the upgraded model for catastrophic risks, determining that its established ASL-2 Standard remains appropriate.
