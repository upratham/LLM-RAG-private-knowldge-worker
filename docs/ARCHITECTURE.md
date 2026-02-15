# System Architecture

## Overview

RAG LLM Private Knowledge Worker is built on a modular pipeline architecture that processes documents through multiple stages to enable semantic search and intelligent question answering.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Document Input                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Data Ingestion        │
            │  - Load documents      │
            │  - Handle formats      │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Text Chunking         │
            │  - Split documents     │
            │  - Maintain context    │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Embedding Generation  │
            │  - Create vectors      │
            │  - Semantic encoding   │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Vector Store          │
            │  - Store embeddings    │
            │  - Index for search    │
            └────────────┬───────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
┌───────────────┐              ┌──────────────────┐
│  User Query   │              │  Index (Vectors) │
│  Processing   │              │  (Persisted)     │
└───────┬───────┘              └──────────────────┘
        │
        ▼
┌────────────────────────┐
│  Query Embedding       │
│  - Encode query        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  Semantic Retrieval    │
│  - Search vectors      │
│  - Find similar docs   │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  Context Building      │
│  - Assemble results    │
│  - Prepare prompt      │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  LLM Generation        │
│  - Generate response   │
│  - Ground with context │
└────────────┬───────────┘
             │
             ▼
        │ Final Response │
```

## Core Components

### 1. Data Ingestion Module (`src/data_ingestion/`)

**Purpose**: Load documents from various sources and formats

**Components**:
- `DocumentLoader`: Abstract loader supporting multiple formats
- `TextLoader`: Plain text file support
- `DataIngestionPipeline`: Orchestrates loading process

**Workflow**:
1. Accept file or directory path
2. Identify file format
3. Load content using appropriate loader
4. Return standardized document format

**Output**: `List[dict]` with keys: `file_path`, `file_name`, `content`, `format`

### 2. Chunking Module (`src/chunking/`)

**Purpose**: Split documents into optimal-sized chunks for embedding

**Components**:
- `BaseSplitter`: Abstract base class
- `TextSplitter`: Fixed-size chunking
- `RecursiveCharacterSplitter`: Intelligent boundary-based splitting

**Parameters**:
- `chunk_size`: Target chunk size in characters (default: 1000)
- `overlap`: Overlap between chunks (default: 100)

**Workflow**:
1. Take document content
2. Split on meaningful boundaries (paragraphs, sentences, spaces)
3. Maintain overlap for context preservation
4. Return list of chunks

**Output**: `List[str]` of text chunks

### 3. Embeddings Module (`src/embeddings/`)

**Purpose**: Convert text into dense vector representations

**Components**:
- `BaseEmbedder`: Abstract embedder interface
- `HuggingFaceEmbedder`: Uses sentence-transformers models
- `DummyEmbedder`: Random vectors for testing
- `EmbeddingGenerator`: Wrapper for embedder selection

**Models Available**:
- `all-MiniLM-L6-v2` (default, 384-dim, fast)
- `all-mpnet-base-v2` (768-dim, accurate)
- Custom models from HuggingFace Model Hub

**Workflow**:
1. Initialize embedder with model
2. Tokenize text
3. Pass through neural network
4. Return normalized vector

**Output**: `np.ndarray` of shape `(dimension,)`

### 4. Vector Store Module (`src/vector_store/`)

**Purpose**: Store and index vector embeddings for efficient retrieval

**Components**:
- `BaseVectorStore`: Abstract interface
- `InMemoryVectorStore`: Python dict-based storage
- Support for external DBs (Faiss, Pinecone, Weaviate)

**Capabilities**:
- Add vectors with metadata
- Cosine similarity search
- Persist/load from disk

**Workflow**:
1. Accept texts, embeddings, metadata
2. Store internally (or external DB)
3. Normalize vectors for search
4. Return k nearest neighbors for query

**Output**: `List[Tuple[str, float]]` of (text, similarity_score)

### 5. Retrieval Module (`src/retrieval/`)

**Purpose**: Retrieve relevant documents for user queries

**Components**:
- `BaseRetriever`: Abstract retriever
- `VectorRetriever`: Semantic similarity-based retrieval
- `Retriever`: Main interface

**Workflow**:
1. Encode user query to embedding
2. Search vector store
3. Rank by similarity score
4. Return top-k results

**Output**: `List[Tuple[str, float]]` of relevant documents

### 6. LLM Module (`src/llm/`)

**Purpose**: Generate responses using language models

**Components**:
- `BaseLLM`: Abstract LLM interface
- `OpenAILLM`: GPT-3.5, GPT-4 support
- `DummyLLM`: Mock responses for testing
- `LLMProvider`: Provider wrapper

**Supported Models**:
- OpenAI: GPT-3.5-turbo, GPT-4
- Extensible: Add custom providers

**Workflow**:
1. Prepare prompt with context
2. Call LLM API
3. Parse and return response

**Output**: `str` (generated text)

### 7. RAG System (`src/rag_system.py`)

**Purpose**: Orchestrate entire pipeline

**Workflow**:
```
ingest_documents() → load & store
     ↓
build_index() → chunk → embed → index
     ↓
query() → embed query → retrieve → generate response
```

**Methods**:
- `ingest_documents(path)`: Load documents
- `build_index()`: Create embeddings and index
- `query(query, top_k)`: Process query end-to-end
- `save_index()`, `load_index()`: Persistence

## Data Flow

### Indexing Phase

```
Documents → Ingestion → Chunks → Embeddings → Vector Store
```

1. **Ingestion**: Load documents from disk
2. **Chunking**: Split into overlapping chunks
3. **Embedding**: Convert to vectors
4. **Storage**: Index in vector store

### Query Phase

```
Query → Embedding → Retrieval → Context → LLM → Response
```

1. **Query Embedding**: Convert query to vector
2. **Retrieval**: Find similar chunks
3. **Context Assembly**: Build prompt with chunks
4. **LLM Generation**: Generate contextual response

## Configuration Files

### config.json
Main system configuration

### .env
Environment variables (API keys, paths)

## Extension Points

### Custom Components

1. **Custom Embedder**:
   ```python
   class MyEmbedder(BaseEmbedder):
       def embed(self, text: str) -> np.ndarray:
           # Implementation
   ```

2. **Custom Vector Store**:
   ```python
   class MyVectorStore(BaseVectorStore):
       def add_vectors(self, texts, embeddings, metadata):
           # Implementation
   ```

3. **Custom LLM**:
   ```python
   class MyLLM(BaseLLM):
       def generate(self, prompt: str, **kwargs) -> str:
           # Implementation
   ```

## Performance Characteristics

| Component | Complexity | Speed | Memory |
|-----------|-----------|-------|--------|
| Ingestion | O(n) | Fast | Low |
| Chunking | O(n) | Fast | Low |
| Embedding | O(n*m) | Medium | High |
| Retrieval | O(n) | Medium | Low |
| LLM | O(m) | Slow | Medium |

Where n = number of chunks, m = vector dimension

## Scalability Considerations

### In-Memory Vector Store
- Good for: <1 million vectors
- Memory: ~1.5GB per 1M vectors (384-dim)
- Search: O(n) - linear scan

### Faiss
- Good for: 1M - 1B vectors
- Search: O(log n) - approximate
- Setup: Local or distributed

### Pinecone
- Good for: 1B+ vectors
- Search: O(1) - cloud-managed
- Advantages: Serverless, no ops

## Error Handling

System implements graceful degradation:
1. Missing files → Skip with warning
2. Unsupported formats → Log and continue
3. API failures → Retry with exponential backoff
4. Memory issues → Process in batches

---

For more details, see component-specific documentation in `docs/`
