---
title: "Get started with Claude Code with npm install"
source_url: "https://docs.anthropic.com/en/docs/claude-code/overview"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Get started with Claude Code with npm install

Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser.

## Installation

### Native Install (Recommended)

macOS, Linux, WSL:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell:
```powershell
irm https://claude.ai/install.ps1 | iex
```

Windows CMD:
```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Native installations automatically update in the background to keep you on the latest version.

### Homebrew

```sh
brew install --cask claude-code
```

Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically.

### WinGet

```powershell
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically.

## Quick start

Start Claude Code in any project:

```bash
cd your-project
claude
```

You will be prompted to log in on first use.

## Available environments

### Terminal
The full-featured CLI for working with Claude Code directly in your terminal. Edit files, run commands, and manage your entire project from the command line.

### VS Code
The VS Code extension provides inline diffs, @-mentions, plan review, and conversation history directly in your editor. Search for "Claude Code" in the Extensions view.

### Desktop App
A standalone app for running Claude Code outside your IDE or terminal. Review diffs visually, run multiple sessions side by side, and kick off cloud sessions.

### Web
Run Claude Code in your browser with no local setup. Kick off long-running tasks and check back when they are done. Start coding at claude.ai/code.

### JetBrains
A plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with interactive diff viewing and selection context sharing.

## What you can do

- Automate tedious tasks: writing tests, fixing lint errors, resolving merge conflicts, updating dependencies, writing release notes
- Build features and fix bugs: describe what you want in plain language across multiple files
- Create commits and pull requests: works directly with git
- Connect your tools with MCP: Model Context Protocol for external data sources
- Customize with instructions, skills, and hooks: CLAUDE.md files, custom slash commands, shell hooks
- Run agent teams and build custom agents: spawn multiple agents working simultaneously
- Pipe, script, and automate with the CLI: composable and follows the Unix philosophy

## Next steps

- Quickstart: walk through your first real task
- Best practices and common workflows
- Settings: customize Claude Code for your workflow
- Troubleshooting: solutions for common issues
