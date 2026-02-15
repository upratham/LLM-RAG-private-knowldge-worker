# Vector Store Directory

This directory stores the persisted vector database indices.

## Content

- **index.json** - Main vector store index (created by `RAGSystem.save_index()`)

## Usage

Save index:
```python
rag.save_index('./vectors/index.json')
```

Load index:
```python
rag.load_index('./vectors/index.json')
```

## Format

The index is stored in JSON format containing:
- **vectors**: List of embedding vectors
- **texts**: List of original text chunks
- **metadata**: Associated metadata for each chunk

## Storage Considerations

- Index size: ~1.5 KB per vector (for 384-dim embeddings)
- 1 million vectors ≈ 1.5 GB
- Compress large indices for archival: `gzip index.json`

## Backup

Regularly backup important indices:
```bash
cp index.json index.json.backup
gzip -c index.json > index.json.gz
```
