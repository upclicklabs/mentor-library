---
title: "Use the Eval Tool on Claude Console"
source_url: "https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use the Eval Tool on Claude Console

The Claude Console features an Evaluation tool that allows you to test your prompts under various scenarios.

## Accessing the Evaluate Feature

To get started with the Evaluation tool:
1. Open the Claude Console and navigate to the prompt editor.
2. After composing your prompt, look for the 'Evaluate' tab at the top of the screen.

Ensure your prompt includes at least 1-2 dynamic variables using the double brace syntax: `{{variable}}`. This is required for creating eval test sets.

## Generating Prompts

The Console offers a built-in prompt generator powered by Claude Opus 4.1:

1. Click 'Generate Prompt' to open a modal for entering your task information
2. Describe your desired task with as much or as little detail as you desire
3. Click the 'Generate Prompt' button to have Claude generate a high quality prompt

## Creating Test Cases

When you access the Evaluation screen, you have several options:
1. Click the '+ Add Row' button to manually add a case
2. Use the 'Generate Test Case' feature to have Claude automatically generate test cases
3. Import test cases from a CSV file

You can also edit the test case generation logic for greater precision and specificity. If you update your original prompt text, you can re-run the entire eval suite against the new prompt.

## Tips for Effective Evaluation

Structure your prompts with clear input and output formats. Use dynamic variables in double brace syntax to enable varying inputs and evaluating outputs consistently.

## Understanding and comparing results

The Evaluation tool offers several features:
1. **Side-by-side comparison**: Compare outputs of two or more prompts
2. **Quality grading**: Grade response quality on a 5-point scale
3. **Prompt versioning**: Create new versions and re-run the test suite

By reviewing results across test cases and comparing different prompt versions, you can spot patterns and make informed adjustments more efficiently.
