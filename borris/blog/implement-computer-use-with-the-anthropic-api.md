---
title: "Implement Computer Use with the Anthropic API"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/computer-use"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Implement Computer Use with the Anthropic API

Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction.

Computer use is currently in beta and requires a beta header:
- `"computer-use-2025-11-24"` for Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5
- `"computer-use-2025-01-24"` for Sonnet 4.5, Haiku 4.5, Opus 4.1, Sonnet 4, Opus 4, and Sonnet 3.7

## Overview

Computer use is a beta feature that enables Claude to interact with desktop environments:
- Screenshot capture: See what's currently displayed on screen
- Mouse control: Click, drag, and move the cursor
- Keyboard input: Type text and use keyboard shortcuts
- Desktop automation: Interact with any application or interface

## Model compatibility

| Model | Tool Version | Beta Flag |
|-------|--------------|-----------|
| Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5 | `computer_20251124` | `computer-use-2025-11-24` |
| All other supported models | `computer_20250124` | `computer-use-2025-01-24` |

Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5 introduce the `computer_20251124` tool version with new capabilities including the zoom action for detailed screen region inspection.

## Security considerations

Computer use has unique risks. Precautions include:
1. Using a dedicated virtual machine or container with minimal privileges
2. Avoiding giving the model access to sensitive data
3. Limiting internet access to an allowlist of domains
4. Asking a human to confirm decisions with real-world consequences

Classifiers automatically run on prompts to flag potential prompt injections. When detected, the model asks for user confirmation before proceeding.

## How computer use works

1. Provide Claude with the computer use tool and a user prompt
2. Claude decides to use the computer use tool and constructs a tool use request
3. Extract tool input, evaluate the tool on a computer, and return results
4. Claude continues calling tools until the task is completed

The repetition of steps 3 and 4 without user input is the "agent loop."

### The computing environment

Computer use requires a sandboxed computing environment with:
- Virtual display (Xvfb)
- Desktop environment (Mutter + Tint2)
- Pre-installed Linux applications
- Tool implementations for translating Claude's requests
- Agent loop for communication

### Available actions

**Basic actions (all versions)**: screenshot, left_click, type, key, mouse_move

**Enhanced actions (computer_20250124)**: scroll, left_click_drag, right_click, middle_click, double_click, triple_click, left_mouse_down, left_mouse_up, hold_key, wait

**Enhanced actions (computer_20251124)**: All above plus zoom (view specific screen region at full resolution)

### Tool parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `type` | Yes | Tool version |
| `name` | Yes | Must be "computer" |
| `display_width_px` | Yes | Display width in pixels |
| `display_height_px` | Yes | Display height in pixels |
| `display_number` | No | Display number for X11 environments |
| `enable_zoom` | No | Enable zoom action (computer_20251124 only) |

## Optimize model performance with prompting

1. Specify simple, well-defined tasks with explicit instructions
2. Prompt Claude to take screenshots and verify each step
3. Use keyboard shortcuts for tricky UI elements
4. Include example screenshots for repeatable tasks
5. Provide login credentials in xml tags like `<robot_credentials>`

## Computer use limitations

1. Latency may be too slow for real-time interactions
2. Computer vision accuracy may have mistakes or hallucinations
3. Tool selection accuracy may vary with niche applications
4. Scrolling reliability has improved with dedicated scroll actions
5. Spreadsheet interaction has improved with fine-grained mouse controls
6. Account creation on social platforms is limited
7. Vulnerabilities like prompt injection may persist
8. Per terms of service, must not be used to violate laws

## Pricing

System prompt overhead: 466-499 tokens. Computer use tool: 735 tokens per tool definition for Claude 4.x and Sonnet 3.7.
