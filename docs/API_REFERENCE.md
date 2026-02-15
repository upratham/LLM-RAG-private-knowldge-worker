# API Reference

## Core Components

### RAGSystem
Main orchestrator for the RAG system.

```python
from src.rag_system import RAGSystem

rag = RAGSystem(config_path='./config/config.json')
```

#### Methods

- `ingest_documents(data_path: str) -> int`: Load documents from directory
- `build_index() -> int`: Create vector index from documents
- `query(query: str, top_k: int = 5) -> dict`: Query the system
- `save_index(path: str)`: Save index to disk
- `load_index(path: str)`: Load index from disk

### DataIngestionPipeline
Handle document loading.

```python
from src.data_ingestion import DataIngestionPipeline

pipeline = DataIngestionPipeline()
docs = pipeline.ingest_from_directory('./data/raw')
```

### TextSplitter
Split text into chunks.

```python
from src.chunking import RecursiveCharacterSplitter

splitter = RecursiveCharacterSplitter(chunk_size=1000, overlap=100)
chunks = splitter.split(text)
```

### EmbeddingGenerator
Generate embeddings.

```python
from src.embeddings import EmbeddingGenerator, HuggingFaceEmbedder

embedder = EmbeddingGenerator(embedder=HuggingFaceEmbedder())
embedding = embedder.embed_text("Your text here")
```

### VectorStore
Store and retrieve embeddings.

```python
from src.vector_store import VectorStore, InMemoryVectorStore

store = VectorStore(store=InMemoryVectorStore())
store.add(texts, embeddings, metadata)
results = store.search(query_embedding, k=5)
```

### Retriever
Retrieve relevant documents.

```python
from src.retrieval import Retriever, VectorRetriever

retriever = Retriever(retriever=VectorRetriever(embedder, store))
results = retriever.retrieve("Your query", k=5)
```

### LLMProvider
Generate responses using LLM.

```python
from src.llm import LLMProvider, OpenAILLM

llm = LLMProvider(llm=OpenAILLM(api_key='sk-...'))
response = llm.generate("Your prompt")
```

## Advanced Usage

### Custom Embedder

```python
from src.embeddings import EmbeddingGenerator, BaseEmbedder
import numpy as np

class CustomEmbedder(BaseEmbedder):
    def embed(self, text: str) -> np.ndarray:
        # Your embedding logic
        pass

embedder = EmbeddingGenerator(embedder=CustomEmbedder())
```

### Custom Vector Store

```python
from src.vector_store import VectorStore, BaseVectorStore

class CustomVectorStore(BaseVectorStore):
    def add_vectors(self, texts, embeddings, metadata=None):
        # Your implementation
        pass

store = VectorStore(store=CustomVectorStore())
```

See examples/ for more detailed usage patterns.
