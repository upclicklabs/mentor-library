---
title: "Get started with vision"
source_url: "https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/getting_started_with_vision.ipynb"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Get started with vision

## Overview

This is a Jupyter notebook tutorial from Anthropic's anthropic-cookbook repository that demonstrates how to use Claude's vision capabilities to process and analyze images through the API.

## Key Topics Covered

### 1. Image Input Methods

The tutorial shows how to pass images to Claude in multiple formats:

- **Base64-encoded images**: Images can be encoded in base64 format and sent directly
- **Multiple image formats supported**: JPEG, PNG, GIF, and WebP
- **URL-based images**: Reference images by URL (where applicable)

### 2. Basic Setup

The notebook begins with installation and imports:

```python
%pip install anthropic IPython
```

This installs the Anthropic SDK needed to interact with Claude's API.

### 3. Vision API Fundamentals

The tutorial demonstrates:

- Creating image content blocks with proper MIME types
- Including images alongside text in prompts
- Handling image data in API requests
- Processing Claude's responses to image analysis

### 4. Supported Image Formats

The API supports:
- **JPEG** (`image/jpeg`)
- **PNG** (`image/png`)
- **GIF** (`image/gif`)
- **WebP** (`image/webp`)

### 5. Use Cases

Common applications covered include:
- Image analysis and description
- Object detection and identification
- Text extraction from images (OCR)
- Visual question answering
- Document analysis
- Chart and diagram interpretation

## Purpose

This cookbook serves as a practical introduction for developers wanting to integrate vision capabilities into their applications using Claude. It provides hands-on examples showing the exact API usage patterns needed to:

1. Prepare images for analysis
2. Send them to Claude along with prompts
3. Interpret and use the responses

The notebook is part of Anthropic's official cookbook resources, which provide practical, copy-paste-ready examples for implementing Claude's various features.
