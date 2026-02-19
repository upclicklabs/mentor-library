---
title: "Explore Anthropic's Claude Code documentation"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Explore Anthropic's Claude Code documentation

Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser.

Claude Code is an AI-powered coding assistant that helps you build features, fix bugs, and automate development tasks. It understands your entire codebase and can work across multiple files and tools to get things done.

## Get started

Choose your environment to get started. Most surfaces require a Claude subscription or Anthropic Console account.

### Installation options

#### Terminal (Native Install - Recommended)

macOS, Linux, WSL:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell:
```powershell
irm https://claude.ai/install.ps1 | iex
```

Then start Claude Code in any project:
```bash
cd your-project
claude
```

#### Homebrew
```sh
brew install --cask claude-code
```

#### WinGet
```powershell
winget install Anthropic.ClaudeCode
```

#### VS Code
Search for "Claude Code" in the Extensions view (Cmd+Shift+X on Mac, Ctrl+Shift+X on Windows/Linux).

#### Desktop App
Download from claude.ai for macOS, Windows (x64), or Windows ARM64.

#### Web
Start coding at claude.ai/code with no local setup required.

#### JetBrains
Install the Claude Code plugin from the JetBrains Marketplace.

## Key capabilities

- **Automate tedious tasks**: Writing tests, fixing lint errors, resolving merge conflicts, updating dependencies, writing release notes
- **Build features and fix bugs**: Describe what you want in plain language across multiple files
- **Create commits and pull requests**: Works directly with git for staging, commits, branches, and PRs
- **Connect tools with MCP**: Model Context Protocol connects to Google Drive, Jira, Slack, and custom tooling
- **Customize with instructions, skills, and hooks**: CLAUDE.md files, custom slash commands, and shell command hooks
- **Run agent teams**: Spawn multiple agents working on different parts simultaneously
- **Pipe, script, and automate**: Composable CLI following the Unix philosophy

## Use Claude Code everywhere

Each surface connects to the same underlying Claude Code engine, so your CLAUDE.md files, settings, and MCP servers work across all of them.

| Use case | Best option |
|---|---|
| Start a task locally, continue on mobile | Web or Claude iOS app |
| Automate PR reviews and issue triage | GitHub Actions or GitLab CI/CD |
| Route bug reports from Slack to pull requests | Slack |
| Debug live web applications | Chrome |
| Build custom agents for your own workflows | Agent SDK |

## Next steps

- Quickstart: Walk through your first real task
- Best practices and common workflows
- Settings: Customize Claude Code for your workflow
- Troubleshooting: Solutions for common issues
- code.claude.com: Demos, pricing, and product details
