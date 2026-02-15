# Data Directory

This directory contains input and processed data for the RAG system.

## Structure

- **raw/** - Original documents to be ingested
- **processed/** - Processed and chunked documents

## Adding Documents

1. Place your documents in `raw/` subdirectory
2. Supported formats: `.txt`, `.pdf`, `.docx`
3. Run `python main.py` or use `RAGSystem.ingest_documents()`

## Examples

```
raw/
├── kb_document_1.txt
├── kb_document_2.txt
├── company_handbook.pdf
└── research_papers/
    ├── paper1.pdf
    └── paper2.txt
```

## Document Best Practices

1. **Format**: Plain text or standard document formats
2. **Size**: Break large files (>1MB) into smaller sections
3. **Language**: Ensure consistent language (preferably English)
4. **Quality**: Clean text without excessive markup or artifacts
5. **Structure**: Organize logically with clear sections

## Data Privacy

- Ensure all documents are authorized for processing
- Sensitive information should be redacted
- Follow organizational data policies
- No PII (personally identifiable information) in documents
