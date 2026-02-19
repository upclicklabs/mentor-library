---
title: "Batch Processing"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/batch-processing"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Batch Processing

Batch processing is a powerful approach for handling large volumes of requests efficiently. Instead of processing requests one at a time with immediate responses, batch processing allows you to submit multiple requests together for asynchronous processing.

This is particularly useful when:
- You need to process large volumes of data
- Immediate responses are not required
- You want to optimize for cost efficiency
- You're running large-scale evaluations or analyses

## Message Batches API

The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput.

### How It Works

1. The system creates a new Message Batch with the provided Messages requests
2. The batch is then processed asynchronously, with each request handled independently
3. You can poll for the status of the batch and retrieve results when processing has ended

### Use Cases

- Large-scale evaluations: Process thousands of test cases efficiently
- Content moderation: Analyze large volumes of user-generated content asynchronously
- Data analysis: Generate insights or summaries for large datasets
- Bulk content generation: Create large amounts of text for various purposes

### Batch Limitations

- Limited to either 100,000 Message requests or 256 MB in size, whichever is reached first
- Most batches complete within 1 hour; batches expire if processing does not complete within 24 hours
- Results are available for 29 days after creation
- Batches are scoped to a Workspace

### Supported Models

All active models support the Message Batches API.

### What Can Be Batched

Any request that you can make to the Messages API can be included in a batch, including vision, tool use, system messages, multi-turn conversations, and any beta features. Each request is processed independently, so you can mix different types within a single batch.

## Pricing

All usage is charged at 50% of the standard API prices.

| Model | Batch Input | Batch Output |
|-------|-------------|--------------|
| Claude Opus 4.6 | $2.50 / MTok | $12.50 / MTok |
| Claude Opus 4.5 | $2.50 / MTok | $12.50 / MTok |
| Claude Opus 4.1 | $7.50 / MTok | $37.50 / MTok |
| Claude Opus 4 | $7.50 / MTok | $37.50 / MTok |
| Claude Sonnet 4.6 | $1.50 / MTok | $7.50 / MTok |
| Claude Sonnet 4.5 | $1.50 / MTok | $7.50 / MTok |
| Claude Sonnet 4 | $1.50 / MTok | $7.50 / MTok |
| Claude Haiku 4.5 | $0.50 / MTok | $2.50 / MTok |
| Claude Haiku 3.5 | $0.40 / MTok | $2 / MTok |
| Claude Haiku 3 | $0.125 / MTok | $0.625 / MTok |

## How to Use

### Prepare and Create Your Batch

A Message Batch is composed of a list of requests, each with:
- A unique custom_id for identifying the Messages request
- A params object with the standard Messages API parameters

### Tracking Your Batch

The processing_status field indicates the stage: starts as in_progress, then updates to ended once all requests finish. Monitor via the Console or the retrieval endpoint.

### Retrieving Batch Results

Once processing ends, each request will have one of four result types:

| Result Type | Description |
|-------------|-------------|
| succeeded | Request was successful, includes the message result |
| errored | Request encountered an error, not billed |
| canceled | User canceled the batch before this request could be sent, not billed |
| expired | Batch reached 24 hour expiration, not billed |

Results are in .jsonl format. Results may not match input order - use custom_id to match.

### Canceling a Batch

You can cancel a batch currently processing. It will transition to canceling status and may contain partial results for requests processed before cancellation.

### Using Prompt Caching with Batches

Prompt caching is supported and pricing discounts stack with batch discounts. Cache hits are best-effort, with typical rates ranging from 30% to 98%. To maximize cache hits:

1. Include identical cache_control blocks in every request
2. Maintain a steady stream of requests to prevent cache expiration
3. Structure requests to share as much cached content as possible

## Best Practices

- Monitor batch processing status regularly and implement retry logic for failed requests
- Use meaningful custom_id values since order is not guaranteed
- Consider breaking very large datasets into multiple batches
- Dry run a single request shape with the Messages API to avoid validation errors
- Batch results are available for 29 days after batch created_at time

## Storage and Privacy

- Batches are isolated within the Workspace they are created in
- Each request within a batch is processed independently with no data leakage
- Results follow Anthropic's data retention policy
