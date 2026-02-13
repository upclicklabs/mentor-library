---
description: Sync pending URLs from Notion — extract YouTube transcripts and blog posts, save as markdown, push to GitHub
---

# Sync Mentor

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Process approved URLs from Notion: extract content, save as markdown, push to GitHub.

## Trigger

User runs `/sync-mentor` or asks to sync, process, or extract pending mentor content.

## Inputs

No inputs required. The command automatically queries Notion for all pending URLs.

## Process

### 1. Sync Repo

```bash
cd /Users/kristineestigoy/Desktop/mentor-library && git pull --quiet 2>/dev/null || true
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

If no pending entries, tell user: "No pending URLs in Notion. Use `/research-mentor [Mentor] [topic]` to find content first."

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

Fetch the URL content. Extract main article text. Strip navigation, ads, sidebars. Preserve headings, paragraphs, lists, formatting. Convert to clean markdown.

### 5. Save as Markdown

**Path:** `/Users/kristineestigoy/Desktop/mentor-library/{mentor-slug}/{source-type}/{title-slug}.md`

- `{mentor-slug}` = mentor name lowercased (hormozi, ethan, chris, claude)
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
cd /Users/kristineestigoy/Desktop/mentor-library
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

## Output Format

For each URL processed:
```
## Processing: [Title]
[x] Retrieved from Notion
[x] Content extracted
[x] Saved as .md file
[x] Pushed to GitHub
[x] Notion status updated -> synced
```

## Error Handling

| Error | Action |
|-------|--------|
| YouTube transcript fails | Try web fetch fallback, then set "error" in Notion |
| Web fetch fails | Set status "error" in Notion |
| Git push fails | Set status "error", show git error to user |
| Notion API fails | Retry once, then alert user |
| No pending URLs | Tell user to run `/research-mentor` first |

## After Sync

Tell the user how many URLs were processed and their status. Offer: "Would you like me to sync more content, or ask a mentor a question?"
