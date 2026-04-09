# Obsidian Second Brain — Notes from Borris Mentor Research

## What is Obsidian?

A note-taking app that stores everything as plain markdown files in a folder on your computer. No cloud database, no proprietary format. You own your notes as `.md` files.

## What is a Wiki?

A folder of compiled, organized notes that Claude automatically creates by reading your raw content and distilling it into clean, linked pages — so it reads one summary instead of scanning hundreds of files every time.

## How "Ingest" Works

1. You drop a file (transcript, article, notes) into `raw/` or a content folder
2. You tell Claude: "Ingest this"
3. Claude reads it, pulls out key knowledge, creates organized wiki pages with links between related concepts
4. Updates `index.md` (master table of contents)

From one transcript, you might get 10-20+ organized, linked wiki pages — automatically.

## Hot Cache (`hot.md`)

A small file (~500 words) holding the most recent context — like a sticky note on your monitor. Claude reads this first so it doesn't have to dig through everything for simple, recent questions.

---

## Two Approaches (from Borris's Sources)

### Ben's Approach (Business AI OS)

Team/business-oriented with a rich folder structure:

- `context/` — Who you are, strategy, brand, ICP, stakeholders
- `daily/` — Auto-logged daily activity (most important folder)
- `departments/` — SOPs for each department
- `intelligence/` — Meeting transcripts, decisions, competitor research
- `onboarding/` — SOPs for new team members/clients
- `projects/` — Active work
- `resources/` — Reusable prompts, templates, frameworks
- `skills/` — Reference material that skills point to
- `tasks/` — To-do lists
- `teams/` — Each team member's role
- `CLAUDE.md` — Navigation instruction layer

Key ideas:
- Skills point to the vault instead of embedding duplicate reference files
- AI updates the vault itself — "remember this in my second brain"
- Start simple (even 5 files), let it grow
- Context compounds — after 6 months, AI is far more powerful than day one

### Nate Herk's Approach (Karpathy LLM Wiki)

Knowledge-system oriented, based on Andrej Karpathy's LLM wiki concept:

```
my-wiki/
  raw/          # Source docs (articles, transcripts, PDFs)
  wiki/
    index.md    # Master index
    log.md      # Operation history
    sources/
    concepts/
    entities/
    analysis/
  CLAUDE.md     # Navigation instructions
```

Key ideas:
- The LLM does all the heavy lifting — drop content in raw/, say "ingest it"
- Hot cache pattern — `hot.md` for recent context
- CLAUDE.md lookup order: hot cache → index → domain subindex → search wiki
- Graph view shows relationships in real time
- Linting — periodic health checks
- 95% token reduction vs raw files
- Wiki beats RAG at small scale

---

## Does Obsidian Make Things Global?

No. Obsidian is just a visual app. You still need to tell Claude Code where the vault is.

Ways to connect:
1. Open Claude Code directly in the vault folder
2. Reference the vault path from other project's `CLAUDE.md`
3. Put the vault path in global `~/.claude/CLAUDE.md` for all sessions

---

## How Mentor-Library Already Works Like Obsidian

The mentor-library is already a markdown knowledge base with global skills. The mentors are callable from any conversation, any repo, any folder. They read from shared content and cite sources.

**What's missing:** A `wiki/` layer (compiled knowledge), `context/` (shared business context), `daily/` logs, and `hot.md`.

---

## UpclickLabs Repos (9 total)

| Repo | Purpose |
|---|---|
| mentor-library | AI mentor assistants from transcripts |
| circadianrest | AEO content pipeline for Circadian REST client |
| leadgen | Lead generation |
| ai-visibility-snapshot | Branded PDF reports — AI visibility |
| AEO-questioncluster-strategy | Question clustering for AEO |
| universal-content-creator | AEO content for all clients |
| upclick-website | Company website |
| shopify-offer | Shopify offer tool |
| web-designer | Web designer |

**Problem:** These are all isolated. Each repo starts from zero — no shared context, no shared knowledge.

---

## Proposed UpClick Brain Structure

```
upclick-brain/
  CLAUDE.md                    # Navigation for all departments
  hot.md                       # What's happening right now

  context/                     # Shared across everything
    me.md
    upclick-labs.md            # ICP, pricing, verticals
    brand.md                   # Tone of voice, style
    writing-preferences.md

  mentors/                     # Shared across everything
    hormozi/
    ethan/
    chris/
    nick/
    borris/

  leadgen/                     # Cold email + LinkedIn outreach
    pipeline.md
    cold-emails/
      templates/
      campaigns/
    linkedin-outreach/
      templates/
      campaigns/
    call-transcripts/
    reports/

  marketing/                   # Social media + website
    linkedin/
      drafts/
      published/
      ideas.md
    social/
    website/
    voice-notes/
    content-calendar.md

  clients/
    _template/
      overview.md
      work-log.md
      comms/
      reports/
      CLAUDE.md
    circadian-rest/
      overview.md
      work-log.md
      comms/
      content-pipeline/
        pipeline-config.md
        articles/
        queue.md
      reddit/
        strategy.md
        engagement-log.md
      reports/
      CLAUDE.md
    client-2/
      ...

  daily/
  wiki/
    index.md
```

### Root CLAUDE.md

```markdown
# UpClick Brain

## Shared context (always available)
- Me: context/me.md
- Business & ICP: context/upclick-labs.md
- Brand & tone: context/brand.md
- Mentor knowledge: mentors/

## Departments
- Lead gen (cold email + LinkedIn outreach): leadgen/
- Marketing (social media + website): marketing/
- Client work: clients/[name]/

## Rules
- All departments can read context/ and mentors/
- Cold emails pull from Nick + Hormozi frameworks
- LinkedIn outreach pulls from Chris frameworks
- Marketing content pulls from Chris + Ethan + brand.md
- Client work pulls from Ethan + relevant client folder
```

---

## Client Folder System

### Simple client (new sign)
```
clients/client-name/
  overview.md
  work-log.md
  comms/              # Flat — date-sorted, prefix by type
    2026-04-05-call-kickoff.md
    2026-04-07-email-revision-request.md
  reports/
  CLAUDE.md
```

### Full operation client (Circadian REST)
```
clients/circadian-rest/
  overview.md
  work-log.md
  comms/
  content-pipeline/
    pipeline-config.md
    articles/
    queue.md
  reddit/
    strategy.md
    engagement-log.md
  reports/
  CLAUDE.md
```

### Comms — keep flat
Date-first filenames: `2026-04-09-call-weekly-checkin.md`, `2026-04-09-email-homepage-feedback.md`. Don't split into subfolders unless 50+ files.

### Work log
After each day, say: "Update work log for [client] — [what you did]"

Claude appends with date stamp. End of week: "Show me work history and draft Upwork message."

---

## Two Brains

Can run two separate vaults (upclick-brain + smartcrew-brain) for full isolation, or one vault with two sections. Separate is better if you don't want a future team seeing personal side projects.

Global `~/.claude/CLAUDE.md` points to both:
```markdown
Business brain: ~/upclick-brain/
Personal brain: ~/smartcrew-brain/
```

---

## Morning Briefing Skill (Future)

Connects three layers:
1. **Obsidian vault** — files (ready now)
2. **Google Calendar MCP** — meetings (needs setup)
3. **Gmail MCP** — emails (needs setup)

One skill reads all three and outputs: today's meetings, follow-ups needed, client work due, content due, suggested schedule.

---

## Key Principles

- Start simple (5 files), let it grow naturally
- Don't overoptimize structure on day one
- CLAUDE.md is the bridge — tells AI how to navigate
- Context compounds — every logged decision, call, and correction makes the system smarter
- Markdown is the oxygen of LLMs — works across Claude Code, Cowork, any AI agent
- The mentor-library is the raw knowledge. The wiki is the compiled layer on top.
- Save work to Obsidian by saying "update work log" or "save this to [folder]"
- For emails: drop files in or paste and say "save to comms" (Gmail MCP for full automation later)
