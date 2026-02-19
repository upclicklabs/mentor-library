---
title: "Read Anthropic's evaluations documentation"
source_url: "https://docs.anthropic.com/en/docs/build-with-claude/develop-tests"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Read Anthropic's evaluations documentation

After defining your success criteria, the next step is designing evaluations to measure LLM performance against those criteria. This is a vital part of the prompt engineering cycle.

## Building evals and test cases

### Eval design principles

1. **Be task-specific**: Design evals that mirror your real-world task distribution. Include edge cases such as:
   - Irrelevant or nonexistent input data
   - Overly long input data or user input
   - Poor, harmful, or irrelevant user input (for chat use cases)
   - Ambiguous test cases where even humans would find it hard to reach consensus

2. **Automate when possible**: Structure questions to allow for automated grading (e.g., multiple-choice, string match, code-graded, LLM-graded).

3. **Prioritize volume over quality**: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.

### Example eval approaches

**Exact match evaluation (Sentiment analysis)**: Measures whether the model's output exactly matches a predefined correct answer. Simple, unambiguous metric perfect for clear-cut categorical answers.

**Cosine similarity evaluation (FAQ bot)**: Measures similarity between sentence embeddings of the model's output. Ideal for evaluating consistency -- similar questions should yield semantically similar answers.

**ROUGE-L evaluation (Summarization)**: Measures the length of the longest common subsequence between candidate and reference summaries. High scores indicate the generated summary captures key information in a coherent order.

**LLM-based Likert scale (Customer service tone)**: Uses an LLM to rate subjective aspects like empathy, professionalism, or patience on a 1-5 scale. Ideal for nuanced aspects difficult to quantify with traditional metrics.

**LLM-based binary classification (Privacy preservation)**: Classifies whether a response contains PHI or not. Can understand context and identify subtle or implicit forms of sensitive information.

**LLM-based ordinal scale (Context utilization)**: Measures on a fixed ordered scale (1-5) the degree to which the model references and builds upon conversation history.

## Grading evals

Choose the fastest, most reliable, most scalable method:

1. **Code-based grading**: Fastest and most reliable, extremely scalable, but lacks nuance for complex judgements.
   - Exact match: `output == golden_answer`
   - String match: `key_phrase in output`

2. **Human grading**: Most flexible and high quality, but slow and expensive. Avoid if possible.

3. **LLM-based grading**: Fast and flexible, scalable and suitable for complex judgement. Test to ensure reliability first then scale.

### Tips for LLM-based grading

- **Have detailed, clear rubrics**: e.g., "The answer should always mention 'Acme Inc.' in the first sentence."
- **Empirical or specific**: Instruct the LLM to output only 'correct' or 'incorrect', or judge from a scale of 1-5.
- **Encourage reasoning**: Ask the LLM to think first before deciding an evaluation score, then discard the reasoning. This increases evaluation performance for tasks requiring complex judgement.

Example grading pattern:

```python
def build_grader_prompt(answer, rubric):
    return f"""Grade this answer based on the rubric:
    <rubric>{rubric}</rubric>
    <answer>{answer}</answer>
    Think through your reasoning in <thinking> tags, then output 'correct' or 'incorrect' in <result> tags."""
```

Tips: Get Claude to help generate more test cases from a baseline set. You can also brainstorm eval methods with Claude.
