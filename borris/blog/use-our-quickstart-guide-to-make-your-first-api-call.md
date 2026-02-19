---
title: "Use our quickstart guide to make your first API call"
source_url: "https://docs.anthropic.com/en/docs/get-started"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use our quickstart guide to make your first API call

Make your first API call to Claude and build a simple web search assistant.

## Prerequisites

- An Anthropic Console account
- An API key

## Call the API

### cURL

1. Set your API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

2. Make your first API call:
```bash
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user",
        "content": "What should I search for to find the latest developments in renewable energy?"
      }
    ]
  }'
```

### Python

1. Set your API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

2. Install the SDK:
```bash
pip install anthropic
```

3. Create your code (save as quickstart.py):
```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
        }
    ],
)
print(message.content)
```

4. Run your code:
```bash
python quickstart.py
```

### TypeScript

1. Set your API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

2. Install the SDK:
```bash
npm install @anthropic-ai/sdk
```

3. Create your code (save as quickstart.ts):
```typescript
import Anthropic from "@anthropic-ai/sdk";

async function main() {
  const anthropic = new Anthropic();

  const msg = await anthropic.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1000,
    messages: [
      {
        role: "user",
        content: "What should I search for to find the latest developments in renewable energy?"
      }
    ]
  });
  console.log(msg);
}

main().catch(console.error);
```

4. Run your code:
```bash
npx tsx quickstart.ts
```

### Java

1. Set your API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

2. Install the SDK - add the Anthropic Java SDK to your project:

Gradle:
```groovy
implementation("com.anthropic:anthropic-java:1.0.0")
```

Maven:
```xml
<dependency>
  <groupId>com.anthropic</groupId>
  <artifactId>anthropic-java</artifactId>
  <version>1.0.0</version>
</dependency>
```

3. Create your code (save as QuickStart.java):
```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;

public class QuickStart {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    MessageCreateParams params = MessageCreateParams.builder()
      .model("claude-opus-4-6")
      .maxTokens(1000)
      .addUserMessage(
        "What should I search for to find the latest developments in renewable energy?"
      )
      .build();

    Message message = client.messages().create(params);
    System.out.println(message.content());
  }
}
```

4. Run your code:
```bash
javac QuickStart.java
java QuickStart
```

## Next steps

Now that you have made your first Claude API request, explore what else is possible:

- Working with Messages: Learn common patterns for the Messages API
- Features Overview: Explore Claude's advanced features and capabilities
- Client SDKs: Discover Anthropic client libraries
- Claude Cookbook: Learn with interactive Jupyter notebooks
