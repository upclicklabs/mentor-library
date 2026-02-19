---
title: "Browse Anthropic's Claude Code common workflows"
source_url: "https://docs.claude.com/en/docs/claude-code/common-workflows"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Browse Anthropic's Claude Code common workflows

Step-by-step guides for exploring codebases, fixing bugs, refactoring, testing, and other everyday tasks with Claude Code.

This page covers practical workflows for everyday development: exploring unfamiliar code, debugging, refactoring, writing tests, creating PRs, and managing sessions.

## Understand new codebases

### Get a quick codebase overview

1. Navigate to the project root directory: `cd /path/to/project`
2. Start Claude Code: `claude`
3. Ask for a high-level overview: `give me an overview of this codebase`
4. Dive deeper into specific components:
   - `explain the main architecture patterns used here`
   - `what are the key data models?`
   - `how is authentication handled?`

Tips: Start with broad questions, then narrow down to specific areas. Ask about coding conventions and patterns used in the project.

### Find relevant code

1. Ask Claude to find relevant files: `find the files that handle user authentication`
2. Get context on how components interact: `how do these authentication files work together?`
3. Understand the execution flow: `trace the login process from front-end to database`

## Fix bugs efficiently

1. Share the error with Claude: `I'm seeing an error when I run npm test`
2. Ask for fix recommendations: `suggest a few ways to fix the @ts-ignore in user.ts`
3. Apply the fix: `update user.ts to add the null check you suggested`

Tips: Tell Claude the command to reproduce the issue and get a stack trace. Mention any steps to reproduce the error.

## Refactor code

1. Identify legacy code for refactoring: `find deprecated API usage in our codebase`
2. Get refactoring recommendations: `suggest how to refactor utils.js to use modern JavaScript features`
3. Apply the changes safely: `refactor utils.js to use ES2024 features while maintaining the same behavior`
4. Verify the refactoring: `run tests for the refactored code`

## Use specialized subagents

1. View available subagents: `/agents`
2. Use subagents automatically - Claude Code automatically delegates appropriate tasks
3. Explicitly request specific subagents: `use the code-reviewer subagent to check the auth module`
4. Create custom subagents for your workflow via `/agents` then "Create New subagent"

## Use Plan Mode for safe code analysis

Plan Mode instructs Claude to create a plan by analyzing the codebase with read-only operations, perfect for exploring codebases, planning complex changes, or reviewing code safely.

### When to use Plan Mode

- Multi-step implementation: When your feature requires making edits to many files
- Code exploration: When you want to research the codebase thoroughly before changing anything
- Interactive development: When you want to iterate on the direction with Claude

### How to use Plan Mode

- Switch during a session using Shift+Tab to cycle through permission modes
- Start a new session in Plan Mode: `claude --permission-mode plan`
- Run headless queries in Plan Mode: `claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"`

## Work with tests

1. Identify untested code: `find functions in NotificationsService.swift that are not covered by tests`
2. Generate test scaffolding: `add tests for the notification service`
3. Add meaningful test cases: `add test cases for edge conditions in the notification service`
4. Run and verify tests: `run the new tests and fix any failures`

## Create pull requests

Use the `/commit-push-pr` skill which commits, pushes, and opens a PR in one step, or guide Claude through it step-by-step:

1. Summarize your changes: `summarize the changes I've made to the authentication module`
2. Generate a pull request: `create a pr`
3. Review and refine: `enhance the PR description with more context about the security improvements`

## Handle documentation

1. Identify undocumented code: `find functions without proper JSDoc comments in the auth module`
2. Generate documentation: `add JSDoc comments to the undocumented functions in auth.js`
3. Review and enhance: `improve the generated documentation with more context and examples`

## Work with images

Methods to add images to the conversation:
1. Drag and drop an image into the Claude Code window
2. Copy an image and paste it into the CLI with ctrl+v
3. Provide an image path: "Analyze this image: /path/to/your/image.png"

## Reference files and directories

Use @ to quickly include files or directories without waiting for Claude to read them:
- Reference a single file: `Explain the logic in @src/utils/auth.js`
- Reference a directory: `What's the structure of @src/components?`
- Reference MCP resources: `Show me the data from @github:repos/owner/repo/issues`

## Use extended thinking (thinking mode)

Extended thinking is enabled by default, giving Claude space to reason through complex problems step-by-step before responding. This reasoning is visible in verbose mode (toggle with Ctrl+O).

Configure thinking mode:
- Adjust effort level in `/model` or set `CLAUDE_CODE_EFFORT_LEVEL`
- Toggle shortcut: Option+T (macOS) or Alt+T (Windows/Linux)
- Global default via `/config`
- Limit token budget with `MAX_THINKING_TOKENS` environment variable

## Resume previous conversations

- `claude --continue` continues the most recent conversation in the current directory
- `claude --resume` opens a conversation picker or resumes by name
- `claude --from-pr 123` resumes sessions linked to a specific pull request

### Name your sessions

Use `/rename` during a session to give it a memorable name: `/rename auth-refactor`

Then resume by name later: `claude --resume auth-refactor`

## Run parallel Claude Code sessions with Git worktrees

Git worktrees allow you to check out multiple branches from the same repository into separate directories.

```bash
# Create a new worktree with a new branch
git worktree add ../project-feature-a -b feature-a

# Run Claude Code in this isolated environment
cd ../project-feature-a
claude
```

## Use Claude as a unix-style utility

### Add Claude to your verification process

```json
{
    "scripts": {
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos.'"
    }
}
```

### Pipe in, pipe out

```bash
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

### Control output format

- `--output-format text` for simple integrations (default)
- `--output-format json` for full conversation log
- `--output-format stream-json` for real-time output of each conversation turn
