---
title: "Claude on Vertex AI"
source_url: "https://docs.anthropic.com/en/api/claude-on-vertex-ai"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Claude on Vertex AI

Anthropic's Claude models are now generally available through Vertex AI.

The Vertex API for accessing Claude is nearly-identical to the Messages API and supports all of the same options, with two key differences:

- In Vertex, `model` is not passed in the request body. Instead, it is specified in the Google Cloud endpoint URL.
- In Vertex, `anthropic_version` is passed in the request body (rather than as a header), and must be set to the value `vertex-2023-10-16`.

Vertex is also supported by Anthropic's official client SDKs.

## Install an SDK for Accessing Vertex AI

### Python
```bash
pip install -U google-cloud-aiplatform "anthropic[vertex]"
```

### TypeScript
```bash
npm install @anthropic-ai/vertex-sdk
```

### Java (Gradle)
```groovy
implementation("com.anthropic:anthropic-java-vertex:2.+")
```

### Go
```bash
go get github.com/anthropics/anthropic-sdk-go
```

### Ruby
```ruby
gem "anthropic"
gem "googleauth"
```

Note: The PHP SDK does not currently support Google Vertex AI.

## Model Availability

Anthropic model availability varies by region. Search for "Claude" in the Vertex AI Model Garden for the latest information.

### API Model IDs

| Model | Vertex AI API model ID |
|-------|----------------------|
| Claude Opus 4.6 | claude-opus-4-6 |
| Claude Sonnet 4.6 | claude-sonnet-4-6 |
| Claude Sonnet 4.5 | claude-sonnet-4-5@20250929 |
| Claude Sonnet 4 | claude-sonnet-4@20250514 |
| Claude Opus 4.5 | claude-opus-4-5@20251101 |
| Claude Opus 4.1 | claude-opus-4-1@20250805 |
| Claude Opus 4 | claude-opus-4@20250514 |
| Claude Haiku 4.5 | claude-haiku-4-5@20251001 |

## Making Requests

Before running requests you may need to run `gcloud auth application-default login` to authenticate with GCP.

### Python Example

```python
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "global"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

### TypeScript Example

```typescript
import { AnthropicVertex } from "@anthropic-ai/vertex-sdk";

const projectId = "MY_PROJECT_ID";
const region = "global";

const client = new AnthropicVertex({ projectId, region });

async function main() {
  const result = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 100,
    messages: [{ role: "user", content: "Hey Claude!" }]
  });
  console.log(JSON.stringify(result, null, 2));
}

main();
```

### Shell Example

```bash
MODEL_ID=claude-opus-4-6
LOCATION=global
PROJECT_ID=MY_PROJECT_ID

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://$LOCATION-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/anthropic/models/${MODEL_ID}:streamRawPredict -d \
'{
  "anthropic_version": "vertex-2023-10-16",
  "messages": [{"role": "user", "content": "Hey Claude!"}],
  "max_tokens": 100
}'
```

## Activity Logging

Vertex provides a request-response logging service that allows customers to log the prompts and completions associated with usage. Anthropic recommends logging activity on at least a 30-day rolling basis.

## Global vs Regional Endpoints

Starting with Claude Sonnet 4.5 and all future models, Google Vertex AI offers two endpoint types:

- **Global endpoints**: Dynamic routing for maximum availability (recommended, no pricing premium)
- **Regional endpoints**: Guaranteed data routing through specific geographic regions (10% pricing premium)

### When to Use Each Option

**Global endpoints (recommended):**
- Maximum availability and uptime
- Dynamic routing to regions with available capacity
- Best for applications where data residency is flexible
- Only supports pay-as-you-go traffic

**Regional endpoints:**
- Route traffic through specific geographic regions
- Required for data residency and compliance requirements
- Support both pay-as-you-go and provisioned throughput

### Implementation

Set the region parameter to "global" for global endpoints, or specify a specific region like "us-east1" for regional endpoints.

Claude is also available through Amazon Bedrock and Microsoft Foundry.
