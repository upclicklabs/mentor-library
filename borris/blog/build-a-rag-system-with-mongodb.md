---
title: "Build a RAG system with MongoDB"
source_url: "https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/MongoDB/rag_using_mongodb.ipynb"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Build a RAG system with MongoDB

## Overview

This tutorial implements a chatbot that takes on the role of a Venture Capital tech Analyst. The chatbot is a naive RAG (Retrieval-Augmented Generation) system with a collection of tech news articles acting as its knowledge source.

### What You Will Learn

1. Set up your development environment (installing libraries, configuring MongoDB database)
2. Efficient data handling methods (creating vector search indexes, preparing data for ingestion and query processing)
3. Employ Claude 3 models within the RAG system for generating precise responses based on contextual information retrieved from the database

### Prerequisites

- Claude API Key
- VoyageAI API Key
- Hugging Face Access Token

## Step 1: Library Installation, Data Loading and Preparation

### Required Libraries

- **anthropic**: Official Python library for Anthropic providing access to Claude 3 family models
- **datasets**: Hugging Face ecosystem library for accessing pre-processed datasets
- **pandas**: Data science library for data manipulation and analysis
- **voyageai**: Official Python client library for VoyageAI's embedding models
- **pymongo**: Python toolkit for MongoDB database interactions

```bash
pip install pymongo datasets pandas anthropic voyageai
```

### Data Download and Preparation

```python
from io import BytesIO
import pandas as pd
import requests

def download_and_combine_parquet_files(parquet_file_urls, hf_token):
    headers = {"Authorization": f"Bearer {hf_token}"}
    all_dataframes = []
    for parquet_file_url in parquet_file_urls:
        response = requests.get(parquet_file_url, headers=headers, timeout=60)
        if response.status_code == 200:
            parquet_bytes = BytesIO(response.content)
            df = pd.read_parquet(parquet_bytes)
            all_dataframes.append(df)
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        return combined_df
    return None
```

### Embedding Generation with VoyageAI

```python
import voyageai

vo = voyageai.Client(api_key=userdata.get("VOYAGE_API_KEY"))

def get_embedding(text):
    if not text.strip():
        return []
    embedding = vo.embed(text, model="voyage-large-2", input_type="document")
    return embedding.embeddings[0]

combined_df["embedding"] = combined_df["description"].apply(get_embedding)
```

## Step 2: Database and Collection Creation

1. Register for a free MongoDB Atlas account
2. Create a new cluster
3. Obtain your MongoDB connection URI
4. Whitelist your IP address
5. Create a database named `tech_news` and collection named `hacker_noon_tech_news`

## Step 3: Vector Search Index Creation

Create a vector search index named `vector_index`:

```json
{
  "fields": [{
    "numDimensions": 1536,
    "path": "embedding",
    "similarity": "cosine",
    "type": "vector"
  }]
}
```

## Step 4: Data Ingestion

```python
import pymongo

def get_mongo_client(mongo_uri):
    try:
        client = pymongo.MongoClient(mongo_uri)
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None

mongo_client = get_mongo_client(mongo_uri)
db = mongo_client["tech_news"]
collection = db["hacker_noon_tech_news"]

collection.delete_many({})
combined_df_json = combined_df.to_dict(orient="records")
collection.insert_many(combined_df_json)
```

## Step 5: Vector Search

```python
def vector_search(user_query, collection):
    query_embedding = get_embedding(user_query)
    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "numCandidates": 150,
                "limit": 5,
            }
        },
        {
            "$project": {
                "_id": 0,
                "embedding": 0,
                "score": {"$meta": "vectorSearchScore"},
            }
        },
    ]
    results = collection.aggregate(pipeline)
    return list(results)
```

## Step 6: Handling User Queries with Claude 3 Models

```python
import anthropic

client = anthropic.Client(api_key=userdata.get("ANTHROPIC_API_KEY"))

def handle_user_query(query, collection):
    get_knowledge = vector_search(query, collection)

    search_result = ""
    for result in get_knowledge:
        search_result += (
            f"Title: {result.get('title', 'N/A')}, "
            f"Company Name: {result.get('companyName', 'N/A')}, "
            f"Description: {result.get('description', 'N/A')},\n"
        )

    response = client.messages.create(
        model="claude-opus-4-1",
        max_tokens=1024,
        system="You are a Venture Capital Tech Analyst with access to some tech company articles and information.",
        messages=[
            {
                "role": "user",
                "content": "Answer this user query: " + query + " with the following context: " + search_result,
            }
        ],
    )
    return response.content[0].text, search_result
```

### Example Usage

```python
query = "Give me the best tech stock to invest in and tell me why"
response, source_information = handle_user_query(query, collection)
print(f"Response: {response}")
print(f"\nSource Information:\n{source_information}")
```

## Key Features

- Semantic search using vector embeddings (VoyageAI)
- MongoDB vector search for efficient retrieval
- Claude 3 integration for intelligent responses
- Context-aware RAG system
- Source attribution and transparency
