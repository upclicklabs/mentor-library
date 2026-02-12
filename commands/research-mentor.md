---
description: Find and curate content from a mentor on a specific topic. Searches YouTube, blogs, and podcasts, then saves approved URLs to Notion for syncing.
argument-hint: "[Mentor] [topic]"
allowed-tools:
  - Bash
  - WebSearch
  - WebFetch
---

# /research-mentor

Search for high-quality content from a mentor and add approved URLs to the Notion database.

## Notion Database
- **Database ID:** `3026ed85-e90a-814d-96e8-e35f0b8fae89`
- **API Token:** Read `NOTION_API_TOKEN` from `/Users/kristineestigoy/Desktop/Mentors Skills/.env`

## Mentors

| Mentor | Focus Areas | Search Sources |
|--------|-------------|----------------|
| **Hormozi** | Offers, lead gen, business growth | YouTube, acquisition.com, podcasts |
| **Ethan** | AEO, answer engine optimization | YouTube, blogs, industry articles |
| **Chris** | LinkedIn strategy, content | YouTube, LinkedIn posts, blogs |
| **Claude** | Prompting, AI workflows, MCP | YouTube, Anthropic docs, blogs |

---

## Process

### 1. Parse the Request

Extract the **mentor name** and **topic** from `$ARGUMENTS`.

Example: `/mentor-skills:research-mentor Hormozi lead generation` -> Mentor: Hormozi, Topic: lead generation

If no mentor specified, ask. If no topic specified, ask.

### 2. Search for Content

Use **WebSearch** with these query patterns:

For YouTube:
- `"{Mentor full name}" {topic} site:youtube.com`

For blogs/articles:
- `"{Mentor full name}" {topic}` (general web)
- `"{Mentor full name}" {topic} site:{mentor-specific-site}`

Mentor-specific sites:
- Hormozi -> `acquisition.com`
- Ethan -> relevant AEO/SEO blogs
- Chris -> `linkedin.com`
- Claude -> `anthropic.com`, `docs.anthropic.com`

### 3. Present Results for Approval

Show findings in this format:

```
## Research Results: [Mentor] -- [Topic]

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | [Title] | YouTube | [link] |
| 2 | [Title] | Blog | [link] |
| 3 | [Title] | Podcast | [link] |

**Reply with:**
- "approve all"
- "approve 1, 3" (specific numbers)
- "reject all"
```

### 4. Add Approved URLs to Notion

For each approved URL, create a Notion page in the database:

```bash
NOTION_TOKEN=$(grep NOTION_API_TOKEN /Users/kristineestigoy/Desktop/Mentors\ Skills/.env | cut -d= -f2)

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

### 5. Confirm and Hand Off

After adding to Notion:

```
Added [X] URLs to Notion with status "pending":
- [Title 1] -> Hormozi / YouTube
- [Title 2] -> Hormozi / Blog

Run `/mentor-skills:sync-mentor` to extract content and push to GitHub.
```

---

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

---

## Rules

1. **Always present for approval.** Never add to Notion without user saying "approve."
2. **Write to Notion only.** This skill creates Notion entries. `/mentor-skills:sync-mentor` handles extraction and GitHub.
3. **Check for duplicates.** Before adding, query Notion to see if the URL already exists.
4. **Set status to "pending."** Every new entry starts as pending.
5. **Be specific in searches.** Use mentor's full name in quotes for accurate results.
6. **Show sources.** Always include the URL so user can verify before approving.
