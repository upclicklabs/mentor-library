---
title: "Read Anthropic's vision documentation"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/vision"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Read Anthropic's vision documentation

Claude's vision capabilities allow it to understand and analyze images, opening up possibilities for multimodal interaction.

## How to use vision

Use Claude's vision capabilities via:
- claude.ai - Upload an image or drag and drop directly into the chat window
- The Console Workbench - A button to add images appears at the top right of every User message block
- API request

## Before you upload

### Basics and Limits

- Include multiple images in a single request (up to 20 for claude.ai, 100 for API)
- Images larger than 8000x8000 px will be rejected
- If submitting more than 20 images in one API request, limit is 2000x2000 px
- 32MB request size limit for standard endpoints

### Evaluate image size

For optimal performance, resize images before uploading if they are too large. If the long edge is more than 1568 pixels, or the image is more than ~1,600 tokens, it will be scaled down preserving aspect ratio.

Maximum image sizes that will not be resized (approximately 1,600 tokens):

| Aspect ratio | Image size |
|---|---|
| 1:1 | 1092x1092 px |
| 3:4 | 951x1268 px |
| 2:3 | 896x1344 px |
| 9:16 | 819x1456 px |
| 1:2 | 784x1568 px |

### Calculate image costs

Token estimation: `tokens = (width px * height px) / 750`

Example costs based on Claude Opus 4.6 ($3/MTok input):

| Image size | Tokens | Cost/image | Cost/1K images |
|---|---|---|---|
| 200x200 px | ~54 | ~$0.00016 | ~$0.16 |
| 1000x1000 px | ~1334 | ~$0.004 | ~$4.00 |
| 1092x1092 px | ~1590 | ~$0.0048 | ~$4.80 |

### Ensuring image quality

- **Image format**: Use JPEG, PNG, GIF, or WebP
- **Image clarity**: Ensure images are clear and not too blurry or pixelated
- **Text**: If the image contains important text, make sure it's legible

## Providing images to Claude

Three ways to provide images:

1. **Base64-encoded image** in `image` content blocks
2. **URL reference** to an image hosted online
3. **Files API** (upload once, use multiple times)

Best practice: Place images before text in your prompts. Images placed after text will still perform well, but image-then-text structure is preferred.

### Multiple images

Introduce each image with `Image 1:` and `Image 2:` etc. You don't need newlines between images.

## Limitations

- **People identification**: Claude cannot identify (name) people in images
- **Accuracy**: May hallucinate or make mistakes with low-quality, rotated, or very small images
- **Spatial reasoning**: Limited abilities for precise localization or layouts
- **Counting**: Approximate counts only, especially with large numbers of small objects
- **AI generated images**: Cannot reliably detect fake or synthetic images
- **Inappropriate content**: Will not process images violating the Acceptable Use Policy
- **Healthcare**: Not designed for complex diagnostic scans (CTs/MRIs); not a substitute for professional medical advice

## FAQ highlights

- Supported formats: JPEG, PNG, GIF, WebP
- Claude can process images from URLs with URL image source blocks
- API max: 5MB per image; claude.ai max: 10MB per image
- API max: 100 images per request; claude.ai max: 20 images per turn
- Claude does not parse or receive image metadata
- Claude cannot generate, edit, or create images - understanding only
