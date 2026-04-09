---
title: "Claude Managed Agents"
source_url: "https://platform.claude.com/docs/en/managed-agents/overview"
source_type: blog
mentor: "Borris"
date_synced: "2026-04-09T00:00:00Z"
---

# Claude Managed Agents

Claude Managed Agents is a pre-built, configurable agent harness that runs in managed infrastructure. It provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and execute code securely. The harness supports built-in prompt caching, compaction, and other performance optimizations for high quality, efficient agent outputs.

## Messages API vs Claude Managed Agents

| | Messages API | Claude Managed Agents |
|---|---|---|
| What it is | Direct model prompting access | Pre-built, configurable agent harness that runs in managed infrastructure |
| Best for | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |

## Core Concepts

Claude Managed Agents is built around four concepts:

| Concept | Description |
|---------|-------------|
| Agent | The model, system prompt, tools, MCP servers, and skills |
| Environment | A configured container template (packages, network access) |
| Session | A running agent instance within an environment, performing a specific task and generating outputs |
| Events | Messages exchanged between your application and the agent (user turns, tool results, status updates) |

## How It Works

1. Create an agent - Define the model, system prompt, tools, MCP servers, and skills. Create the agent once and reference it by ID across sessions.
2. Create an environment - Configure a cloud container with pre-installed packages (Python, Node.js, Go, etc.), network access rules, and mounted files.
3. Start a session - Launch a session that references your agent and environment configuration.
4. Send events and stream responses - Send user messages as events. Claude autonomously executes tools and streams back results via server-sent events (SSE). Event history is persisted server-side and can be fetched in full.
5. Steer or interrupt - Send additional user events to guide the agent mid-execution, or interrupt it to change direction.

## When to Use Claude Managed Agents

Best for workloads that need:
- Long-running execution - Tasks that run for minutes or hours with multiple tool calls
- Cloud infrastructure - Secure containers with pre-installed packages and network access
- Minimal infrastructure - No need to build your own agent loop, sandbox, or tool execution layer
- Stateful sessions - Persistent file systems and conversation history across multiple interactions

## Beta Access

Claude Managed Agents is currently in beta. All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

Requirements:
1. A Claude API key
2. The beta header on all requests
3. Access to Claude Managed Agents (enabled by default for all API accounts)

Certain features (outcomes, multiagent, and memory) are in research preview and require requesting access.

## Rate Limits

| Operation | Limit |
| --- | --- |
| Create endpoints (agents, sessions, environments, etc.) | 60 requests per minute |
| Read endpoints (retrieve, list, stream, etc.) | 600 requests per minute |

Organization-level spend limits and tier-based rate limits also apply.

---

# Quickstart

## Install the CLI

### Homebrew (macOS)

```bash
brew install anthropics/tap/ant
```

On macOS, unquarantine the binary:

```bash
xattr -d com.apple.quarantine "$(brew --prefix)/bin/ant"
```

### curl (Linux/WSL)

```bash
VERSION=1.0.0
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m | sed -e 's/x86_64/amd64/' -e 's/aarch64/arm64/')
curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin ant
```

### Go

```bash
go install github.com/anthropics/anthropic-cli/cmd/ant@latest
```

## Install the SDK

```bash
# Python
pip install anthropic

# TypeScript
npm install @anthropic-ai/sdk

# Go
go get github.com/anthropics/anthropic-sdk-go
```

Set your API key:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Create Your First Session

### Step 1: Create an Agent

```python
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    system="You are a helpful coding assistant. Write clean, well-documented code.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)
```

The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more).

### Step 2: Create an Environment

```python
environment = client.beta.environments.create(
    name="quickstart-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)
```

### Step 3: Start a Session

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Quickstart session",
)
```

### Step 4: Send a Message and Stream the Response

```python
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
                    },
                ],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nAgent finished.")
                break
```

### What's Happening

When you send a user event, Claude Managed Agents:
1. Provisions a container based on your environment configuration
2. Runs the agent loop - Claude decides which tools to use
3. Executes tools inside the container (file writes, bash commands, etc.)
4. Streams events back in real-time
5. Emits `session.status_idle` when done

---

# Agent Setup

An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills.

## Agent Configuration Fields

| Field | Description |
| --- | --- |
| `name` | Required. A human-readable name for the agent. |
| `model` | Required. The Claude model that powers the agent. All Claude 4.5 and later models are supported. |
| `system` | A system prompt that defines the agent's behavior and persona. |
| `tools` | The tools available to the agent. Combines pre-built agent tools, MCP tools, and custom tools. |
| `mcp_servers` | MCP servers that provide standardized third-party capabilities. |
| `skills` | Skills that supply domain-specific context with progressive disclosure. |
| `callable_agents` | Other agents this agent can invoke for multi-agent orchestration (research preview). |
| `description` | A description of what the agent does. |
| `metadata` | Arbitrary key-value pairs for your own tracking. |

## Create an Agent

```python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    system="You are a helpful coding agent.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)
```

To use Claude Opus 4.6 with fast mode, pass model as an object: `{"id": "claude-opus-4-6", "speed": "fast"}`.

The response includes `id`, `version`, `created_at`, `updated_at`, and `archived_at` fields. The `version` starts at 1 and increments each time you update the agent.

## Update an Agent

Updating generates a new version. Pass the current `version` to ensure you're updating from a known state.

```python
updated_agent = client.beta.agents.update(
    agent.id,
    version=agent.version,
    system="You are a helpful coding agent. Always write tests.",
)
```

### Update Semantics

- Omitted fields are preserved - only include fields you want to change
- Scalar fields (`model`, `system`, `name`) are replaced with the new value
- Array fields (`tools`, `mcp_servers`, `skills`, `callable_agents`) are fully replaced
- Metadata is merged at the key level; set a key to empty string to delete it
- No-op detection - if the update produces no change, no new version is created

## Agent Lifecycle

| Operation | Behavior |
| --- | --- |
| Update | Generates a new agent version |
| List versions | Fetch the full version history |
| Archive | Agent becomes read-only; new sessions cannot reference it, existing sessions continue |

```python
# List versions
for version in client.beta.agents.versions.list(agent.id):
    print(f"Version {version.version}: {version.updated_at.isoformat()}")

# Archive
archived = client.beta.agents.archive(agent.id)
```

---

# Sessions

A session is a running agent instance within an environment. Each session references an agent and an environment and maintains conversation history across multiple interactions.

## Creating a Session

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)
```

### Pinning to a Specific Agent Version

```python
pinned_session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": 1},
    environment_id=environment.id,
)
```

## MCP Authentication Through Vaults

Pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials:

```python
vault_session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
```

## Starting the Session

Creating a session provisions the environment and agent but does not start any work. Send events to delegate a task:

```python
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {"type": "text", "text": "List the files in the working directory."}
            ],
        },
    ],
)
```

## Session Statuses

| Status | Description |
|--------|-------------|
| `idle` | Agent is waiting for input. Sessions start in `idle`. |
| `running` | Agent is actively executing |
| `rescheduling` | Transient error occurred, retrying automatically |
| `terminated` | Session has ended due to an unrecoverable error |

## Other Session Operations

```python
# Retrieve a session
retrieved = client.beta.sessions.retrieve(session.id)

# List sessions
for session in client.beta.sessions.list():
    print(f"{session.id}: {session.status}")

# Archive a session (prevents new events, preserves history)
client.beta.sessions.archive(session.id)

# Delete a session (permanently removes record, events, container)
client.beta.sessions.delete(session.id)
```

A `running` session cannot be deleted; send an interrupt event first.

---

# Cloud Environment Setup

Environments define the container configuration where your agent runs. Create once, reference by ID each time you start a session.

## Create an Environment

```python
environment = client.beta.environments.create(
    name="python-dev",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)
```

## Configuration Options

### Packages

Pre-install packages into the container before the agent starts:

```python
environment = client.beta.environments.create(
    name="data-analysis",
    config={
        "type": "cloud",
        "packages": {
            "pip": ["pandas", "numpy", "scikit-learn"],
            "npm": ["express"],
        },
        "networking": {"type": "unrestricted"},
    },
)
```

Supported package managers:

| Field | Package manager | Example |
| --- | --- | --- |
| `apt` | System packages (apt-get) | `"ffmpeg"` |
| `cargo` | Rust (cargo) | `"ripgrep@14.0.0"` |
| `gem` | Ruby (gem) | `"rails:7.1.0"` |
| `go` | Go modules | `"golang.org/x/tools/cmd/goimports@latest"` |
| `npm` | Node.js (npm) | `"express@4.18.0"` |
| `pip` | Python (pip) | `"pandas==2.2.0"` |

### Networking

| Mode | Description |
| --- | --- |
| `unrestricted` | Full outbound network access, except for a general safety blocklist. Default. |
| `limited` | Restricts container network access to the `allowed_hosts` list. |

```python
config = {
    "type": "cloud",
    "networking": {
        "type": "limited",
        "allowed_hosts": ["api.example.com"],
        "allow_mcp_servers": True,
        "allow_package_managers": True,
    },
}
```

When using `limited` networking:
- `allowed_hosts` specifies domains the container can reach (must be HTTPS-prefixed)
- `allow_mcp_servers` permits outbound access to MCP server endpoints. Defaults to `false`.
- `allow_package_managers` permits outbound access to public package registries. Defaults to `false`.

For production deployments, use `limited` networking with an explicit `allowed_hosts` list.

## Environment Lifecycle

- Environments persist until explicitly archived or deleted
- Multiple sessions can reference the same environment
- Each session gets its own container instance (no shared file system state)
- Environments are not versioned

## Manage Environments

```python
# List environments
environments = client.beta.environments.list()

# Retrieve a specific environment
env = client.beta.environments.retrieve(environment.id)

# Archive (read-only, existing sessions continue)
client.beta.environments.archive(environment.id)

# Delete (only if no sessions reference it)
client.beta.environments.delete(environment.id)
```

## Pre-installed Runtimes (Cloud Container Reference)

### Programming Languages

| Language | Version | Package manager |
|----------|---------|-----------------|
| Python | 3.12+ | pip, uv |
| Node.js | 20+ | npm, yarn, pnpm |
| Go | 1.22+ | go modules |
| Rust | 1.77+ | cargo |
| Java | 21+ | maven, gradle |
| Ruby | 3.3+ | bundler, gem |
| PHP | 8.3+ | composer |
| C/C++ | GCC 13+ | make, cmake |

### Databases

| Database | Description |
|----------|-------------|
| SQLite | Pre-installed, available immediately |
| PostgreSQL client | `psql` client for connecting to external databases |
| Redis client | `redis-cli` for connecting to external instances |

Database servers are not running by default - only client tools are included.

### System Utilities

git, curl, wget, jq, tar, zip, unzip, ssh, scp, tmux, screen, make, cmake, ripgrep (rg), tree, htop, sed, awk, grep, vim, nano, diff, patch

### Container Specifications

| Property | Value |
|----------|-------|
| Operating system | Ubuntu 22.04 LTS |
| Architecture | x86_64 (amd64) |
| Memory | Up to 8 GB |
| Disk space | Up to 10 GB |
| Network | Disabled by default (enable in environment config) |

---

# Events and Streaming

Communication with Claude Managed Agents is event-based. You send user events, and receive agent and session events back.

## Event Types

Event type strings follow a `{domain}.{action}` naming convention.

### User Events (you send these)

| Type | Description |
| --- | --- |
| `user.message` | A user message with text content |
| `user.interrupt` | Stop the agent mid-execution |
| `user.custom_tool_result` | Response to a custom tool call from the agent |
| `user.tool_confirmation` | Approve or deny an agent or MCP tool call when a permission policy requires confirmation |
| `user.define_outcome` | Define an outcome for the agent to work toward |

### Agent Events (you receive these)

| Type | Description |
| --- | --- |
| `agent.message` | Agent response containing text content blocks |
| `agent.thinking` | Agent thinking content, emitted separately from messages |
| `agent.tool_use` | Agent invoked a pre-built agent tool |
| `agent.tool_result` | Result of a pre-built agent tool execution |
| `agent.mcp_tool_use` | Agent invoked an MCP server tool |
| `agent.mcp_tool_result` | Result of an MCP tool execution |
| `agent.custom_tool_use` | Agent invoked one of your custom tools |

### Session Events (status updates)

| Type | Description |
| --- | --- |
| `session.status_idle` | Session is idle, waiting for input |
| `session.status_running` | Session transitioned to running |
| `session.error` | A non-fatal error occurred |

### Span Events (grouping)

| Type | Description |
| --- | --- |
| `span.start` | Marks the beginning of a logical span |
| `span.end` | Marks the end of a logical span |

## Opening a Stream

Use SSE (Server-Sent Events) to stream events in real time:

```python
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\nAgent finished.")
                break
```

### Resuming from a specific event

Pass `after_event_id` to resume streaming from a specific point:

```python
with client.beta.sessions.events.stream(session.id, after_event_id=last_seen_id) as stream:
    for event in stream:
        # process events...
        pass
```

## Sending Multiple Events

You can batch multiple events in a single request:

```python
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [{"type": "text", "text": "First, do X. Then do Y."}],
        },
    ],
)
```

## Interrupting the Agent

Send `user.interrupt` to stop the agent mid-execution:

```python
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt"}],
)
```

After an interrupt, the session goes idle. You can then send a new `user.message` to redirect.

## Handling Custom Tool Calls

When the agent invokes a custom tool, it emits an `agent.custom_tool_use` event and waits for your `user.custom_tool_result`:

```python
for event in stream:
    if event.type == "agent.custom_tool_use":
        # Execute the tool in your application
        result = execute_my_tool(event.name, event.input)

        # Send the result back
        client.beta.sessions.events.send(
            session.id,
            events=[
                {
                    "type": "user.custom_tool_result",
                    "tool_use_id": event.id,
                    "content": [{"type": "text", "text": result}],
                },
            ],
        )
```

## Tool Confirmation

When tools have an `always_ask` permission policy, the session pauses with `session.status_idle` containing `stop_reason: requires_action`:

```python
for event in stream:
    if event.type == "session.status_idle" and event.stop_reason.type == "requires_action":
        for event_id in event.stop_reason.event_ids:
            # Allow or deny each pending tool
            client.beta.sessions.events.send(
                session.id,
                events=[
                    {
                        "type": "user.tool_confirmation",
                        "tool_use_id": event_id,
                        "result": "allow",  # or "deny"
                    },
                ],
            )
```

## Retrieving Past Events

Fetch all events for a session at any time:

```python
for event in client.beta.sessions.events.list(session.id):
    print(f"[{event.type}] {event.processed_at}")
```

---

# Tools

Claude Managed Agents provides a set of built-in tools that Claude can use autonomously within a session.

## Available Tools

| Tool | Name | Description |
|---|---|---|
| Bash | `bash` | Execute bash commands in a shell session |
| Read | `read` | Read a file from the local filesystem |
| Write | `write` | Write a file to the local filesystem |
| Edit | `edit` | Perform string replacement in a file |
| Glob | `glob` | Fast file pattern matching using glob patterns |
| Grep | `grep` | Text search using regex patterns |
| Web fetch | `web_fetch` | Fetch content from a URL |
| Web search | `web_search` | Search the web for information |

## Configuring the Toolset

Enable the full toolset with `agent_toolset_20260401`:

```python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    tools=[
        {
            "type": "agent_toolset_20260401",
            "configs": [
                {"name": "web_fetch", "enabled": False},
            ],
        },
    ],
)
```

### Disabling Specific Tools

```json
{
  "type": "agent_toolset_20260401",
  "configs": [
    { "name": "web_fetch", "enabled": false },
    { "name": "web_search", "enabled": false }
  ]
}
```

### Enabling Only Specific Tools

Set `default_config.enabled` to `false` and explicitly enable what you need:

```json
{
  "type": "agent_toolset_20260401",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true },
    { "name": "write", "enabled": true }
  ]
}
```

## Custom Tools

Define custom tools analogous to user-defined client tools in the Messages API. The model emits a structured request, your code runs the operation, and the result flows back.

```python
agent = client.beta.agents.create(
    name="Weather Agent",
    model="claude-sonnet-4-6",
    tools=[
        {"type": "agent_toolset_20260401"},
        {
            "type": "custom",
            "name": "get_weather",
            "description": "Get current weather for a location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                },
                "required": ["location"],
            },
        },
    ],
)
```

### Best Practices for Custom Tools

- Provide extremely detailed descriptions (3-4+ sentences per tool)
- Consolidate related operations into fewer tools with an `action` parameter
- Use meaningful namespacing in tool names (e.g., `db_query`, `storage_read`)
- Return only high-signal information in tool responses

---

# Permission Policies

Permission policies control whether server-executed tools run automatically or wait for approval. Custom tools are controlled by your application.

## Permission Policy Types

| Policy | Behavior |
| --- | --- |
| `always_allow` | The tool executes automatically with no confirmation |
| `always_ask` | Session pauses and waits for a `user.tool_confirmation` event |

## Setting a Policy

### Agent Toolset Permissions

```python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    tools=[
        {
            "type": "agent_toolset_20260401",
            "default_config": {
                "permission_policy": {"type": "always_ask"},
            },
        },
    ],
)
```

Default for agent toolset if omitted: `always_allow`.

### MCP Toolset Permissions

MCP toolsets default to `always_ask`. To auto-approve:

```python
agent = client.beta.agents.create(
    name="Dev Assistant",
    model="claude-sonnet-4-6",
    mcp_servers=[
        {"type": "url", "name": "github", "url": "https://mcp.example.com/github"},
    ],
    tools=[
        {"type": "agent_toolset_20260401"},
        {
            "type": "mcp_toolset",
            "mcp_server_name": "github",
            "default_config": {
                "permission_policy": {"type": "always_allow"},
            },
        },
    ],
)
```

### Override Individual Tool Policy

Allow the full toolset by default but require confirmation for bash:

```python
tools = [
    {
        "type": "agent_toolset_20260401",
        "default_config": {
            "permission_policy": {"type": "always_allow"},
        },
        "configs": [
            {
                "name": "bash",
                "permission_policy": {"type": "always_ask"},
            },
        ],
    },
]
```

## Responding to Confirmation Requests

When a tool with `always_ask` is invoked:
1. Session emits an `agent.tool_use` or `agent.mcp_tool_use` event
2. Session pauses with `session.status_idle` containing `stop_reason: requires_action`
3. Send a `user.tool_confirmation` event with `result` set to `"allow"` or `"deny"`
4. Once all blocking events are resolved, session transitions back to `running`

---

# MCP Connector

Claude Managed Agents supports connecting Model Context Protocol (MCP) servers to your agents.

MCP configuration is split across two steps:
1. Agent creation declares which MCP servers the agent connects to (by name and URL)
2. Session creation supplies auth by referencing a pre-registered vault

This separation keeps secrets out of reusable agent definitions.

## Declare MCP Servers on the Agent

```python
agent = client.beta.agents.create(
    name="GitHub Assistant",
    model="claude-sonnet-4-6",
    mcp_servers=[
        {
            "type": "url",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp/",
        },
    ],
    tools=[
        {"type": "agent_toolset_20260401"},
        {"type": "mcp_toolset", "mcp_server_name": "github"},
    ],
)
```

The MCP toolset defaults to `always_ask` permission policy.

## Provide Auth at Session Creation

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
```

If authorization credentials are invalid, session creation succeeds but a `session.error` event is emitted. Authentication retries happen on the next idle-to-running transition.

## Supported MCP Server Types

Claude Managed Agents connects to remote MCP servers that expose an HTTP endpoint. The server must support MCP protocol's streamable HTTP transport.

---

# Authenticate with Vaults

Vaults and credentials let you register credentials for third-party services once and reference them by ID at session creation.

## Create a Vault

```python
vault = client.beta.vaults.create(
    display_name="Alice",
    metadata={"external_user_id": "usr_abc123"},
)
```

Vaults and credentials are workspace-scoped - anyone with API key access can use them.

## Add a Credential

Each credential binds to a single `mcp_server_url`. Two types are supported:

### MCP OAuth Credential

Use when the MCP server uses OAuth 2.0:

```python
credential = client.beta.vaults.credentials.create(
    vault_id=vault.id,
    display_name="Alice's Slack",
    auth={
        "type": "mcp_oauth",
        "mcp_server_url": "https://mcp.slack.com/mcp",
        "access_token": "xoxp-...",
        "expires_at": "2026-04-15T00:00:00Z",
        "refresh": {
            "token_endpoint": "https://slack.com/api/oauth.v2.access",
            "client_id": "1234567890.0987654321",
            "scope": "channels:read chat:write",
            "refresh_token": "xoxe-1-...",
            "token_endpoint_auth": {"type": "client_secret_post", "client_secret": "abc123..."},
        },
    },
)
```

The `refresh.token_endpoint_auth.type` field options:
- `none` - public client
- `client_secret_basic` - HTTP Basic auth
- `client_secret_post` - client secret in POST body

### Static Bearer Credential

Use when the MCP server accepts a fixed bearer token:

```python
credential = client.beta.vaults.credentials.create(
    vault_id=vault.id,
    display_name="Linear API key",
    auth={
        "type": "static_bearer",
        "mcp_server_url": "https://mcp.linear.app/mcp",
        "token": "lin_api_your_linear_key",
    },
)
```

### Credential Constraints

- One active credential per `mcp_server_url` per vault (409 if duplicate)
- `mcp_server_url` is immutable after creation
- Maximum 20 credentials per vault
- Secret fields are write-only (never returned in API responses)

## Rotate a Credential

Only the secret payload and metadata are mutable:

```python
client.beta.vaults.credentials.update(
    credential.id,
    vault_id=vault.id,
    auth={
        "type": "mcp_oauth",
        "access_token": "xoxp-new-...",
        "expires_at": "2026-05-15T00:00:00Z",
        "refresh": {"refresh_token": "xoxe-1-new-..."},
    },
)
```

## Other Operations

- List vaults or credentials - Paginated, newest first; pass `include_archived=true` for archived records
- Archive a vault - Cascades to all credentials; secrets are purged, records retained for auditing
- Archive a credential - Purges secret payload; frees the `mcp_server_url` for a replacement
- Delete a vault or credential - Hard delete, no record retained

---

# Skills

Skills are reusable, filesystem-based resources that give your agent domain-specific expertise. Unlike prompts, skills load on demand.

## Skill Types

| Field | Description |
| --- | --- |
| `type` | Either `anthropic` for pre-built skills or `custom` for organization-authored skills |
| `skill_id` | For Anthropic skills, use the short name (e.g., `xlsx`). For custom skills, use the `skill_*` ID. |
| `version` | Custom skills only. Pin to a specific version or use `latest`. |

## Enable Skills on an Agent

```python
agent = client.beta.agents.create(
    name="Financial Analyst",
    model="claude-sonnet-4-6",
    system="You are a financial analysis agent.",
    skills=[
        {"type": "anthropic", "skill_id": "xlsx"},
        {"type": "custom", "skill_id": "skill_abc123", "version": "latest"},
    ],
)
```

Maximum of 20 skills per session (includes skills across all agents in multi-agent sessions).

Pre-built Anthropic skills include: PowerPoint, Excel, Word, and PDF handling.

---

# Adding Files

Upload files via the Files API and mount them in the session's container.

## Upload a File

```python
file = client.beta.files.upload(file=Path("data.csv"))
```

## Mount Files in a Session

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "file",
            "file_id": file.id,
            "mount_path": "/workspace/data.csv",
        },
    ],
)
```

Maximum 100 files per session. Files are mounted as read-only copies.

## Managing Files on a Running Session

```python
# Add a file
resource = client.beta.sessions.resources.add(
    session.id,
    type="file",
    file_id=file.id,
)

# List resources
listed = client.beta.sessions.resources.list(session.id)

# Remove a file
client.beta.sessions.resources.delete(resource.id, session_id=session.id)
```

## Listing and Downloading Session Files

```python
# List files associated with a session
files = client.beta.files.list(scope_id="sess_abc123")

# Download a file
content = client.beta.files.download(files.data[0].id)
content.write_to_file("output.txt")
```

---

# Multiagent Sessions (Research Preview)

Multi-agent orchestration lets one agent coordinate with others. Agents can act in parallel with their own isolated context.

## How It Works

All agents share the same container and filesystem, but each agent runs in its own session thread (context-isolated event stream). The coordinator reports activity in the primary thread; additional threads are spawned at runtime.

Threads are persistent - follow-ups retain context from previous turns. Each agent uses its own configuration (model, system prompt, tools, MCP servers, skills).

### Good Delegation Examples

- Code review - A reviewer agent with focused system prompt and read-only tools
- Test generation - A test agent that writes and runs tests
- Research - A search agent with web tools that summarizes findings

## Declare Callable Agents

```python
orchestrator = client.beta.agents.create(
    name="Engineering Lead",
    model="claude-sonnet-4-6",
    system="You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
    tools=[{"type": "agent_toolset_20260401"}],
    callable_agents=[
        {"type": "agent", "id": reviewer_agent.id, "version": reviewer_agent.version},
        {"type": "agent", "id": test_writer_agent.id, "version": test_writer_agent.version},
    ],
)
```

Only one level of delegation is supported - the coordinator can call other agents, but those agents cannot call agents of their own.

## Session Threads

The session-level event stream is the primary thread. Session threads let you drill into specific agent reasoning and tool calls.

```python
# List all threads
for thread in client.beta.sessions.threads.list(session.id):
    print(f"[{thread.agent_name}] {thread.status}")

# Stream events from a specific thread
with client.beta.sessions.threads.stream(thread.id, session_id=session.id) as stream:
    for event in stream:
        # process events...
        pass
```

## Multiagent Event Types

| Type | Description |
| --- | --- |
| `session.thread_created` | Coordinator spawned a new thread |
| `session.thread_idle` | An agent thread finished its current work |
| `agent.thread_message_sent` | Agent sent a message to another thread |
| `agent.thread_message_received` | Agent received a message from another thread |

## Tool Permissions in Threads

When a callable_agent thread needs tool confirmation or custom tool result, the request surfaces on the session stream with a `session_thread_id` field. Echo the same `session_thread_id` when you post your response.

---

# Console (Prototype in Console)

Console provides a visual interface for creating and configuring agents at https://platform.claude.com/workspaces/default/agent-quickstart/

## Building an Agent in Console

- Model and system prompt - Pick a model and write the system prompt
- MCP servers - Add remote MCP servers by URL and authenticate
- Tools - Extend capabilities using pre-built agent toolset and MCP tools
- Skills - Attach Anthropic or custom skills

As you configure, Console shows the equivalent API request for copying into your code.

## Testing

Console includes an inline session runner. After configuring your agent, start a test session directly, send messages, and watch the event stream without leaving the page.

## From Prototype to Code

1. Copy the agent ID from Console output
2. Reference it in your code when creating sessions

---

# Branding Guidelines

For partners integrating Claude Managed Agents:

Allowed:
- "Claude Agent" (preferred for dropdown menus)
- "Claude" (when within a menu already labeled "Agents")
- "{YourAgentName} Powered by Claude"

Not permitted:
- "Claude Code" or "Claude Code Agent"
- "Claude Cowork" or "Claude Cowork Agent"
- Claude Code-branded ASCII art or visual elements
