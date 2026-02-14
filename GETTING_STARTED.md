# Getting Started with RAG Private Knowledge Worker

This guide will help you get started with the RAG (Retrieval-Augmented Generation) Private Knowledge Worker system.

## Quick Start (5 minutes)

### 1. Clone and Install

```bash
# Clone the repository
git clone https://github.com/upratham/LL-RAG-private-knowldge-worker.git
cd LL-RAG-private-knowldge-worker

# Install dependencies
pip install -r requirements.txt
```

### 2. Try the Example

```bash
# Run the basic example (uses sample document)
python examples/basic_usage.py
```

This will:
- Initialize the RAG pipeline
- Index the sample document
- Run an example query
- Display results with sources

### 3. Add Your Own Documents

```bash
# Add your documents to the data directory
cp your-document.txt data/documents/
cp your-notes.md data/documents/

# Index your documents using the CLI
python main.py index data/documents
```

### 4. Query Your Knowledge Base

```bash
# Ask questions about your documents
python main.py query "What is the main topic of these documents?"

# Get more results
python main.py query "Tell me about X" -k 10
```

## Common Use Cases

### Use Case 1: Personal Knowledge Management

```python
from src.rag import RAGPipeline

# Create your personal knowledge base
rag = RAGPipeline(
    vector_store_path="data/vector_store/personal.json"
)

# Index your notes, documents, articles
rag.index_documents("path/to/your/notes", is_directory=True)

# Query your knowledge
response = rag.query("What did I learn about Python decorators?")
print(response['answer'])
```

### Use Case 2: Technical Documentation Assistant

```python
from src.rag import RAGPipeline

# Load technical documentation
rag = RAGPipeline(
    vector_store_path="data/vector_store/docs.json"
)

# Index your API docs, README files, guides
rag.index_documents("path/to/docs", is_directory=True)

# Get instant answers
response = rag.query("How do I configure authentication?")
```

### Use Case 3: Research Paper Q&A

```python
from src.rag import RAGPipeline

# Create research assistant
rag = RAGPipeline(
    vector_store_path="data/vector_store/papers.json"
)

# Index research papers (add PDF support first!)
rag.index_documents("path/to/papers", is_directory=True)

# Ask research questions
response = rag.query(
    "What are the main findings about neural networks?",
    k=10  # Get more context
)
```

## Configuration

### Using Configuration Files

Create a custom config file:

```json
{
  "embedding": {
    "model": "my-custom-model",
    "dimension": 768
  },
  "llm": {
    "model": "gpt-4",
    "max_tokens": 1000,
    "temperature": 0.8
  },
  "retrieval": {
    "k": 10
  }
}
```

Use it:

```python
from src.rag.utils.config import Config
from src.rag import RAGPipeline

config = Config("my_config.json")
rag = RAGPipeline(
    embedding_model=config.get('embedding.model'),
    llm_model=config.get('llm.model'),
    vector_store_path=config.get('paths.vector_store')
)
```

### Using Environment Variables

Create a `.env` file:

```bash
# Copy the template
cp .env.example .env

# Edit .env with your settings
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=gpt-4
OPENAI_API_KEY=your-api-key-here
```

The system will automatically load these settings.

## Next Steps

### 1. Integrate Production Components

The current implementation uses placeholders. Here's how to upgrade:

#### Add Real Embeddings (HuggingFace)

```bash
pip install sentence-transformers
```

Update `src/rag/core/embeddings.py`:

```python
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator(BaseEmbedding):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def embed_text(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()
```

#### Add OpenAI LLM

```bash
pip install openai
```

Update `src/rag/core/llm.py`:

```python
from openai import OpenAI

class LLMInterface(BaseLLM):
    def __init__(self, model_name: str = "gpt-4"):
        self.client = OpenAI()  # Uses OPENAI_API_KEY from env
        self.model_name = model_name
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
```

#### Add FAISS Vector Store

```bash
pip install faiss-cpu
```

Create new vector store implementation following the pattern in `src/rag/core/vector_store.py`.

### 2. Add Support for More File Types

#### PDF Support

```bash
pip install pypdf
```

Add to `src/rag/core/document_loader.py`:

```python
import pypdf

class PDFDocumentLoader(BaseDocumentLoader):
    def load(self, file_path: str) -> List[Document]:
        documents = []
        with open(file_path, 'rb') as f:
            reader = pypdf.PdfReader(f)
            for page_num, page in enumerate(reader.pages):
                content = page.extract_text()
                metadata = {
                    'source': file_path,
                    'file_type': 'pdf',
                    'page': page_num + 1
                }
                documents.append(Document(content, metadata))
        return documents

# Register in DocumentLoader.__init__
self.loaders['.pdf'] = PDFDocumentLoader()
```

### 3. Create a Web API

```bash
pip install fastapi uvicorn
```

Create `api.py`:

```python
from fastapi import FastAPI
from src.rag import RAGPipeline

app = FastAPI()
rag = RAGPipeline(vector_store_path="data/vector_store/store.json")

@app.post("/query")
async def query(question: str, k: int = 5):
    response = rag.query(question, k=k)
    return response

@app.post("/index")
async def index(path: str):
    rag.index_documents(path, is_directory=True)
    return {"status": "success"}

# Run with: uvicorn api:app --reload
```

## Troubleshooting

### Issue: "No documents loaded"

**Solution**: Make sure you have documents in the `data/documents/` directory and they have supported extensions (.txt, .md).

### Issue: "ModuleNotFoundError"

**Solution**: Install all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Placeholder responses

**Solution**: The default implementation uses placeholders. Follow "Next Steps" to integrate real embeddings and LLMs.

### Issue: Poor retrieval results

**Solutions**:
- Increase k value (retrieve more documents)
- Use better embeddings (sentence-transformers)
- Chunk documents into smaller pieces
- Clean and preprocess text

## Best Practices

1. **Document Preparation**
   - Clean text before indexing
   - Remove irrelevant content
   - Split large documents into chunks
   - Add meaningful metadata

2. **Configuration**
   - Start with default settings
   - Tune based on your use case
   - Use environment variables for secrets
   - Keep config files in version control (without secrets)

3. **Query Optimization**
   - Be specific in questions
   - Adjust k based on context needs
   - Use appropriate temperature for creativity vs. accuracy
   - Review sources to verify answers

4. **Production Deployment**
   - Use production-grade components (FAISS, OpenAI)
   - Add authentication and rate limiting
   - Monitor costs (API calls)
   - Implement caching
   - Add error handling and logging

## Resources

- [ARCHITECTURE.md](ARCHITECTURE.md) - Detailed system architecture
- [README.md](README.md) - Full documentation
- [examples/](examples/) - Working examples
- [tests/](tests/) - Unit tests

## Getting Help

1. Check the documentation in this repository
2. Review the examples
3. Look at the test cases for usage patterns
4. Open an issue on GitHub

## What's Next?

Now that you have a working RAG system:

1. ✅ Add your own documents
2. ✅ Experiment with queries
3. ✅ Integrate production components
4. ✅ Add more file type support
5. ✅ Build your specific use case
6. ✅ Deploy to production

Happy building! 🚀
