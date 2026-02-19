---
name: architect-skill
description: Helps structure Claude Code projects by running a discovery session, then designing the correct mix of skills, sub-agents, Claude.md routing rules, MCP tools, and folder structure. Use when planning a new Claude Code workspace, refactoring an existing one, deciding what should be a skill vs sub-agent, or designing a multi-agent workflow. Triggers on "help me plan my Claude Code project", "what should be a skill vs agent", "design my workflow", or "structure my Claude Code setup".
---

# Claude Code Workflow Architect

Runs a structured discovery session, determines the simplest architecture that works, then generates a buildable blueprint — folder structure, Claude.md routing rules, agent definitions, skills list, and implementation checklist.

**Core principle**: Find the simplest solution possible. Only increase complexity when it demonstrably improves outcomes. Many problems are solved with a single LLM call + a well-written skill.

The process:

1. **Discovery** — understand what they're building
2. **Complexity check** — determine simplest viable architecture
3. **Design** — classify components correctly
4. **Blueprint** — generate everything needed to build it
5. **Implementation** — build order with test scenarios

---

## PHASE 1: DISCOVERY SESSION

Before designing anything, run through these questions conversationally. Group 2-3 per turn max. Don't dump all questions at once.

### Round 1: The Big Picture
- **What are you building?** (content pipeline, proposal system, reporting dashboard, etc.)
- **Who is it for?** (yourself, a specific client, multiple clients, a team?)
- **What's the end deliverable?** (documents, dashboards, scheduled posts, code?)

### Round 2: The Workflow
- **Walk me through the steps manually.** How do you do this today? (Where you say "then I..." is usually where an agent boundary lives)
- **What decisions happen along the way?** ("I check if content matches brand voice" = quality gate. "I decide format based on client" = routing logic)
- **What gets reused across projects?** ("I always use the same blog format" = skill)

### Round 3: Tools & Data
- **What external tools/platforms are involved?** (Google Sheets, Notion, Ahrefs, WordPress, GA4 → MCP connections)
- **What files or templates do you already have?** (brand guidelines, templates → context files)
- **Does anything need live/real-time data?** (analytics, rankings → MCP vs static files)

### Round 4: Complexity & Control
- **Is the workflow predictable every time, or does Claude need judgment calls?** (Predictable = workflow. Judgment = agent)
- **Is this one project or reusable across clients?** (project-level vs user-level)
- **How tightly do you need to control each step?** (High/medium/low freedom — see below)
- **Where do you need to review before it continues?** (Human checkpoints, automated validation, full autonomy?)

### Degrees of Freedom
For each task, classify how tightly Claude follows instructions:

- **High freedom**: Multiple approaches valid, context-dependent ("review this for quality")
- **Medium freedom**: Preferred pattern exists, some flexibility ("write a blog using this template")
- **Low freedom**: Must follow exact steps ("run this migration script exactly")

### After Discovery: Summarize Back

```
Here's what I understand:
- Building: [description]
- Deliverables: [list]
- Workflow steps: [numbered list]
- Complexity level: [skills-only / workflow / multi-agent]
- External tools: [list]
- Reusable patterns: [list]
- Validation points: [where checks happen]
- Scale: [one-off / multi-client]
```

Confirm with user before proceeding.

---

## PHASE 1.5: COMPLEXITY CHECK

**Before designing architecture, determine if you even need agents.**

```
CAN A SINGLE LLM CALL + SKILL HANDLE THIS?
  → Single type of work?
  → All steps done by one "person" conceptually?
  → No parallel work needed?
  → No different tool permissions per step?
  → YES TO ALL = Pattern 1: Skills-Only. Stop here.

DO YOU NEED PREDEFINED STEPS IN A FIXED ORDER?
  → Same sequence every time?
  → Each step feeds the next?
  → No dynamic decision-making?
  → YES = Pattern 2: Prompt Chaining. May or may not need sub-agents.

DOES THE INPUT TYPE DETERMINE WHICH HANDLER TO USE?
  → Distinct request categories?
  → Each category needs different tools/skills?
  → YES = Pattern 3: Routing.

DO INDEPENDENT TASKS NEED TO RUN SIMULTANEOUSLY?
  → Multiple outputs combined at the end?
  → Tasks don't depend on each other?
  → YES = Pattern 4: Parallelization.

DOES CLAUDE NEED TO DECIDE DYNAMICALLY WHAT TO DO?
  → Can't predict subtasks in advance?
  → Number of steps depends on input?
  → YES = Pattern 5: Orchestrator-Workers.

DOES OUTPUT NEED ITERATIVE REFINEMENT?
  → Clear evaluation criteria exist?
  → Multiple rounds measurably improve quality?
  → YES = Pattern 6: Evaluator-Optimizer.
```

**Key distinction**: Workflows = predefined code paths. Agents = LLM dynamically directs its own process. Use workflows when predictable, agents when flexible.

If skills-only works, say so directly. Don't build a 5-agent system for a one-skill task.

For detailed pattern descriptions with diagrams: See `references/patterns.md`

---

## PHASE 2: ARCHITECTURE DESIGN

### Decision Framework

```
IS IT KNOWLEDGE OR PROCEDURE?
  → "How to write an AEO blog post", "Brand voice rules"
  → YES = SKILL (.md in /skills/)

IS IT AN INDEPENDENT WORKER WITH ITS OWN TOOLS?
  → "Research using web search", "Pull GA4 data and build dashboard"
  → YES = SUB-AGENT (.md in /agents/)

IS IT A ROUTING DECISION?
  → "Blog requests go to writer, decks go to presentation agent"
  → YES = CLAUDE.MD routing rules

IS IT A LIVE DATA CONNECTION?
  → "Connect to Notion / Ahrefs / GA4"
  → YES = MCP SERVER

IS IT A CHECK/VALIDATION POINT?
  → "Verify schema before publishing", "Check brand voice compliance"
  → YES = FEEDBACK LOOP (script, human gate, or self-eval)
```

### Rules
- **Skills are portable** — multiple agents can load the same skill
- **Sub-agents get isolated context** — only see what you pass them
- **Non-overlapping roles** — two agents handling same request = conflicts
- **Every sub-agent needs**: role, skills it loads, MCP tools, what it returns
- **Claude.md needs explicit routing rules** — no rules = no delegation
- **Fully qualified MCP tool names** — `ServerName:tool_name` format
- **Design tools as carefully as prompts** — clear descriptions, absolute file paths, no ambiguity

### Feedback Loops

For every workflow, design where validation happens:

- **Automated**: Script checks output → pass/fail → retry on fail
- **Human gate**: Workflow pauses for approval before continuing
- **Self-evaluation**: Agent checks own output against criteria, revises if gaps found

---

## PHASE 3: GENERATE THE BLUEPRINT

For templates and examples: See `references/templates.md` and `references/examples.md`

### 3a. Folder Structure
```
project-name/
├── CLAUDE.md              # Routing brain + project context
├── business-context/      # Brand info, client briefs
├── agents/                # Sub-agents (one .md per specialist)
├── skills/                # Reusable instruction manuals
├── scripts/               # Validation/utility scripts
├── templates/             # Output templates agents follow
├── data/                  # Input data, intermediate files
└── output/                # Final deliverables
```

### 3b. Generate for each component:

- **Claude.md** — project context, routing rules, multi-agent workflows, quality gates
- **Agent definitions** — role, responsibilities, skills, MCP tools, output format, constraints, degrees of freedom
- **Skills summary** — name, purpose, which agents use it, exists or needs creating
- **MCP tools** — server name (fully qualified), which agents, purpose, install method
- **Validation steps** — what gets checked, how, what happens on failure

---

## PHASE 4: IMPLEMENTATION CHECKLIST

```
BUILD ORDER:
□ 1. Create project folder + business context files
□ 2. Create CLAUDE.md with project context (NOT routing rules yet)
□ 3. Write 3 test scenarios for end-to-end workflow
□ 4. Install MCP servers (/mcp command in terminal)
□ 5. Install official skills (/plugin command)
□ 6. Create custom skills in /skills/
□ 7. Create validation scripts in /scripts/
□ 8. Create sub-agents via /agents command in terminal
□ 9. Test each agent individually against test scenarios
□ 10. Update CLAUDE.md with routing rules
      (ask Claude to review all agents and generate routes)
□ 11. Test multi-agent workflow end-to-end
□ 12. Iterate based on observed behavior
```

**Critical**:
- Step 3 before building — eval-first approach
- Step 10 after all agents exist — Claude needs to see them all
- Step 12 is ongoing — watch for: unexpected paths, missed references, ignored files, overreliance on certain sections

---

## TONE & APPROACH

- Direct and practical — buildable architecture, not theory
- Reference existing skills when relevant (check user's /skills/ folder)
- Justify every classification — explain WHY something is a skill vs agent
- Default to simplest architecture that works
- Listen for task boundaries — "then I..." = potential agent boundary
- Spend as much effort on tool interface design as on prompts
