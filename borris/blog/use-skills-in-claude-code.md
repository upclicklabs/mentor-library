---
title: "Use Skills in Claude Code"
source_url: "https://docs.claude.com/en/docs/claude-code/skills"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use Skills in Claude Code

Skills extend what Claude can do. Create a SKILL.md file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with /skill-name.

Claude Code skills follow the Agent Skills open standard, which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control, subagent execution, and dynamic context injection.

## Getting started

### Create your first skill

This example creates a skill that teaches Claude to explain code using visual diagrams and analogies.

1. Create the skill directory:
```bash
mkdir -p ~/.claude/skills/explain-code
```

2. Write SKILL.md at `~/.claude/skills/explain-code/SKILL.md`:
```yaml
---
name: explain-code
description: Explains code with visual diagrams and analogies. Use when explaining how code works.
---

When explaining code, always include:

1. **Start with an analogy**: Compare the code to something from everyday life
2. **Draw a diagram**: Use ASCII art to show the flow, structure, or relationships
3. **Walk through the code**: Explain step-by-step what happens
4. **Highlight a gotcha**: What's a common mistake or misconception?
```

3. Test the skill by asking "How does this code work?" or invoke directly with `/explain-code src/auth/login.ts`

### Where skills live

| Location | Path | Applies to |
|---|---|---|
| Enterprise | Managed settings | All users in your organization |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Where plugin is enabled |

When skills share the same name across levels, higher-priority locations win: enterprise > personal > project.

### Skill directory structure

```
my-skill/
  SKILL.md           # Main instructions (required)
  template.md        # Template for Claude to fill in
  examples/
    sample.md        # Example output showing expected format
  scripts/
    validate.sh      # Script Claude can execute
```

## Configure skills

### Types of skill content

**Reference content** adds knowledge Claude applies to your current work. Conventions, patterns, style guides, domain knowledge.

```yaml
---
name: api-conventions
description: API design patterns for this codebase
---

When writing API endpoints:
- Use RESTful naming conventions
- Return consistent error formats
- Include request validation
```

**Task content** gives Claude step-by-step instructions for a specific action.

```yaml
---
name: deploy
description: Deploy the application to production
context: fork
disable-model-invocation: true
---

Deploy the application:
1. Run the test suite
2. Build the application
3. Push to the deployment target
```

### Frontmatter reference

| Field | Required | Description |
|---|---|---|
| name | No | Display name for the skill. If omitted, uses directory name |
| description | Recommended | What the skill does and when to use it |
| argument-hint | No | Hint shown during autocomplete |
| disable-model-invocation | No | Set to true to prevent Claude from auto-loading. Default: false |
| user-invocable | No | Set to false to hide from / menu. Default: true |
| allowed-tools | No | Tools Claude can use without asking permission |
| model | No | Model to use when this skill is active |
| context | No | Set to fork to run in a forked subagent context |
| agent | No | Which subagent type to use when context: fork is set |
| hooks | No | Hooks scoped to this skill's lifecycle |

### String substitutions

| Variable | Description |
|---|---|
| $ARGUMENTS | All arguments passed when invoking the skill |
| $ARGUMENTS[N] | Access a specific argument by 0-based index |
| $N | Shorthand for $ARGUMENTS[N] |
| ${CLAUDE_SESSION_ID} | The current session ID |

### Control who invokes a skill

- **disable-model-invocation: true**: Only you can invoke the skill. Use for workflows with side effects like /commit, /deploy
- **user-invocable: false**: Only Claude can invoke the skill. Use for background knowledge

### Pass arguments to skills

```yaml
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---

Fix GitHub issue $ARGUMENTS following our coding standards.

1. Read the issue description
2. Understand the requirements
3. Implement the fix
4. Write tests
5. Create a commit
```

Run with: `/fix-issue 123`

## Advanced patterns

### Inject dynamic context

The `!`command`` syntax runs shell commands before the skill content is sent to Claude:

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

## Your task
Summarize this pull request...
```

### Run skills in a subagent

Add `context: fork` to your frontmatter when you want a skill to run in isolation:

```yaml
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:

1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file references
```

### Restrict tool access

```yaml
---
name: safe-reader
description: Read files without making changes
allowed-tools: Read, Grep, Glob
---
```

## Share skills

Skills can be distributed at different scopes:
- **Project skills**: Commit `.claude/skills/` to version control
- **Plugins**: Create a `skills/` directory in your plugin
- **Managed**: Deploy organization-wide through managed settings

## Troubleshooting

### Skill not triggering
1. Check the description includes keywords users would naturally say
2. Verify the skill appears in "What skills are available?"
3. Try rephrasing your request to match the description
4. Invoke it directly with /skill-name

### Skill triggers too often
1. Make the description more specific
2. Add `disable-model-invocation: true` for manual-only invocation

### Claude doesn't see all my skills
Skill descriptions are loaded into context. If you have many skills, they may exceed the character budget (2% of context window, fallback 16,000 characters). Run `/context` to check. Override with `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable.
