---
title: "Use MCP with Claude Code"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use MCP with Claude Code

This page covers practical workflows for everyday development with Claude Code, including exploring unfamiliar code, debugging, refactoring, writing tests, creating PRs, and managing sessions.

## Key Workflows

### Understand New Codebases

- Navigate to the project root directory and start Claude Code
- Ask for a high-level overview, then dive deeper into specific components
- Start with broad questions, then narrow down to specific areas

### Fix Bugs Efficiently

- Share the error with Claude
- Ask for fix recommendations
- Apply the fix

### Refactor Code

- Identify legacy code for refactoring
- Get refactoring recommendations
- Apply the changes safely
- Verify the refactoring

### Use Specialized Subagents

- View available subagents with `/agents`
- Claude Code automatically delegates appropriate tasks to specialized subagents
- Create custom subagents for your workflow in `.claude/agents/`

### Use Plan Mode for Safe Code Analysis

Plan Mode instructs Claude to create a plan by analyzing the codebase with read-only operations, perfect for exploring codebases, planning complex changes, or reviewing code safely.

- Toggle Plan Mode during a session using Shift+Tab
- Start a new session in Plan Mode: `claude --permission-mode plan`

### Work with Tests

- Identify untested code
- Generate test scaffolding
- Add meaningful test cases
- Run and verify tests

### Create Pull Requests

- Use `/commit-push-pr` skill for one-step commit, push, and PR creation
- Or guide Claude through the process step-by-step

### Reference Files and Directories

Use `@` to quickly include files or directories without waiting for Claude to read them:
- `@src/utils/auth.js` - reference a single file
- `@src/components` - reference a directory

### Use Extended Thinking

Extended thinking is enabled by default, giving Claude space to reason through complex problems step-by-step before responding.

### Resume Previous Conversations

- `claude --continue` continues the most recent conversation
- `claude --resume` opens a conversation picker or resumes by name
- `claude --from-pr 123` resumes sessions linked to a specific pull request

### Run Parallel Sessions with Git Worktrees

Git worktrees allow you to check out multiple branches from the same repository into separate directories, enabling parallel Claude Code sessions with complete code isolation.

### Use Claude as a Unix-style Utility

- Pipe data through Claude: `cat build-error.txt | claude -p 'explain this error' > output.txt`
- Control output format with `--output-format text`, `json`, or `stream-json`
