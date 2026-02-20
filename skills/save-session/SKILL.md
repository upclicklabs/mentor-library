---
name: save-session
description: "Save a session summary so the next session can pick up where you left off. Use when the user says 'save session', 'save my progress', or runs /save-session."
---

# Save Session Memory

Write a concise rolling session summary to `~/.claude/session-memory.md`. This file is read at the start of every future session so Claude knows what happened last time.

## What to write

Overwrite the file completely (don't append). Use this format:

```markdown
# Session Memory
- **Date**: [today's date]
- **Project**: [repo/project name]
- **Branch**: [current git branch if in a repo]

## What was done
- [bullet points of key work completed]

## Key decisions
- [any important choices made and why]

## Open items
- [what's left to do, blockers, next steps]

## Context for next session
- [anything the next session needs to know to pick up smoothly]
```

## Rules

- Max 25-30 lines total — keep it tight
- Focus on what matters for continuity, not exhaustive detail
- Always include the project/repo name so the next session has context
- If multiple projects were worked on, summarize each briefly
- Overwrite each time — this is a rolling summary, not a log
