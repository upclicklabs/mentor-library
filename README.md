# Mentor Library

AI mentor assistants built from YouTube transcripts, blog posts, and podcasts. Claude Code plugin with a three-phase pipeline.

## Commands

| Command | What it does |
|---------|-------------|
| `/claude` | Ask the Claude/AI mentor about prompting, workflows, MCP |
| `/hormozi` | Ask Hormozi about offers, lead gen, pricing, growth |
| `/ethan` | Ask Ethan about AEO and AI visibility |
| `/chris` | Ask Chris about LinkedIn strategy and content |
| `/research-mentor [Mentor] [topic]` | Search for content, approve URLs, save to Notion |
| `/sync-mentor` | Pull pending URLs from Notion, extract content, push to GitHub |

## How It Works

```
/research-mentor  →  Notion (pending)  →  /sync-mentor  →  GitHub (.md files)  →  /claude, /hormozi, etc.
```

1. **Research** — `/research-mentor Hormozi lead gen` finds YouTube videos and articles, presents them for approval, and saves approved URLs to Notion with status "pending"
2. **Sync** — `/sync-mentor` pulls all pending URLs from Notion, extracts transcripts/content, saves as markdown to this repo, and updates Notion status to "synced"
3. **Ask** — `/hormozi How do I price my offer?` reads the markdown files and answers grounded in the mentor's actual content

## Folder Structure

```
mentor-library/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── claude.md
│   ├── hormozi.md
│   ├── ethan.md
│   ├── chris.md
│   ├── sync-mentor.md
│   └── research-mentor.md
├── claude/
│   └── youtube/
├── hormozi/
│   └── youtube/
├── ethan/
│   └── youtube/
├── chris/
│   └── youtube/
└── README.md
```

## Setup

1. Clone this repo
2. Create `.env` with your Notion API token:
   ```
   NOTION_API_TOKEN=your_token_here
   ```
3. Install the plugin in Claude Code / Cowork
4. Install Python dependency: `pip3 install youtube-transcript-api`

## Requirements

- Notion integration with access to the Mentor Sources database
- Python 3 with `youtube-transcript-api` package
- GitHub access to this repo
