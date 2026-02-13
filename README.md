# Mentor Skills

A mentor plugin primarily designed for [Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop application — though it also works in Claude Code. Build personal AI mentor assistants from YouTube transcripts, blog posts, and podcasts.

## Installation

Upload the plugin zip to Cowork via Plugins > Upload plugin.

## Commands

| Command | Description |
|---|---|
| `/research-mentor` | Find and curate mentor content on a topic — search YouTube, blogs, and podcasts, then save approved URLs to Notion |
| `/sync-mentor` | Sync pending URLs from Notion — extract YouTube transcripts and blog posts, save as markdown, push to GitHub |

## Skills

| Skill | Description |
|---|---|
| `mentor-claude` | Answer questions using Claude/Anthropic knowledge base — prompting, AI workflows, MCP, and Anthropic tools |
| `mentor-hormozi` | Answer questions using Alex Hormozi's knowledge base — offers, lead gen, pricing, and business growth |
| `mentor-ethan` | Answer questions using Ethan's knowledge base — AEO, answer engine optimization, and AI visibility |
| `mentor-chris` | Answer questions using Chris's knowledge base — LinkedIn strategy, content, and personal branding |

## How It Works

```
/research-mentor  →  Notion (pending)  →  /sync-mentor  →  GitHub (.md files)  →  mentor skills
```

1. **Research** — `/research-mentor Hormozi lead gen` finds YouTube videos and articles, presents them for approval, and saves approved URLs to Notion with status "pending"
2. **Sync** — `/sync-mentor` pulls all pending URLs from Notion, extracts transcripts/content, saves as markdown to this repo, and updates Notion status to "synced"
3. **Ask** — ask a question about offers and the Hormozi mentor skill activates automatically, reads the markdown files, and answers grounded in the mentor's actual content

## Example Workflows

### Researching Content

```
> /research-mentor Hormozi lead generation
```

Claude will search YouTube and the web for Hormozi content on lead generation, present results for approval, and save approved URLs to Notion.

### Syncing Content

```
> /sync-mentor
```

Claude will pull all pending URLs from Notion, extract transcripts, save as markdown, push to GitHub, and mark entries as synced.

### Asking a Mentor

```
> How does Hormozi recommend pricing a Grand Slam Offer?
```

The Hormozi mentor skill auto-activates, pulls latest transcripts from GitHub, and responds grounded in actual content with citations.

## Configuration

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin works with the following integrations:

- **Notion** — Stores mentor URLs with sync status (pending/synced/error)
- **GitHub** — Stores extracted transcripts as markdown files

## Setup

1. Clone this repo to `/Users/kristineestigoy/Desktop/mentor-library`
2. Add `NOTION_API_TOKEN` to your `.env` file
3. Install Python dependency: `pip3 install youtube-transcript-api`
4. Upload the plugin zip to Cowork
