# Global Claude Code Instructions

## Session Memory

At the start of every session, read `~/.claude/session-memory.md` if it exists. This file contains a summary of the previous session. Use it to pick up where the last session left off.

Before ending a session (or when the user says "save session" or runs /save-session), write a concise 20-30 line summary to `~/.claude/session-memory.md` — overwrite, don't append. Include: date, project, what was done, key decisions, and open items.
