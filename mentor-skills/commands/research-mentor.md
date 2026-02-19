---
description: Find and curate mentor content on a topic — search YouTube, blogs, and podcasts, then save approved URLs to Notion
argument-hint: "<mentor> <topic>"
---

# Research Mentor

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Search for high-quality content from a mentor and add approved URLs to the Notion database.

## Trigger

User runs `/research-mentor` or asks to find, research, or discover content for a mentor.

## Inputs

1. **Mentor** — one of: Hormozi, Ethan, Chris, Borris
2. **Topic** — the subject to search for

If no mentor specified, ask. If no topic specified, ask.

## Mentors

| Mentor | Focus Areas | Search Sources |
|--------|-------------|----------------|
| **Hormozi** | Offers, lead gen, business growth | YouTube, acquisition.com, podcasts |
| **Ethan** | AEO, answer engine optimization | YouTube, blogs, industry articles |
| **Chris** | LinkedIn strategy, content | YouTube, LinkedIn posts, blogs |
| **Borris** | Prompting, AI workflows, MCP | YouTube, Anthropic docs, blogs |

## Notion API Strategy

**Try Notion MCP tools first.** If MCP fails (Zod validation errors, serialization errors, or any tool-level error), **fall back to curl** using the commands below. Do not ask the user — just switch to curl silently and continue.

## Notion Database
- **Database ID:** `3026ed85-e90a-814d-96e8-e35f0b8fae89`

## Process

### 1. Search for Content

Search the web with these query patterns:

For YouTube:
- `"{Mentor full name}" {topic} site:youtube.com`

For blogs/articles:
- `"{Mentor full name}" {topic}` (general web)
- `"{Mentor full name}" {topic} site:{mentor-specific-site}`

Mentor-specific sites:
- Hormozi -> `acquisition.com`
- Ethan -> relevant AEO/SEO blogs
- Chris -> `linkedin.com`
- Borris -> `anthropic.com`, `docs.anthropic.com`

### 2. Present Results for Approval

Show findings in this format:

```
## Research Results: [Mentor] — [Topic]

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | [Title] | YouTube | [link] |
| 2 | [Title] | Blog | [link] |
| 3 | [Title] | Podcast | [link] |

Reply with:
- "approve all"
- "approve 1, 3" (specific numbers)
- "reject all"
```

### 3. Add Approved URLs to Notion

**MCP first:** Use the Notion MCP `notion-create-pages` tool to create a page in database `3026ed85-e90a-814d-96e8-e35f0b8fae89` with properties: Title, URL, Mentor, Source Type, Status (pending).

**Curl fallback** (if MCP fails):

```bash
NOTION_TOKEN=$(grep NOTION_API_TOKEN .env 2>/dev/null || echo "")

curl -s --max-time 15 -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{
    "parent": {"database_id": "3026ed85-e90a-814d-96e8-e35f0b8fae89"},
    "properties": {
      "Title": {"title": [{"text": {"content": "CONTENT TITLE"}}]},
      "URL": {"url": "CONTENT_URL"},
      "Mentor": {"select": {"name": "MENTOR_NAME"}},
      "Source Type": {"select": {"name": "youtube|blog|podcast"}},
      "Status": {"select": {"name": "pending"}}
    }
  }'
```

### 4. Check for Duplicates

**MCP first:** Use Notion MCP `notion-search` or `notion-fetch` to check if the URL already exists in the database.

**Curl fallback** (if MCP fails):
```bash
curl -s --max-time 15 -X POST "https://api.notion.com/v1/databases/3026ed85-e90a-814d-96e8-e35f0b8fae89/query" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{"filter":{"property":"URL","url":{"equals":"CONTENT_URL"}}}'
```

Skip duplicates and tell the user.

## Output Format

After adding to Notion:

```
Added [X] URLs to Notion with status "pending":
- [Title 1] -> Hormozi / YouTube
- [Title 2] -> Hormozi / Blog

Run `/sync-mentor` to extract content and save to the mentor-library repo.
```

## Search Quality Guidelines

**Include:**
- Long-form content (10+ min videos, detailed articles)
- Recent content (last 2 years preferred)
- Primary sources (mentor's own channels/sites)
- High engagement/views

**Exclude:**
- Short clips under 5 minutes
- Listicles and thin content
- Third-party summaries or reaction videos
- Duplicate content (same topic covered in another already-synced source)

## After Research

Ask: "Would you like me to:
- Search for more content on a different topic?
- Run `/sync-mentor` to extract and save the approved content?
- Research content for a different mentor?"
