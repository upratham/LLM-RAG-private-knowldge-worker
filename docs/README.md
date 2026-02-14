# RAG LLM Documentation

## Overview

This RAG (Retrieval-Augmented Generation) system provides a complete pipeline for building knowledge-based AI assistants.

## Architecture

### Components

1. **Document Ingestion**
   - Loads documents from various formats
   - Splits text into manageable chunks
   - Preserves metadata

2. **Embeddings**
   - Generates vector representations
   - Uses sentence-transformers or custom models
   - Configurable dimensions

3. **Vector Store**
   - Stores embeddings efficiently
   - FAISS or numpy-based search
   - Persistent storage

4. **Retrieval**
   - Semantic similarity search
   - Configurable number of results
   - Score-based filtering

5. **LLM Integration**
   - Multiple provider support
   - Prompt engineering
   - Context-aware generation

6. **Query Processing**
   - Orchestrates the pipeline
   - Formats responses
   - Tracks sources

## Workflow

```
Documents → Ingestion → Chunks → Embeddings → Vector Store
                                                     ↓
User Query → Embedding → Similarity Search → Top K Results
                                                     ↓
                                        LLM with Context → Answer
```

## Configuration Guide

### Embedding Models

Choose based on your needs:
- `all-MiniLM-L6-v2`: Fast, 384 dimensions, good for most use cases
- `all-mpnet-base-v2`: Better quality, 768 dimensions
- `multi-qa-mpnet-base-dot-v1`: Optimized for Q&A

### Chunk Size

- Smaller chunks (500-1000): More precise retrieval
- Larger chunks (1000-2000): More context per chunk
- Overlap: 10-20% of chunk size for continuity

### Retrieval Settings

- K (number of results): 3-10 depending on query complexity
- Score threshold: Filter low-quality matches
- Context formatting: How to present retrieved docs to LLM

## Best Practices

1. **Document Preparation**
   - Clean and format documents
   - Remove unnecessary content
   - Organize by topic

2. **Chunking Strategy**
   - Respect semantic boundaries
   - Maintain context
   - Test different sizes

3. **Embedding Selection**
   - Match domain if possible
   - Consider speed vs quality
   - Use consistent models

4. **Query Optimization**
   - Clear, specific questions
   - Relevant keywords
   - Appropriate detail level

5. **LLM Prompting**
   - Clear instructions
   - Context formatting
   - Source citation

## Troubleshooting

### Common Issues

1. **Poor Retrieval Quality**
   - Increase K value
   - Adjust chunk size
   - Try different embedding model

2. **Slow Performance**
   - Use FAISS for large datasets
   - Reduce embedding dimensions
   - Optimize chunk size

3. **Out of Memory**
   - Process documents in batches
   - Use smaller embedding model
   - Reduce chunk overlap

4. **Irrelevant Responses**
   - Improve query phrasing
   - Adjust system prompt
   - Filter by score threshold

## API Reference

See inline documentation in each module for detailed API references.
