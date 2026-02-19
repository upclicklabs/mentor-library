---
title: "Files API"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/files"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Files API

The Files API lets you upload and manage files to use with the Claude API without re-uploading content with each request. This is particularly useful when using the code execution tool to provide inputs (e.g. datasets and documents) and then download outputs (e.g. charts). You can also use the Files API to prevent having to continually re-upload frequently used documents and images across multiple API calls.

Note: The Files API is currently in beta.

Note: This feature is in beta and is not covered by Zero Data Retention (ZDR) arrangements.

## Supported models

Referencing a file_id in a Messages request is supported in all models that support the given file type. For example, images are supported in all Claude 3+ models, PDFs in all Claude 3.5+ models, and various other file types for the code execution tool in Claude Haiku 4.5 plus all Claude 3.7+ models.

The Files API is currently not supported on Amazon Bedrock or Google Vertex AI.

## How the Files API works

The Files API provides a simple create-once, use-many-times approach for working with files:

- Upload files to secure storage and receive a unique file_id
- Download files that are created from skills or the code execution tool
- Reference files in Messages requests using the file_id instead of re-uploading content
- Manage your files with list, retrieve, and delete operations

## How to use the Files API

To use the Files API, you'll need to include the beta feature header: anthropic-beta: files-api-2025-04-14.

### Uploading a file

Upload a file to be referenced in future API calls:

```bash
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@/path/to/document.pdf"
```

```python
import anthropic

client = anthropic.Anthropic()
client.beta.files.upload(
    file=("document.pdf", open("/path/to/document.pdf", "rb"), "application/pdf"),
)
```

### Using a file in messages

Once uploaded, reference the file using its file_id in a document content block:

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Please summarize this document for me."},
                {
                    "type": "document",
                    "source": {
                        "type": "file",
                        "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
                    },
                },
            ],
        }
    ],
    betas=["files-api-2025-04-14"],
)
```

### File types and content blocks

| File Type | MIME Type | Content Block Type | Use Case |
| :--- | :--- | :--- | :--- |
| PDF | application/pdf | document | Text analysis, document processing |
| Plain text | text/plain | document | Text analysis, processing |
| Images | image/jpeg, image/png, image/gif, image/webp | image | Image analysis, visual tasks |
| Datasets, others | Varies | container_upload | Analyze data, create visualizations |

### Managing files

- List files: GET /v1/files
- Get file metadata: GET /v1/files/{file_id}
- Delete a file: DELETE /v1/files/{file_id}
- Download a file: GET /v1/files/{file_id}/content (only for files created by skills or code execution tool)

## File storage and limits

- Maximum file size: 500 MB per file
- Total storage: 100 GB per organization
- Files persist until you delete them
- Files are scoped to the workspace of the API key

## Usage and billing

File API operations are free (uploading, downloading, listing, getting metadata, deleting). File content used in Messages requests are priced as input tokens.

### Rate limits

During the beta period, file-related API calls are limited to approximately 100 requests per minute.
