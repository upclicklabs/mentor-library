# Templates

Copy and customise these when generating blueprints.

---

## Claude.md Template

```markdown
# [Project Name]

## Project Context
[One paragraph: what this workspace does, who it serves]

## Business Context
[Brief key info. Link to business-context/ files for details]

## Agent Routing Rules

### [Agent Name]
- **Trigger**: [specific phrases/request types]
- **Delegates to**: @agent-name
- **Skills loaded**: [skill-1], [skill-2]
- **MCP tools**: [ServerName:tool_name]
- **Returns**: [what agent hands back]

## Multi-Agent Workflows

### [Workflow Name]
1. @agent-1 does [task] → produces [output]
2. **Gate**: [validation — script/human/self-eval]
3. @agent-2 uses [step 1 output] → produces [output]
4. **Gate**: [validation]
5. @agent-3 compiles all → [final deliverable]

## Quality Gates
- **Automated**: [scripts, when they run]
- **Human review**: [what needs approval, at which step]
- **Self-evaluation**: [what Claude checks, revision criteria]
```

---

## Agent Definition Template

One .md file per agent in /agents/.

```markdown
# [Agent Name]

## Role
[One sentence: what it does, when it's called]

## Responsibilities
- [Task 1]
- [Task 2]

## Skills
- /skills/[name]/SKILL.md — for [purpose]

## MCP Tools
- ServerName:tool_name — for [purpose]

## Input
[What it receives from main agent or previous step]

## Output Format
[What it returns — format, structure, where saved]

## Validation
- Script: `python scripts/validate_[x].py output_file`
- Self-check: [criteria]

## Constraints
- [What it must NOT do]
- [Role boundaries]

## Degrees of Freedom
[High/Medium/Low + justification]
```

---

## Test Scenarios Template

Create 3 BEFORE building (eval-first):

```
Test 1: [Simple case]
- Input: "[user request]"
- Expected flow: [which agents/skills activate]
- Expected output: [deliverable description]
- Pass criteria: [specific checks]

Test 2: [Typical case]
- Input: "[request]"
- Expected flow: [agents/skills]
- Expected output: [deliverable]
- Pass criteria: [checks]

Test 3: [Edge case / complex multi-agent]
- Input: "[request]"
- Expected flow: [full chain]
- Expected output: [deliverable]
- Pass criteria: [checks]
```
