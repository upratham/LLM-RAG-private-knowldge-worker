# RAG System Architecture

## Overview

This document describes the architecture of the RAG (Retrieval-Augmented Generation) private knowledge worker system.

## System Components

### 1. Document Loader (`src/rag/core/document_loader.py`)

**Purpose**: Load and parse documents from various file formats.

**Key Classes**:
- `Document`: Represents a document with content and metadata
- `BaseDocumentLoader`: Abstract base class for document loaders
- `TextDocumentLoader`: Concrete implementation for text files
- `DocumentLoader`: Main interface supporting multiple file types

**Extensibility**: Add new loaders by extending `BaseDocumentLoader`

### 2. Embedding Generator (`src/rag/core/embeddings.py`)

**Purpose**: Generate vector embeddings for text content.

**Key Classes**:
- `BaseEmbedding`: Abstract interface for embedding generators
- `EmbeddingGenerator`: Pluggable implementation (currently placeholder)

**Integration Points**: 
- OpenAI Embeddings API
- HuggingFace Sentence Transformers
- Custom embedding models

### 3. Vector Store (`src/rag/core/vector_store.py`)

**Purpose**: Store and retrieve document embeddings efficiently.

**Features**:
- In-memory storage with cosine similarity search
- Save/load functionality for persistence
- Extensible to production vector databases

**Production Alternatives**:
- FAISS (Facebook AI Similarity Search)
- Pinecone (managed vector database)
- Chroma (open-source vector database)
- Weaviate, Milvus, Qdrant

### 4. Retriever (`src/rag/core/retriever.py`)

**Purpose**: Find relevant documents for a given query.

**Process**:
1. Generate query embedding
2. Search vector store for similar documents
3. Return top-k matches with scores

### 5. LLM Interface (`src/rag/core/llm.py`)

**Purpose**: Interface with Large Language Models for text generation.

**Key Methods**:
- `generate()`: Basic text generation
- `generate_with_context()`: RAG-aware generation with context

**Integration Points**:
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- HuggingFace (open-source models)
- Local LLMs (LLaMA, Mistral, etc.)

### 6. RAG Pipeline (`src/rag/core/rag_pipeline.py`)

**Purpose**: Orchestrate the complete RAG workflow.

**Workflow**:
1. **Indexing Phase**:
   - Load documents
   - Generate embeddings
   - Store in vector database
   
2. **Query Phase**:
   - Receive user query
   - Retrieve relevant documents
   - Generate context-aware response

## Utility Modules

### Configuration (`src/rag/utils/config.py`)

- JSON-based configuration
- Environment variable support
- Hierarchical settings with dot notation

### Logging (`src/rag/utils/logger.py`)

- Centralized logging setup
- Console and file output
- Configurable log levels

### Text Processing (`src/rag/utils/text_processing.py`)

- Text chunking with overlap
- Text cleaning and normalization
- Sentence extraction

## Data Flow

```
User Document → DocumentLoader → Text Chunks
                                       ↓
                            EmbeddingGenerator
                                       ↓
                                 VectorStore
                                       
User Query → EmbeddingGenerator → Retriever → VectorStore
                                       ↓
                              Relevant Documents
                                       ↓
                                 LLMInterface
                                       ↓
                              Generated Answer
```

## Configuration Management

### Configuration Files
- `config/default_config.json`: Default settings
- Custom config files can override defaults

### Environment Variables
- `EMBEDDING_MODEL`: Embedding model name
- `LLM_MODEL`: LLM model name
- `LLM_MAX_TOKENS`: Maximum tokens for generation
- `LLM_TEMPERATURE`: Sampling temperature
- `RETRIEVAL_K`: Number of documents to retrieve

## Extension Points

### Adding New Document Types

```python
class PDFDocumentLoader(BaseDocumentLoader):
    def load(self, file_path: str) -> List[Document]:
        # Implement PDF loading
        pass

# Register in DocumentLoader
loader.loaders['.pdf'] = PDFDocumentLoader()
```

### Integrating Production Embeddings

```python
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator(BaseEmbedding):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def embed_text(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()
```

### Using Production Vector Stores

```python
import faiss

class FAISSVectorStore:
    def __init__(self, dimension: int = 768):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []
        self.metadata = []
```

### Integrating Real LLMs

```python
from openai import OpenAI

class LLMInterface(BaseLLM):
    def __init__(self, model_name: str = "gpt-4"):
        self.client = OpenAI()
        self.model_name = model_name
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
```

## Testing Strategy

### Unit Tests
- Document loading and parsing
- Text processing utilities
- Configuration management

### Integration Tests (Future)
- End-to-end RAG pipeline
- Vector store operations
- Query and retrieval accuracy

### Test Coverage
- Current: 13 tests covering core functionality
- Goal: >80% code coverage

## Deployment Considerations

### Environment Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment: Copy `.env.example` to `.env`
3. Add documents to `data/documents/`
4. Index documents: `python main.py index data/documents`

### Production Recommendations
1. Use production embedding models (not placeholders)
2. Integrate scalable vector database (FAISS, Pinecone)
3. Configure real LLM provider (OpenAI, Anthropic)
4. Add authentication and rate limiting
5. Implement monitoring and logging
6. Add comprehensive error handling

### Scalability
- Vector store: Use distributed vector databases
- Document processing: Parallel/batch processing
- Caching: Cache embeddings and frequent queries
- Load balancing: Multiple RAG instances

## Security Considerations

1. **API Keys**: Store in environment variables, never in code
2. **Input Validation**: Sanitize user inputs
3. **Access Control**: Implement authentication/authorization
4. **Data Privacy**: Handle sensitive documents appropriately
5. **Rate Limiting**: Prevent abuse of API endpoints

## Performance Optimization

1. **Embedding Caching**: Cache document embeddings
2. **Batch Processing**: Process multiple documents together
3. **Approximate Search**: Use FAISS for faster similarity search
4. **Query Optimization**: Optimize retrieval parameters (k value)
5. **Model Selection**: Balance quality vs. speed

## Future Enhancements

- [ ] Web API (FastAPI/Flask)
- [ ] Conversation history and context
- [ ] Multi-document types (PDF, DOCX, HTML)
- [ ] Advanced chunking strategies
- [ ] Query refinement and expansion
- [ ] Hybrid search (vector + keyword)
- [ ] Result reranking
- [ ] Streaming responses
- [ ] Multimodal support (images, tables)
- [ ] Analytics and monitoring dashboard
