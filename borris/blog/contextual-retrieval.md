---
title: "Contextual Retrieval"
source_url: "https://www.anthropic.com/news/contextual-retrieval"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Contextual Retrieval

Published: September 19, 2024

## Overview

AI systems often require access to specialized background knowledge to function effectively in specific contexts. Developers typically enhance AI capabilities using Retrieval-Augmented Generation (RAG), which retrieves relevant information from knowledge bases and appends it to user prompts.

However, traditional RAG implementations face a critical limitation: they frequently eliminate contextual information during the encoding process, resulting in failed retrievals of necessary data.

## The Innovation

Anthropic introduced "Contextual Retrieval," a method combining two techniques:

- Contextual Embeddings
- Contextual BM25

This approach can reduce retrieval failures by 49%, and when paired with reranking, by 67%, yielding substantial improvements in retrieval accuracy and downstream task performance.

## Understanding RAG Systems

Traditional RAG operates through these steps:

1. Fragment knowledge bases into smaller text chunks
2. Convert chunks into vector embeddings capturing semantic meaning
3. Store embeddings in searchable vector databases

At runtime, semantic similarity identifies relevant chunks for inclusion in prompts sent to generative models. While embedding models excel at semantic relationships, they may miss exact matches. BM25, a lexical ranking function, addresses this gap by finding precise word and phrase matches.

## The Context Problem

Traditional RAG fragments documents for efficient retrieval, but isolated chunks often lack sufficient context. For example, a financial database query might retrieve a chunk that simply states a revenue figure without specifying which company or timeframe, rendering it unhelpful.

## The Solution

Contextual Retrieval prepends explanatory chunk-specific context before embedding and indexing. Rather than manually annotating millions of chunks, Anthropic uses Claude to generate concise, targeted context explaining how each chunk fits within its broader document.

The prompt structure instructs Claude to provide succinct contextual explanations, typically 50-100 tokens, that are prepended to chunks before processing.

Cost Efficiency: By leveraging prompt caching, the one-time cost to generate contextualized chunks is approximately $1.02 per million document tokens.

## Performance Results

Experiments across codebases, fiction, academic papers, and scientific literature demonstrated consistent improvements:

- Contextual Embeddings alone reduced failure rates by 35% (5.7% to 3.7%)
- Combined with BM25, failure rates dropped 49% (5.7% to 2.9%)
- With reranking added, failure rates decreased 67% (5.7% to 1.9%)

## Implementation Considerations

- Chunk boundaries significantly affect retrieval performance based on size, boundaries, and overlap choices
- Embedding model selection matters - different models benefit variably from contextualization
- Custom prompts tailored to specific domains may outperform generic templates
- Chunk quantity impacts results; testing with 5, 10, and 20 chunks revealed 20 to be most effective
- Evaluation remains essential

## Reranking Integration

Adding reranking substantially amplifies improvements:

1. Initial retrieval identifying top 150 potentially relevant chunks
2. Passing chunks and queries through reranking models
3. Scoring chunks for relevance and importance
4. Selecting top 20 chunks for final prompt inclusion

## Key Findings

- Embeddings plus BM25 outperforms embeddings alone
- Voyage and Gemini embeddings excel compared to alternatives
- Twenty chunks prove more effective than ten or five
- Context addition substantially improves accuracy
- Reranking consistently enhances retrieval quality
- All benefits compound together for optimal performance

## Conclusion

Developers working with knowledge bases should experiment with combining contextual embeddings (Voyage or Gemini), contextual BM25, reranking, and twenty-chunk retrieval to achieve superior performance levels.
