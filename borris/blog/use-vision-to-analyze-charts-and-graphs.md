---
title: "Use vision to analyze charts and graphs"
source_url: "https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/reading_charts_graphs_powerpoints.ipynb"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Use vision to analyze charts and graphs

Claude is highly capable of working with charts, graphs, and broader slide decks. Depending on your use case, there are a number of tips and tricks that you may want to take advantage of.

## Charts and Graphs

For the most part, using Claude with charts and graphs is simple. This section walks through how to ingest them and pass them to Claude, as well as some common tips to improve your results.

### Ingestion and Calling the Claude API

The best way to pass Claude charts and graphs is to take advantage of its vision capabilities and the PDF support feature. That is, give Claude a PDF document of the chart or graph, along with a text question about it.

### Setup

```python
%pip install anthropic
```

```python
import base64
from anthropic import Anthropic

client = Anthropic(default_headers={"anthropic-beta": "pdfs-2024-09-25"})
MODEL_NAME = "claude-sonnet-4-6"
```

### Helper Function

```python
def get_completion(messages):
    response = client.messages.create(
        model=MODEL_NAME, max_tokens=8192, temperature=0, messages=messages
    )
    return response.content[0].text
```

### Working with PDFs

Read in a PDF and encode it as base64:

```python
with open("./documents/cvna_2021_annual_report.pdf", "rb") as pdf_file:
    binary_data = pdf_file.read()
    base_64_encoded_data = base64.b64encode(binary_data)
    base64_string = base_64_encoded_data.decode("utf-8")
```

### Passing the Document to Claude

```python
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "document",
                "source": {
                    "type": "base64",
                    "media_type": "application/pdf",
                    "data": base64_string,
                },
            },
            {"type": "text", "text": "What's in this document? Answer in a single sentence."},
        ],
    }
]
print(get_completion(messages))
```

### Tips for Working with Charts and Graphs

- **Arithmetic Errors**: Sometimes Claude's arithmetic capabilities get in the way. Consider providing Claude with a calculator tool to ensure it does not make these types of mistakes.

- **Complex Charts**: With super complicated charts and graphs, ask Claude to "First describe every data point you see in the document" as a way to elicit similar improvements to what we see in traditional Chain of Thought.

- **Color-Dependent Charts**: Claude occasionally struggles with charts that depend on lots of colors to convey information, such as grouped bar charts with many groups. Asking Claude to first identify the colors in your graph using HEX codes can boost its accuracy.

## Slide Decks

Slides represent a critical source of information for many domains, including financial services. While you can use packages like PyPDF to extract text from slide decks, their chart/graph heavy nature often makes this a poor choice as models will struggle to access the information they actually need.

The PDF support feature can be a great replacement as it uses both extracted text and vision when processing PDF documents.

### Basic Approach

The best way to get a typical slide deck into Claude is to download it as a PDF and provide it directly to Claude.

```python
with open("./documents/twilio_q4_2023.pdf", "rb") as pdf_file:
    binary_data = pdf_file.read()
    base_64_encoded_data = base64.b64encode(binary_data)
    base64_string = base_64_encoded_data.decode("utf-8")
```

```python
question = "What was Twilio y/y revenue growth for fiscal year 2023?"
content = [
    {
        "type": "document",
        "source": {"type": "base64", "media_type": "application/pdf", "data": base64_string},
    },
    {"type": "text", "text": question},
]
messages = [{"role": "user", "content": content}]
print(get_completion(messages))
```

### Limitations

- You can only include a total of 100 pages across all provided documents in a request (this limit is intended to increase over time).
- If you are using slide content as part of RAG, introducing multimodal PDFs into your embeddings can cause problems.

### Advanced Approach: Text Narration for RAG

To overcome these limitations, you can take advantage of Claude's vision capabilities to get a much higher quality representation of the slide deck in text form than normal PDF text extraction allows.

The best way to do this is to ask Claude to sequentially narrate the deck from start to finish, passing it the current slide and its prior narration.

```python
prompt = """
You are the Twilio CFO, narrating your Q4 2023 earnings presentation.
Please narrate this presentation as if you were the presenter.
Do not leave any details un-narrated as some of your viewers are vision-impaired.

Structure your response like this:
<narration>
 <page_narration id=1>
 [Your narration for page 1]
 </page_narration>
 ...
</narration>

Use excruciating detail for each page.
"""
```

Once you have a text-based narration, you can use this deck with any text-only workflow, including vector search.

## Conclusion

With these techniques at your side, you are ready to start applying models to chart and graph heavy content like slide decks.
