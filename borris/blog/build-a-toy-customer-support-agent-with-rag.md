---
title: "Build a toy customer support agent with RAG"
source_url: "https://github.com/anthropics/anthropic-quickstarts/tree/main/customer-support-agent"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Build a toy customer support agent with RAG

## Overview

The Claude Customer Support Agent is an advanced, fully customizable customer support chat interface powered by Claude and leveraging Amazon Bedrock Knowledge Bases for knowledge retrieval (RAG).

## Key Features

- **AI-powered chat** using Anthropic's Claude model
- **Amazon Bedrock integration** for contextual knowledge retrieval (RAG)
- **Real-time thinking and debug information** display
- **Knowledge base source visualization**
- **User mood detection** and appropriate agent redirection
- **Highly customizable UI** with shadcn/ui components

## Getting Started

### Quick Setup (5 steps)

1. Clone the repository
2. Install dependencies: `npm install`
3. Set up environment variables
4. Run development server: `npm run dev`
5. Open http://localhost:3000 in your browser

## Configuration

### Required Environment Variables

Create a `.env.local` file with:

- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `BAWS_ACCESS_KEY_ID` - Your AWS access key
- `BAWS_SECRET_ACCESS_KEY` - Your AWS secret key

Note: The 'B' prefix on AWS variables is intentional (AWS doesn't allow environment variable names starting with "AWS" in Amplify).

## Amazon Bedrock RAG Integration

### Configuring Knowledge Bases

Update `ChatArea.tsx` with your knowledge base IDs to connect your own data sources.

### Creating Your Own Knowledge Base

1. Go to AWS Console, then Amazon Bedrock
2. Select "Knowledge base", then "Create knowledge base"
3. Choose data source (e.g., Amazon S3)
4. Select embedding model (e.g., Titan Text Embeddings 2)
5. Select "Quick create a new vector store"
6. Confirm and retrieve the knowledge base ID

## Switching Models

Configure available models in `ChatArea.tsx` to use different Claude models.

## Customization

- **UI Components:** Modify files in `components/ui/`
- **Theme:** Edit `app/globals.css`
- **Layout:** Customize individual component files
- **Theme Colors:** Edit `styles/themes.js`

## Deployment with AWS Amplify

### Step-by-Step Deployment

1. Go to AWS Console, then Amplify, then "Create new app"
2. Select GitHub as source
3. Choose this repository
4. Edit YAML configuration for build settings
5. Add environment variables in "Advanced settings"
6. Click "Save and deploy"

### Service Role Setup (Post-Deployment)

Attach the AmazonBedrockFullAccess policy to the Amplify service role.

## NPM Scripts

- `npm run dev` - Full app with both sidebars
- `npm run dev:chat` - Chat area only (no sidebars)
- `npm run build` - Build with both sidebars
- `npm run build:chat` - Build chat area only

## Important Note

This project is provided as-is as a prototype and is not intended for production use. No warranties or guarantees are provided.
