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

### 1. Data Ingestion Module (`src/data_ingestion.py`)

**Purpose**: Load documents from various sources and create LangChain Document objects

**Functions**:
- `fetch_documents(filenames)`: Load documents with metadata
- `chunking(documents, chunk_size, chunk_overlap)`: Split documents into chunks using LangChain

**Workflow**:
1. Accept list of file paths
2. Read file content and extract folder type from path
3. Create LangChain Document objects with metadata (type, source)
4. Split documents using RecursiveCharacterTextSplitter

**Output**: List of LangChain `Document` objects with page_content and metadata

**Key Features**:
- Automatic document type detection from folder structure
- Integration with LangChain's document handling
- Metadata preservation through the pipeline

### 2. Text Splitting (LangChain Integration)

**Purpose**: Split documents into optimal-sized chunks using LangChain's text splitters

**Implementation**: Uses `RecursiveCharacterTextSplitter` from `langchain-text-splitters`

**Parameters**:
- `chunk_size`: Target chunk size in characters (configurable)
- `chunk_overlap`: Overlap between chunks to maintain context (configurable)

**Workflow**:
1. Convert documents to LangChain Document format
2. Apply RecursiveCharacterTextSplitter
3. Split on meaningful boundaries (paragraphs, sentences, spaces)
4. Preserve metadata through splitting process

**Output**: List of LangChain `Document` objects with chunks

### 3. Embeddings Module (`src/embedder.py`)

**Purpose**: Convert text into dense vector representations using HuggingFace models via LangChain

**Implementation**: Uses `HuggingFaceEmbeddings` from `langchain-huggingface`

**Function**: `embedder(db_path, chunks)`

**Model Used**: `intfloat/e5-large-v2`
- High-quality embeddings (1024-dimensional)
- Optimized for semantic search
- Normalized embeddings for cosine similarity

**Workflow**:
1. Initialize HuggingFaceEmbeddings with e5-large-v2 model
2. Create/reset Chroma vector store at specified path
3. Generate embeddings for all document chunks
4. Store embeddings with metadata in Chroma
5. Return vectorstore instance

**Key Features**:
- Automatic normalization for cosine similarity
- Direct integration with Chroma vector database
- Persistent storage of embeddings

**Output**: Chroma vectorstore instance with embedded documents

### 4. Vector Store Module (Chroma DB)

**Purpose**: Store and index vector embeddings using Chroma vector database

**Implementation**: Uses `Chroma` from `langchain-chroma`

**Storage Location**: `vectors/` directory
- `chroma.sqlite3`: SQLite database for metadata
- Collection directories: Vector data and indices

**Capabilities**:
- Persistent storage of embeddings and metadata
- Fast similarity search using Chroma's indexing
- Collection management (create, delete, update)
- Metadata filtering and hybrid search

**Workflow**:
1. Initialize Chroma with persist_directory
2. Store document chunks with embeddings and metadata
3. Build internal indices for fast retrieval
4. Perform similarity search on queries
5. Return top-k most similar documents

**Key Advantages**:
- Production-ready vector database
- Persistent storage (survives restarts)
- Efficient indexing for large-scale retrieval
- Built-in metadata support

**Output**: Chroma search results with documents, scores, and metadata

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

### 7. Visualization Module (`src/visualize_vector_db.py`)

**Purpose**: Visualize vector embeddings in 2D and 3D space

**Implementation**: Uses t-SNE for dimensionality reduction and Plotly for interactive visualization

**Functions**:
- `prepare_visualization_data(vector_store)`: Extract vectors and metadata from Chroma
- `visualize_2d(vector_store)`: Create 2D t-SNE visualization
- `visualize_3d(vector_store)`: Create 3D t-SNE visualization
- `get_default_colors()`: Color mapping for document types
- `map_colors(doc_types, colors)`: Apply color scheme to documents

**Features**:
- Interactive hover information showing document text
- Color-coded by document type
- Configurable titles, dimensions, and random state
- Export to HTML for sharing

**Workflow**:
1. Retrieve embeddings and metadata from Chroma
2. Apply t-SNE to reduce dimensions (2D or 3D)
3. Map document types to colors
4. Create Plotly scatter plots
5. Add hover text with document preview

**Use Cases**:
- Understanding document clustering
- Quality assurance of embeddings
- Identifying similar document groups
- Debugging retrieval issues

### 8. RAG System (`src/rag_system.py`)

**Purpose**: Orchestrate entire RAG pipeline (Note: Uses legacy architecture, may need update for LangChain)

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

**Note**: Current implementation references legacy modules. For production use with LangChain, refer to notebooks/pipeline.ipynb

## Data Flow

### Indexing Phase (LangChain + Chroma)

```
Documents → fetch_documents() → LangChain Documents
    ↓
chunking() → RecursiveCharacterTextSplitter
    ↓
embedder() → HuggingFaceEmbeddings (e5-large-v2)
    ↓
Chroma.from_documents() → Persistent Vector Store (vectors/)
```

1. **Ingestion**: Load documents from disk with metadata
2. **Document Creation**: Convert to LangChain Document objects
3. **Chunking**: Split using RecursiveCharacterTextSplitter
4. **Embedding**: Generate vectors using e5-large-v2 model
5. **Storage**: Persist to Chroma database with full metadata

### Query Phase

```
User Query → HuggingFaceEmbeddings
    ↓
Chroma.similarity_search()
    ↓
Retrieve Top-K Documents with Metadata
    ↓
Context Assembly → LLM Prompt
    ↓
LLM Generation → Grounded Response
```

1. **Query Embedding**: Convert query to vector using same embedder
2. **Similarity Search**: Find top-k similar chunks in Chroma
3. **Metadata Filtering**: Optional filtering by document type or source
4. **Context Assembly**: Build prompt with retrieved chunks
5. **LLM Generation**: Generate contextual response with sources

## Configuration Files

### config.json
Main system configuration

### .env
Environment variables (API keys, paths)

## Extension Points

### Custom Components (LangChain-Based)

1. **Custom Embedder**:
   ```python
   from langchain_huggingface import HuggingFaceEmbeddings
   
   # Use different HuggingFace model
   embeddings = HuggingFaceEmbeddings(
       model_name="your-model-name",
       encode_kwargs={"normalize_embeddings": True}
   )
   ```

2. **Custom Vector Store**:
   ```python
   from langchain_community.vectorstores import Pinecone, FAISS
   
   # Switch to different vector store
   vectorstore = Pinecone.from_documents(
       documents=chunks, 
       embedding=embeddings,
       index_name="your-index"
   )
   ```

3. **Custom Text Splitter**:
   ```python
   from langchain_text_splitters import CharacterTextSplitter
   
   # Use different splitting strategy
   splitter = CharacterTextSplitter(
       chunk_size=500,
       chunk_overlap=50
   )
   ```

4. **Custom LLM Integration**:
   ```python
   from langchain_openai import ChatOpenAI
   from langchain_anthropic import ChatAnthropic
   
   # Use different LLM provider
   llm = ChatAnthropic(model="claude-3-opus")
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

### Chroma (Current Implementation)
- Good for: <10 million vectors
- Memory: ~4GB per 1M vectors (1024-dim e5-large-v2)
- Search: O(log n) with HNSW indexing
- Storage: Persistent SQLite + file-based
- Advantages: Zero config, persistent, metadata support
- Best for: Small to medium document collections

### Alternative Vector Stores (via LangChain)

#### Pinecone
- Good for: 1M - 1B+ vectors
- Search: O(1) - cloud-managed
- Advantages: Serverless, fully managed, high performance
- Use case: Production apps with large scale

#### Weaviate
- Good for: 1M - 100M+ vectors
- Search: O(log n) with HNSW
- Advantages: Hybrid search, GraphQL API, advanced filtering
- Use case: Complex metadata queries

#### FAISS
- Good for: 1M - 1B vectors
- Search: O(log n) - approximate
- Setup: Local or distributed
- Use case: High-performance local deployments

## Error Handling

System implements graceful degradation:
1. Missing files → Skip with warning
2. Unsupported formats → Log and continue
3. API failures → Retry with exponential backoff
4. Memory issues → Process in batches

---

For more details, see component-specific documentation in `docs/`
