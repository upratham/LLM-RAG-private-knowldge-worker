# Getting Started Guide

## 1. Installation & Setup

### Step 1: Clone the Repository
```bash
cd LLM-RAG-private-knowledge-worker
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
cp .env.example .env
# Edit .env file with your API keys
```

## 2. Prepare Your Data

Place your documents in `data/raw/` directory. Supported formats:
- `.txt` - Plain text files
- `.pdf` - PDF documents (requires PyPDF2)
- `.docx` - Word documents (requires python-docx)

Example:
```
data/raw/
  ├── document1.txt
  ├── document2.txt
  └── research/
      └── paper.pdf
```

## 3. Configure the System

Edit `config/config.json`:

```json
{
  "embedding": {
    "model": "sentence-transformers/all-MiniLM-L6-v2",
    "dimension": 384,
    "batch_size": 32
  },
  "chunking": {
    "chunk_size": 1000,
    "overlap": 100,
    "strategy": "recursive"
  },
  "retrieval": {
    "top_k": 5,
    "similarity_threshold": 0.3
  },
  "llm": {
    "provider": "openai",
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 500
  }
}
```

## 4. Run Your First Example

```bash
# Basic usage
python examples/basic_usage.py

# Custom pipeline
python examples/custom_pipeline.py

# Advanced features
python examples/advanced_features.py
```

## 5. Use in Your Code

```python
from src.rag_system import RAGSystem

# Initialize
rag = RAGSystem(config_path='./config/config.json')

# Ingest documents
rag.ingest_documents('./data/raw')
print("Documents ingested")

# Build index
chunks = rag.build_index()
print(f"Index built with {chunks} chunks")

# Query
results = rag.query("What is machine learning?", top_k=3)
print(f"Response: {results['response']}")
```

## 6. API Keys Setup

### OpenAI
1. Get API key from https://platform.openai.com/api-keys
2. Add to `.env`:
   ```env
   OPENAI_API_KEY=sk-...
   ```

### Other LLM Providers
- **Anthropic Claude**: Get key from https://console.anthropic.com
- **Hugging Face**: Get token from https://huggingface.co/settings/tokens
- **Cohere**: Get API key from https://dashboard.cohere.com

## 7. Performance Tuning

### For Better Retrieval Quality
```python
rag = RAGSystem()
# Increase chunk size for better context
config['chunking']['chunk_size'] = 2000
# Increase overlap
config['chunking']['overlap'] = 200
```

### For Faster Processing
```python
# Reduce chunk size
config['chunking']['chunk_size'] = 500
# Use smaller embedding model
config['embedding']['model'] = 'paraphrase-MiniLM-L6-v2'
```

### For Lower Memory Usage
```python
# Reduce batch size
config['embedding']['batch_size'] = 8
# Use smaller model dimension
config['embedding']['dimension'] = 256
```

## 8. Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src

# Run specific test
pytest tests/test_rag.py::TestEmbeddings
```

## 9. Debugging

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

from src.rag_system import RAGSystem
rag = RAGSystem()
rag.ingest_documents('./data/raw')
```

Check logs in `logs/rag_system.log`

## 10. Next Steps

- Read [API Reference](API_REFERENCE.md)
- Explore [examples/](examples/) directory
- Check [Integration Guide](INTEGRATION_GUIDE.md) for vector DBs
- Review [Architecture](ARCHITECTURE.md) for system design

---

**Need Help?**
- Check [examples/](examples/) for working code
- Read component documentation in `docs/`
- Review error logs in `logs/`
