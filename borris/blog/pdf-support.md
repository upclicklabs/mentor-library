---
title: "PDF Support"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/pdf-support"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# PDF Support

Process PDFs with Claude. Extract text, analyze charts, and understand visual content from your documents.

## Use Cases

- Analyzing financial reports and understanding charts/tables
- Extracting key information from legal documents
- Translation assistance for documents
- Converting document information into structured formats

## PDF Requirements

| Requirement | Limit |
|------------|--------|
| Maximum request size | 32MB |
| Maximum pages per request | 100 |
| Format | Standard PDF (no passwords/encryption) |

Both limits are on the entire request payload, including any other content sent alongside PDFs. Since PDF support relies on Claude's vision capabilities, it is subject to the same limitations as other vision tasks.

## Supported Platforms and Models

PDF support is currently supported via direct API access and Google Vertex AI. All active models support PDF processing. PDF support is also available on Amazon Bedrock.

### Amazon Bedrock PDF Support

Two distinct document processing modes exist:

1. **Converse Document Chat** (Text extraction only): Provides basic text extraction from PDFs. Cannot analyze images, charts, or visual layouts. Uses approximately 1,000 tokens for a 3-page PDF. Automatically used when citations are not enabled.

2. **Claude PDF Chat** (Full visual understanding): Provides complete visual analysis of PDFs. Can understand charts, graphs, images, and visual layouts. Uses approximately 7,000 tokens for a 3-page PDF. Requires citations to be enabled in the Converse API.

## Process PDFs with Claude

You can provide PDFs to Claude in three ways:

### Option 1: URL-based PDF document

Reference a PDF directly from a URL using the `document` content block with `source.type: "url"`.

### Option 2: Base64-encoded PDF document

Send PDFs from your local system using base64 encoding with `source.type: "base64"` and `media_type: "application/pdf"`.

### Option 3: Files API

For PDFs you'll use repeatedly, upload via the Files API and reference with `source.type: "file"` and a `file_id`.

## How PDF Support Works

1. The system converts each page into an image and extracts text from each page
2. Claude analyzes both the text and images to understand the document
3. Claude responds, referencing both textual and visual content

## Estimate Your Costs

- **Text token costs**: Each page typically uses 1,500-3,000 tokens depending on content density
- **Image token costs**: Each page is converted into an image with standard image-based cost calculations

## Optimize PDF Processing

### Improve Performance

- Place PDFs before text in your requests
- Use standard fonts
- Ensure text is clear and legible
- Rotate pages to proper upright orientation
- Use logical page numbers in prompts
- Split large PDFs into chunks when needed
- Enable prompt caching for repeated analysis

### Scale Your Implementation

#### Use Prompt Caching

Cache PDFs to improve performance on repeated queries by adding `cache_control: {"type": "ephemeral"}` to the document content block.

#### Process Document Batches

Use the Message Batches API for high-volume workflows to process multiple PDFs efficiently.
