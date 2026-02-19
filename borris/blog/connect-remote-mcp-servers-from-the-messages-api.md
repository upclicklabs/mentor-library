---
title: "Connect Remote MCP Servers from the Messages API"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Connect Remote MCP Servers from the Messages API

Claude's Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API without a separate MCP client.

Current version: This feature requires the beta header: "anthropic-beta": "mcp-client-2025-11-20"

The previous version (mcp-client-2025-04-04) is deprecated.

This feature is in beta and is not covered by Zero Data Retention (ZDR) arrangements.

## Key Features

- **Direct API integration**: Connect to MCP servers without implementing an MCP client
- **Tool calling support**: Access MCP tools through the Messages API
- **Flexible tool configuration**: Enable all tools, allowlist specific tools, or denylist unwanted tools
- **Per-tool configuration**: Configure individual tools with custom settings
- **OAuth authentication**: Support for OAuth Bearer tokens for authenticated servers
- **Multiple servers**: Connect to multiple MCP servers in a single request

## Limitations

- Of the feature set of the MCP specification, only tool calls are currently supported.
- The server must be publicly exposed through HTTP (supports both Streamable HTTP and SSE transports). Local STDIO servers cannot be connected directly.
- The MCP connector is currently not supported on Amazon Bedrock and Google Vertex.

## Using the MCP Connector in the Messages API

The MCP connector uses two components:

1. **MCP Server Definition** (mcp_servers array): Defines server connection details (URL, authentication)
2. **MCP Toolset** (tools array): Configures which tools to enable and how to configure them

### Basic Example (Shell)

```bash
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: mcp-client-2025-11-20" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": "What tools do you have available?"}],
    "mcp_servers": [
      {
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse",
        "name": "example-mcp",
        "authorization_token": "YOUR_TOKEN"
      }
    ],
    "tools": [
      {
        "type": "mcp_toolset",
        "mcp_server_name": "example-mcp"
      }
    ]
  }'
```

## MCP Server Configuration

Each MCP server in the mcp_servers array defines the connection details:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| type | string | Yes | Currently only "url" is supported |
| url | string | Yes | The URL of the MCP server. Must start with https:// |
| name | string | Yes | A unique identifier for this MCP server |
| authorization_token | string | No | OAuth authorization token if required by the MCP server |

## MCP Toolset Configuration

The MCPToolset lives in the tools array and configures which tools from the MCP server are enabled.

### Tool Configuration Options

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| enabled | boolean | true | Whether this tool is enabled |
| defer_loading | boolean | false | If true, tool description is not sent to the model initially. Used with Tool Search Tool. |

### Configuration Merging Precedence

1. Tool-specific settings in configs
2. Set-level default_config
3. System defaults

## Common Configuration Patterns

### Enable All Tools (default)

```json
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp"
}
```

### Allowlist - Enable Only Specific Tools

```json
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp",
  "default_config": { "enabled": false },
  "configs": {
    "search_events": { "enabled": true },
    "create_event": { "enabled": true }
  }
}
```

### Denylist - Disable Specific Tools

```json
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp",
  "configs": {
    "delete_all_events": { "enabled": false },
    "share_calendar_publicly": { "enabled": false }
  }
}
```

## Response Content Types

### MCP Tool Use Block

```json
{
  "type": "mcp_tool_use",
  "id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "name": "echo",
  "server_name": "example-mcp",
  "input": { "param1": "value1", "param2": "value2" }
}
```

### MCP Tool Result Block

```json
{
  "type": "mcp_tool_result",
  "tool_use_id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "is_error": false,
  "content": [{ "type": "text", "text": "Hello" }]
}
```

## Multiple MCP Servers

You can connect to multiple MCP servers by including multiple server definitions in mcp_servers and a corresponding MCPToolset for each in the tools array.

## Authentication

For MCP servers that require OAuth authentication, obtain an access token and pass it via the authorization_token parameter. API consumers are expected to handle the OAuth flow and token refresh prior to making the API call.

The MCP inspector can guide you through obtaining an access token for testing:

1. Run: npx @modelcontextprotocol/inspector
2. Select "SSE" or "Streamable HTTP" transport type
3. Enter the MCP server URL
4. Click "Open Auth Settings" then "Quick OAuth Flow"
5. Follow the steps and copy the access_token value

## Client-Side MCP Helpers (TypeScript)

The TypeScript SDK provides helper functions that convert between MCP types and Claude API types:

- **mcpTools(tools, mcpClient)**: Converts MCP tools to Claude API tools for use with toolRunner()
- **mcpMessages(messages)**: Converts MCP prompt messages to Claude API message format
- **mcpResourceToContent(resource)**: Converts an MCP resource to a Claude API content block
- **mcpResourceToFile(resource)**: Converts an MCP resource to a file object for upload

Install both SDKs: `npm install @anthropic-ai/sdk @modelcontextprotocol/sdk`

## Migration Guide (from mcp-client-2025-04-04)

Key changes:
1. New beta header: Change from mcp-client-2025-04-04 to mcp-client-2025-11-20
2. Tool configuration moved to the tools array as MCPToolset objects
3. More flexible configuration: supports allowlisting, denylisting, and per-tool configuration

## Validation Rules

- Server must exist: mcp_server_name must match a defined server
- Server must be used: Every MCP server must be referenced by exactly one MCPToolset
- Unique toolset per server: Each MCP server can only be referenced by one MCPToolset
- Unknown tool names in configs will log a warning but not return an error
