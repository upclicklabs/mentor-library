---
title: "Claude Code IDE Integrations"
source_url: "https://docs.anthropic.com/en/docs/claude-code/ide-integrations"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Claude Code IDE Integrations

The VS Code extension provides a native graphical interface for Claude Code, integrated directly into your IDE. This is the recommended way to use Claude Code in VS Code.

With the extension, you can review and edit Claude's plans before accepting them, auto-accept edits as they're made, @-mention files with specific line ranges from your selection, access conversation history, and open multiple conversations in separate tabs or windows.

## Prerequisites

- VS Code 1.98.0 or higher
- An Anthropic account (you'll sign in when you first open the extension)

The extension includes the CLI (command-line interface), which you can access from VS Code's integrated terminal for advanced features.

## Install the Extension

In VS Code, press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux) to open the Extensions view, search for "Claude Code", and click Install.

## Get Started

### Open the Claude Code Panel

The Spark icon indicates Claude Code throughout VS Code. Click it in the Editor Toolbar (top-right corner) when you have a file open.

Other ways to open:
- **Command Palette**: `Cmd+Shift+P` / `Ctrl+Shift+P`, type "Claude Code"
- **Status Bar**: Click "Claude Code" in the bottom-right corner

### Send a Prompt

Ask Claude to help with your code or files. Claude automatically sees your selected text. Press `Option+K` (Mac) / `Alt+K` (Windows/Linux) to insert an @-mention reference.

### Review Changes

When Claude wants to edit a file, it shows a side-by-side comparison of the original and proposed changes, then asks for permission. You can accept, reject, or tell Claude what to do instead.

## Use the Prompt Box

- **Permission modes**: Normal mode (asks permission), Plan mode (describes first), Auto-accept mode (edits without asking)
- **Command menu**: Click `/` to open commands for attaching files, switching models, toggling extended thinking
- **Context indicator**: Shows how much of Claude's context window you're using
- **Extended thinking**: Lets Claude spend more time reasoning through complex problems
- **Multi-line input**: Press `Shift+Enter` to add a new line

### Reference Files and Folders

Use @-mentions to give Claude context about specific files or folders. Claude Code supports fuzzy matching.

### Resume Past Conversations

Click the dropdown at the top of the Claude Code panel to access conversation history.

## Customize Your Workflow

### Choose Where Claude Lives

Drag the Claude panel to reposition it: Secondary sidebar, Primary sidebar, or Editor area.

### Run Multiple Conversations

Use "Open in New Tab" or "Open in New Window" from the Command Palette.

### Switch to Terminal Mode

Enable "Use Terminal" in VS Code settings under Extensions > Claude Code.

## Manage Plugins

Type `/plugins` in the prompt box to open the Manage plugins interface. Install plugins at user scope, project scope, or local scope.

## Automate Browser Tasks with Chrome

Connect Claude to your Chrome browser to test web apps, debug with console logs, and automate browser workflows. Type `@browser` in the prompt box followed by what you want Claude to do.

## VS Code Commands and Shortcuts

| Command | Shortcut | Description |
|---------|----------|-------------|
| Focus Input | `Cmd+Esc` / `Ctrl+Esc` | Toggle focus between editor and Claude |
| Open in New Tab | `Cmd+Shift+Esc` / `Ctrl+Shift+Esc` | Open new conversation as editor tab |
| New Conversation | `Cmd+N` / `Ctrl+N` | Start new conversation (Claude focused) |
| Insert @-Mention | `Option+K` / `Alt+K` | Insert reference to current file and selection |

## VS Code Extension vs. Claude Code CLI

Some features are only available in the CLI. The extension and CLI share the same conversation history. To continue an extension conversation in the CLI, run `claude --resume` in the terminal.

### Rewind with Checkpoints

The extension supports checkpoints for tracking Claude's file edits. Hover over any message to reveal the rewind button with options: Fork conversation, Rewind code, or Fork and rewind.

## Configure Settings

- **Extension settings**: Control the extension's behavior within VS Code
- **Claude Code settings** in `~/.claude/settings.json`: Shared between extension and CLI

## Use Third-Party Providers

If your organization uses Amazon Bedrock, Google Vertex AI, or Microsoft Foundry:
1. Disable login prompt in VS Code settings
2. Follow the setup guide for your provider
