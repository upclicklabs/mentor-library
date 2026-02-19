# Architecture Examples

Real-world examples at different complexity levels.

---

## Example 1: Skills-Only (Pattern 1)

**Task**: Write a single client blog post.
**Why no agents**: Single task type, no parallel work, no different permissions.

```
project/
├── CLAUDE.md
├── business-context/
│   └── client-brief.md
├── skills/
│   ├── aeo-listicle-writer/SKILL.md
│   └── aeo-entity-master/SKILL.md
└── output/
```

Claude.md loads the right skill based on content type. No agents needed.

---

## Example 2: Prompt Chaining (Pattern 2)

**Task**: Full AEO content pipeline — research, write, generate schema.
**Why chaining**: Steps are sequential and dependent. Research must finish before writing.

```
project/
├── CLAUDE.md
├── business-context/
├── agents/
│   ├── content-researcher.md
│   ├── aeo-content-writer.md
│   └── schema-generator.md
├── skills/
│   ├── listicle-writer/SKILL.md
│   ├── comparison-writer/SKILL.md
│   └── aeo-entity-master/SKILL.md
├── scripts/
│   ├── validate_schema.py
│   └── check_aeo_score.py
└── output/
```

**Claude.md workflow**:
1. @content-researcher → content brief
2. GATE: Human reviews brief
3. @aeo-content-writer → article (loads listicle skill)
4. GATE: check_aeo_score.py → must pass 80%+
5. @schema-generator → JSON-LD (loads entity-master skill)
6. GATE: validate_schema.py → must pass

---

## Example 3: Routing (Pattern 3)

**Task**: Upwork proposal system — different flows for analysis, writing, demos.
**Why routing**: Distinct request types need different agents and skills.

```
project/
├── CLAUDE.md
├── agents/
│   ├── job-analyzer.md
│   ├── proposal-writer.md
│   └── demo-builder.md
├── skills/
│   ├── summary-skill/SKILL.md
│   ├── proposal-assistant/SKILL.md
│   └── n8n-workflow-architect/SKILL.md
└── output/
```

**Claude.md routing**:
- "Analyze this job" → @job-analyzer
- "Write proposal" → @proposal-writer
- "Build demo" → @demo-builder
- "Full proposal package" → all three in sequence

---

## Anti-Pattern: Over-Engineered Simple Task

**DON'T** create 7 agents for one blog post:

```
agents/
  ├── topic-brainstormer.md
  ├── outline-creator.md
  ├── intro-writer.md
  ├── body-writer.md
  ├── conclusion-writer.md
  ├── editor.md
  └── publisher.md
```

**DO**: One skill loaded by main agent. Done.
