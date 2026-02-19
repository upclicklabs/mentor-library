---
title: "Connect Claude Code with Google Vertex or Amazon Bedrock"
source_url: "https://docs.anthropic.com/en/docs/claude-code/enterprise-setup"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Connect Claude Code with Google Vertex or Amazon Bedrock

Organizations can deploy Claude Code through Anthropic directly or through a cloud provider. This page helps you choose the right configuration.

## Compare deployment options

For most organizations, Claude for Teams or Claude for Enterprise provides the best experience. Team members get access to both Claude Code and Claude on the web with a single subscription, centralized billing, and no infrastructure setup required.

**Claude for Teams** is self-service and includes collaboration features, admin tools, and billing management. Best for smaller teams that need to get started quickly.

**Claude for Enterprise** adds SSO and domain capture, role-based permissions, compliance API access, and managed policy settings for deploying organization-wide Claude Code configurations. Best for larger organizations with security and compliance requirements.

### Feature comparison

| Feature | Claude for Teams/Enterprise | Anthropic Console | Amazon Bedrock | Google Vertex AI | Microsoft Foundry |
|---|---|---|---|---|---|
| Best for | Most organizations (recommended) | Individual developers | AWS-native deployments | GCP-native deployments | Azure-native deployments |
| Billing | Teams: $150/seat (Premium) with PAYG available; Enterprise: Contact Sales | PAYG | PAYG through AWS | PAYG through GCP | PAYG through Azure |
| Prompt caching | Enabled by default | Enabled by default | Enabled by default | Enabled by default | Enabled by default |
| Authentication | Claude.ai SSO or email | API key | API key or AWS credentials | GCP credentials | API key or Microsoft Entra ID |
| Cost tracking | Usage dashboard | Usage dashboard | AWS Cost Explorer | GCP Billing | Azure Cost Management |
| Includes Claude on web | Yes | No | No | No | No |

### Setup options

- Claude for Teams or Enterprise: Authentication setup
- Anthropic Console: Console authentication
- Amazon Bedrock: Bedrock setup
- Google Vertex AI: Vertex AI setup
- Microsoft Foundry: Foundry setup

## Configure proxies and gateways

Most organizations can use a cloud provider directly without additional configuration. However, you may need to configure a corporate proxy or LLM gateway if your organization has specific network or management requirements.

- **Corporate proxy**: Routes traffic through an HTTP/HTTPS proxy. Use this if your organization requires all outbound traffic to pass through a proxy server for security monitoring, compliance, or network policy enforcement. Configure with the `HTTPS_PROXY` or `HTTP_PROXY` environment variables.
- **LLM Gateway**: A service that sits between Claude Code and the cloud provider to handle authentication and routing. Use this if you need centralized usage tracking across teams, custom rate limiting or budgets, or centralized authentication management. Configure with the `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, or `ANTHROPIC_VERTEX_BASE_URL` environment variables.

### Amazon Bedrock

#### Corporate proxy

```bash
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

#### LLM Gateway

```bash
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1

# Configure LLM gateway
export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # If gateway handles AWS auth
```

### Google Vertex AI

#### Corporate proxy

```bash
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

#### LLM Gateway

```bash
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1

# Configure LLM gateway
export ANTHROPIC_VERTEX_BASE_URL='https://your-llm-gateway.com/vertex'
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1  # If gateway handles GCP auth
```

### Microsoft Foundry

#### Corporate proxy

```bash
# Enable Microsoft Foundry
export CLAUDE_CODE_USE_FOUNDRY=1
export ANTHROPIC_FOUNDRY_RESOURCE=your-resource
export ANTHROPIC_FOUNDRY_API_KEY=your-api-key  # Or omit for Entra ID auth

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

#### LLM Gateway

```bash
# Enable Microsoft Foundry
export CLAUDE_CODE_USE_FOUNDRY=1

# Configure LLM gateway
export ANTHROPIC_FOUNDRY_BASE_URL='https://your-llm-gateway.com'
export CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1  # If gateway handles Azure auth
```

Use `/status` in Claude Code to verify your proxy and gateway configuration is applied correctly.

## Best practices for organizations

### Invest in documentation and memory

Organizations can deploy CLAUDE.md files at multiple levels:

- **Organization-wide**: Deploy to system directories like `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) for company-wide standards
- **Repository-level**: Create `CLAUDE.md` files in repository roots containing project architecture, build commands, and contribution guidelines. Check these into source control so all users benefit

### Simplify deployment

If you have a custom development environment, creating a "one click" way to install Claude Code is key to growing adoption across an organization.

### Start with guided usage

Encourage new users to try Claude Code for codebase Q&A, or on smaller bug fixes or feature requests. Ask Claude Code to make a plan. Check Claude's suggestions and give feedback if it's off-track.

### Pin model versions for cloud providers

If you deploy through Bedrock, Vertex AI, or Foundry, pin specific model versions using `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `ANTHROPIC_DEFAULT_HAIKU_MODEL`. Without pinning, Claude Code aliases resolve to the latest version, which can break users when Anthropic releases a new model that isn't yet enabled in your account.

### Configure security policies

Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration.

### Leverage MCP for integrations

MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs. One central team can configure MCP servers and check a `.mcp.json` configuration into the codebase so that all users benefit.

## Next steps

1. Roll out to your team: Share installation instructions and have team members install Claude Code and authenticate with their credentials.
2. Set up shared configuration: Create a CLAUDE.md file in your repositories to help Claude Code understand your codebase and coding standards.
3. Configure permissions: Review security settings to define what Claude Code can and cannot do in your environment.
