---
title: "Embeddings"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/embeddings"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Embeddings

Text embeddings are numerical representations of text that enable measuring semantic similarity. This guide introduces embeddings, their applications, and how to use embedding models for tasks like search, recommendations, and anomaly detection.

## Before Implementing Embeddings

When selecting an embeddings provider, consider:

- **Dataset size and domain specificity**: Size of the model training dataset and its relevance to your domain
- **Inference performance**: Embedding lookup speed and end-to-end latency, especially important for large scale production deployments
- **Customization**: Options for continued training on private data or specialization for specific domains

## How to Get Embeddings with Anthropic

Anthropic does not offer its own embedding model. Voyage AI is recommended as an embeddings provider with a wide variety of options and capabilities. Voyage AI makes state-of-the-art embedding models and offers customized models for specific industry domains such as finance and healthcare.

## Available Models

Voyage recommends the following text embedding models:

| Model | Context Length | Embedding Dimension | Description |
|-------|---------------|-------------------|-------------|
| `voyage-3-large` | 32,000 | 1024 (default) | Best general-purpose and multilingual retrieval quality |
| `voyage-3.5` | 32,000 | 1024 (default) | Optimized for general-purpose and multilingual retrieval |
| `voyage-3.5-lite` | 32,000 | 1024 (default) | Optimized for latency and cost |
| `voyage-code-3` | 32,000 | 1024 (default) | Optimized for code retrieval |
| `voyage-finance-2` | 32,000 | 1024 | Optimized for finance retrieval and RAG |
| `voyage-law-2` | 16,000 | 1024 | Optimized for legal and long-context retrieval |

Multimodal embedding model:

| Model | Context Length | Embedding Dimension | Description |
|-------|---------------|-------------------|-------------|
| `voyage-multimodal-3` | 32,000 | 1024 | Rich multimodal embedding for interleaved text and images |

## Getting Started with Voyage AI

1. Sign up on Voyage AI's website
2. Obtain an API key
3. Set the API key as an environment variable:

```bash
export VOYAGE_API_KEY="<your secret key>"
```

### Voyage Python Library

```bash
pip install -U voyageai
```

```python
import voyageai

vo = voyageai.Client()
texts = ["Sample text 1", "Sample text 2"]
result = vo.embed(texts, model="voyage-3.5", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

### Voyage HTTP API

```bash
curl https://api.voyageai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "input": ["Sample text 1", "Sample text 2"],
    "model": "voyage-3.5"
  }'
```

## Quickstart Example

Embed documents and perform semantic search using dot-product similarity:

```python
import voyageai
import numpy as np

vo = voyageai.Client()

documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables...",
    "Photosynthesis in plants converts light energy into glucose...",
    "20th-century innovations centered on electronic advancements...",
    "Rivers provide water, irrigation, and habitat for aquatic species...",
    "Apple's conference call is scheduled for Thursday, November 2, 2023...",
    "Shakespeare's works endure in literature...",
]

doc_embds = vo.embed(documents, model="voyage-3.5", input_type="document").embeddings

query = "When is Apple's conference call scheduled?"
query_embd = vo.embed([query], model="voyage-3.5", input_type="query").embeddings[0]

similarities = np.dot(doc_embds, query_embd)
retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
```

## Similarity Functions

Use dot-product similarity, cosine similarity, or Euclidean distance. Voyage AI embeddings are normalized to length 1, so cosine similarity is equivalent to dot-product similarity.

## Quantization

Supported quantization options include float (default), int8, uint8, binary, and ubinary. Quantization reduces storage and costs by 4x to 32x.
