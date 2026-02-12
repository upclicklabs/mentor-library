---
description: Sync pending URLs from Notion into the mentor knowledge base. Extracts YouTube transcripts and blog posts, saves as markdown, pushes to GitHub.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - WebFetch
---

# /sync-mentor

Process approved URLs from Notion: extract content, save as markdown, push to GitHub.

## Notion Database
- **Database ID:** `3026ed85-e90a-814d-96e8-e35f0b8fae89`
- **API Token:** Read `NOTION_API_TOKEN` from `~/.env` or from the environment

## GitHub Repository
- **Plugin root:** `${CLAUDE_PLUGIN_ROOT}`
- **Remote:** `upclicklabs/mentor-library`

## Mentors
| Mentor | Folder |
|--------|--------|
| Hormozi | `hormozi/` |
| Ethan | `ethan/` |
| Chris | `chris/` |
| Claude | `claude/` |

---

## Process

### 1. Sync Repo

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && git pull --quiet 2>/dev/null || true
```

### 2. Load Notion Token

```bash
NOTION_TOKEN=$(grep NOTION_API_TOKEN /Users/kristineestigoy/Desktop/Mentors\ Skills/.env | cut -d= -f2)
```

### 3. Query Notion for Pending URLs

```bash
curl -s --max-time 15 -X POST "https://api.notion.com/v1/databases/3026ed85-e90a-814d-96e8-e35f0b8fae89/query" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{"filter":{"property":"Status","select":{"equals":"pending"}}}'
```

Extract from each entry: **URL**, **Mentor**, **Source Type**, **Page ID**.

If no pending entries, tell user: "No pending URLs in Notion. Use `/mentor-skills:research-mentor [Mentor] [topic]` to find content first."

### 4. Extract Content (for each URL)

#### YouTube (URL contains youtube.com or youtu.be)

**Get video title:**
```bash
curl -s --max-time 10 "https://noembed.com/embed?url=YOUTUBE_URL"
```
Parse the `title` field from the JSON response.

**Extract video ID** from URL:
- `youtu.be/VIDEO_ID` or `youtube.com/watch?v=VIDEO_ID`

**Get transcript:**
```bash
python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch('VIDEO_ID')
for snippet in transcript:
    print(snippet.text)
"
```

**Format** the raw transcript into clean, readable paragraphs. Remove filler, group related sentences.

#### Blogs/Articles

Use **WebFetch** to pull the URL. Extract main article text. Strip navigation, ads, sidebars. Preserve headings, paragraphs, lists, formatting. Convert to clean markdown.

### 5. Save as Markdown

**Path:** `${CLAUDE_PLUGIN_ROOT}/{mentor-slug}/{source-type}/{title-slug}.md`

- `{mentor-slug}` = mentor name lowercased
- `{source-type}` = `youtube`, `blog`, or `pdf`
- `{title-slug}` = title lowercased, spaces to hyphens, max 80 chars, URL-safe

Create directories if needed: `mkdir -p {path}`

**File format:**
```markdown
---
title: "CONTENT TITLE"
source_url: "ORIGINAL URL"
source_type: youtube|blog|pdf
mentor: "MENTOR NAME"
date_synced: "ISO TIMESTAMP"
---

# CONTENT TITLE

[Clean extracted content here...]
```

### 6. Push to GitHub

```bash
cd "${CLAUDE_PLUGIN_ROOT}"
git add {mentor-slug}/{source-type}/{title-slug}.md
git commit -m "Add {Mentor} {source-type}: {Title}"
git push
```

### 7. Update Notion Status

**On success:**
```bash
curl -s --max-time 15 -X PATCH "https://api.notion.com/v1/pages/PAGE_ID" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{"properties":{"Status":{"select":{"name":"synced"}},"Title":{"title":[{"text":{"content":"CONTENT TITLE"}}]}}}'
```

**On failure:** Set status to `error`.

---

## Progress Display

For each URL:
```
## Processing: [Title]
[x] Retrieved from Notion
[x] Content extracted
[x] Saved as .md file
[x] Pushed to GitHub
[x] Notion status updated -> synced
```

For batch:
```
| # | Title | Mentor | Status |
|---|-------|--------|--------|
| 1 | [Title] | Hormozi | synced |
| 2 | [Title] | Claude | processing... |
| 3 | [Title] | Ethan | pending |
```

---

## Error Handling

| Error | Action |
|-------|--------|
| YouTube transcript fails | Try WebFetch fallback, then set "error" in Notion |
| Web fetch fails | Set status "error" in Notion |
| Git push fails | Set status "error", show git error to user |
| Notion API fails | Retry once, then alert user |
| No pending URLs | Tell user to run `/mentor-skills:research-mentor` first |

---

## Rules

1. **Read from Notion, write to GitHub.** Never create Notion entries — that's `/mentor-skills:research-mentor`'s job.
2. **Always update Notion status** after processing (synced or error).
3. **One commit per file.** Don't batch commits.
4. **Clean formatting.** Transcripts should be readable paragraphs, not raw dumps.
5. **Show progress.** Display the tracker for every URL processed.
