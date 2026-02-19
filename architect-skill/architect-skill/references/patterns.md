# Architecture Patterns

6 patterns ranked simplest to most complex. Start at 1, only move up when justified.

---

## Pattern 1: Skills-Only

Main agent loads skills directly. No delegation.

```
User request → Main Agent loads skill → Executes → Output
```

**Use when**: Single type of work, no parallel tasks, no different tool permissions per step.

**Example**: "Write an AEO blog post" — load listicle-writer skill, write it, done.

**Test**: If you're creating agents that each do 5 minutes of work, they should be steps in one skill, not separate agents.

---

## Pattern 2: Prompt Chaining

Fixed sequential steps. Each LLM call processes the previous output. Add gates between steps.

```
User request → Step 1 → [Gate] → Step 2 → [Gate] → Step 3 → Output
```

**Use when**: Task cleanly decomposes into fixed subtasks. Trading latency for accuracy.

**Example**: Research topic → [review brief] → Write article → [validate schema] → Generate JSON-LD → Publish

**Key feature**: Gates between steps — a script, human review, or simple check.

---

## Pattern 3: Routing

Classifies input and directs to specialized handler. Each handler has own tools and skills.

```
User request → Classifier →
  ├── Category A → Specialist A
  ├── Category B → Specialist B
  └── Category C → Specialist C
```

**Use when**: Distinct request types needing different handling. Optimizing one path shouldn't hurt another.

**Example**: "Write blog" → @content-writer | "Build deck" → @presentation-specialist | "Analyze traffic" → @data-analyst

**Key feature**: Non-overlapping categories. Ambiguous classifier = failed routing.

---

## Pattern 4: Parallelization

Multiple agents work simultaneously on independent parts. Results aggregated.

Two variations:
- **Sectioning**: Different subtasks in parallel
- **Voting**: Same task multiple times for confidence

```
User request → Main Agent splits:
  ├── Agent A (content)  ──┐
  ├── Agent B (schema)   ──┤→ Main Agent combines → Output
  └── Agent C (visuals)  ──┘
```

**Use when**: Independent tasks that benefit from simultaneous execution. Multiple perspectives improve quality.

---

## Pattern 5: Orchestrator-Workers

Central LLM dynamically breaks down tasks and delegates. Subtasks not predefined — determined by input.

```
User request → Orchestrator analyzes →
  Creates subtasks dynamically →
  Delegates to workers →
  Synthesizes → Output
```

**Use when**: Can't predict subtasks in advance. Number and nature of steps depends on input.

**Example**: "Update all client content for Q2" — orchestrator scans what exists, determines what needs updating, assigns workers with correct client-specific skills.

---

## Pattern 6: Evaluator-Optimizer

One agent generates, another evaluates. Loops until quality threshold met.

```
User request → Generator → Output →
  Evaluator reviews →
    ├── Pass → Final output
    └── Fail → Feedback → Generator revises → [loop]
```

**Use when**: Clear evaluation criteria. Iterative refinement measurably improves output.

**Example**: Writer drafts article → Evaluator checks AEO score + brand voice → sends revision notes → Writer revises → re-evaluate.

---

## Combining Patterns

Common combos:
- **Routing + Chaining**: Route to specialist, then chain through their subtasks
- **Chaining + Evaluator**: Pipeline with eval loops at quality-critical steps
- **Orchestrator + Parallelization**: Orchestrator identifies tasks, workers execute in parallel

**Rule**: Combining 3+ patterns = probably over-engineering. Step back.
