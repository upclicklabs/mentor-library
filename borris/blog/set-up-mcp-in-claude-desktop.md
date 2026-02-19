---
title: "Set Up MCP in Claude Desktop"
source_url: "https://modelcontextprotocol.io/quickstart/user"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Set Up MCP in Claude Desktop

Model Context Protocol (MCP) servers extend AI applications' capabilities by providing secure, controlled access to local resources and tools. This guide demonstrates how to connect to local MCP servers using Claude Desktop.

## Prerequisites

### Claude Desktop

Download and install Claude Desktop for your operating system (macOS and Windows). If you already have it installed, verify you're running the latest version.

### Node.js

The Filesystem Server and many other MCP servers require Node.js to run. Verify your Node.js installation:

```bash
node --version
```

If not installed, download from nodejs.org. The LTS version is recommended for stability.

## Understanding MCP Servers

MCP servers are programs that run on your computer and provide specific capabilities to Claude Desktop through a standardized protocol. Each server exposes tools that Claude can use to perform actions, with your approval. The Filesystem Server provides tools for:

- Reading file contents and directory structures
- Creating new files and directories
- Moving and renaming files
- Searching for files by name or content

All actions require your explicit approval before execution.

## Installing the Filesystem Server

### Step 1: Open Claude Desktop Settings

Access the Claude Desktop settings by clicking on the Claude menu in your system's menu bar and selecting "Settings..."

### Step 2: Access Developer Settings

Navigate to the "Developer" tab in the left sidebar and click the "Edit Config" button to open the configuration file.

The file is located at:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### Step 3: Configure the Filesystem Server

Replace the contents of the configuration file with the following JSON structure:

**macOS:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Desktop",
        "/Users/username/Downloads"
      ]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\username\\Desktop",
        "C:\\Users\\username\\Downloads"
      ]
    }
  }
}
```

Replace `username` with your actual computer username. The paths listed specify which directories the Filesystem Server can access.

### Step 4: Restart Claude Desktop

After saving the configuration file, completely quit and restart Claude Desktop. You'll see an MCP server indicator in the bottom-right corner of the conversation input box upon successful restart.

## Using the Filesystem Server

### File Management Examples

- "Can you write a poem and save it to my desktop?"
- "What work-related files are in my downloads folder?"
- "Please organize all images on my desktop into a new folder called 'Images'"

### How Approval Works

Before executing any file system operation, Claude will request your approval. Review each request carefully before approving.

## Troubleshooting

### Server not showing up

1. Restart Claude Desktop completely
2. Check your `claude_desktop_config.json` file syntax
3. Make sure file paths are valid and absolute
4. Check logs for connection errors
5. Try manually running the server from command line

### Getting logs

Claude.app logging related to MCP is written to:
- macOS: `~/Library/Logs/Claude`
- Windows: `%APPDATA%\Claude\logs`

### Tool calls failing silently

1. Check Claude's logs for errors
2. Verify your server builds and runs without errors
3. Try restarting Claude Desktop

## Next Steps

- Explore other MCP servers from the collection of official and community-created servers
- Build your own custom MCP server
- Connect to remote MCP servers for cloud-based tools
- Dive deeper into the MCP architecture
