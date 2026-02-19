---
title: "Use Voyage AI for embeddings"
source_url: "https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/VoyageAI/how_to_create_embeddings.md"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use Voyage AI for embeddings

## Overview

Text embeddings are numerical representations of text strings, represented as vectors of floating-point numbers. The distance between two text embeddings (commonly using cosine similarity) measures how related two pieces of text are, with smaller distances indicating higher relatedness.

Embeddings enable applications like:
- **Search** (popular in RAG architectures)
- **Recommendations**
- **Anomaly detection**

## How to Get Embeddings with Anthropic

Anthropic has partnered with Voyage AI as the preferred provider for text embeddings. Voyage offers state-of-the-art embedding models, including industry-specific versions for finance and healthcare.

### Setup

1. Sign up at Voyage AI's dashboard
2. Obtain an API key and set it as an environment variable:

```bash
export VOYAGE_API_KEY="<your secret key>"
```

## Installation and Usage

### Voyage Python Package

```bash
pip install -U voyageai
```

Basic usage:

```python
import voyageai

vo = voyageai.Client()

texts = ["Sample text 1", "Sample text 2"]
result = vo.embed(texts, model="voyage-2", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

**Parameters:**
- **texts** (List[str]): List of strings to embed (max 128 items, 320K tokens for voyage-2, 120K for voyage-code-2)
- **model** (str): Model name - `voyage-2` (default) or `voyage-code-2`
- **input_type** (str, optional): `None` (default), `query`, or `document`. Use `query` for search queries and `document` for documents to enhance retrieval quality.
- **truncation** (bool, optional): How to handle over-length texts

### Voyage HTTP API

**Endpoint:** `https://api.voyageai.com/v1/embeddings` (POST)

```bash
curl https://api.voyageai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "input": ["Sample text 1", "Sample text 2"],
    "model": "voyage-2"
  }'
```

### AWS Marketplace

Voyage embeddings are also available on AWS Marketplace:

1. Navigate to the model listing and subscribe
2. Review and accept terms
3. Note the Product ARN for your region
4. Deploy using the provided SageMaker notebook

## Available Models

| Model | Context Length | Embedding Dimension | Description |
|-------|---------------|-------------------|-------------|
| `voyage-2` | 4000 | 1024 | Latest generalist model with best retrieval quality |
| `voyage-code-2` | 16000 | 1536 | Optimized for code retrieval (17% better than alternatives) |

**Coming soon:** `voyage-finance-2`, `voyage-law-2`, `voyage-multilingual-2`, `voyage-healthcare-2`

## Motivating Example: Semantic Search

```python
documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple's conference call to discuss fourth fiscal quarter results is scheduled for Thursday, November 2, 2023.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature."
]

# Embed documents
doc_embds = vo.embed(documents, model="voyage-2", input_type="document").embeddings

# Query
query = "When is Apple's conference call scheduled?"
query_embd = vo.embed([query], model="voyage-2", input_type="query").embeddings[0]

# Find most relevant document using cosine similarity
import numpy as np
similarities = np.dot(doc_embds, query_embd)
retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
```

## FAQ

### How do I calculate the distance between two embedding vectors?

Use cosine similarity. Voyage embeddings are normalized to length 1, so cosine similarity equals dot-product:

```python
import numpy as np
similarity = np.dot(embd1, embd2)
```

### Can I count the number of tokens in a string before embedding it?

Yes:

```python
import voyageai
vo = voyageai.Client()
total_tokens = vo.count_tokens(["Sample text"])
```

## Pricing

See Voyage AI's pricing page for current pricing details.
