---
title: "AI Content and Search"
source_url: "https://graphite.io/five-percent/ai-content-and-search"
source_type: blog
mentor: "Ethan"
date_synced: "2026-02-14T00:00:00Z"
---

# AI Content and Search

## Motivation

Companies are exploring AI for organic content creation to reduce costs and scale efficiently. However, concerns exist about quality, as Google emphasizes expertise and personal experience. This research investigates the prevalence of AI-generated content in search results and compares its performance against human-written content.

Key finding: purely AI-generated content makes up 3% of organic search results today, and generally ranks lower than human-generated content.

## Experiment Setup

### 1. Keyword Selection
- 2,200 keywords across 10 categories (Tech, Productivity, News, Food, Finance, Entertainment, Education, Crypto, Commerce, Local)
- 220 random keywords selected per category

### 2. URL Selection and Filtering
- Top 20 organic results per keyword
- Limited to articles and listicles (excluded product/category pages, PDFs)
- Final dataset: 20,280 URLs after filtering and processing

### 3. AI Detection
Used Originality.ai with >90% accuracy. Classification method:
- **AI-generated paragraphs**: score >= 0.85
- **Human-created paragraphs**: score < 0.15
- **Uncertain paragraphs**: between thresholds

Final filtered dataset: 11,994 URLs (removed ~40% with excessive ambiguous content)

### 4. AI Content Taxonomy

- **Human-created**: <10% AI content
- **AI-generated**: >=90% AI content
- **Mixed: low AI**: 10-50% AI content
- **Mixed: high AI**: 50-90% AI content

## Results

### AI Content Prevalence in Search

Pure AI-generated content comprises only 3% of first two search result pages. Pages with >50% AI content account for 12% total; 88% contain minimal-to-no AI content.

Category variations: Food shows <1% purely AI-generated; Commerce leads at 8%. Crypto, Commerce, Finance, and Local categories feature approximately 20% with >50% AI content.

### Rank Performance Analysis

The best position for human-created content is in the first five positions 50% of the time, while the best position for AI-created content is on the second SERP 50% of the time.

Average ranking positions worsen with increased AI content percentage. Human-written content consistently outranks AI-generated alternatives.

## Conclusion

Research indicates AI-generated content represents a small search result fraction and performs worse than human-created content. Despite cost reductions, human-written content performs better in search when evaluating ROI across strategies. The landscape continues evolving rapidly.
