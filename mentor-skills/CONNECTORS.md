# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~knowledge base` refers to Notion or whichever knowledge base tool is connected.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Knowledge base | `~~knowledge base` | Notion | Confluence, Airtable |

## Required setup

| Tool | What it does | Setup |
|------|-------------|-------|
| **Notion** | Stores mentor URLs with status (pending/synced/error) | Connect Notion in Cowork, or provide `NOTION_API_TOKEN` in `.env` for curl fallback |
| **GitHub** | Stores mentor content as markdown files | Repo: `upclicklabs/mentor-library`. Clone the repo to access locally. Sync pushes via git. |
| **Python** | Extracts YouTube transcripts | `pip3 install youtube-transcript-api` |

## Notion Database

- **Database ID:** `3026ed85-e90a-814d-96e8-e35f0b8fae89`
- **Properties:** Title, URL, Mentor, Source Type, Status
