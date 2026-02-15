# Integration Guide

Guide for integrating external vector databases and LLM providers.

## Vector Database Integration

### 1. Faiss (Local)

Faiss is ideal for local/on-premise deployments.

```python
pip install faiss-cpu  # or faiss-gpu

from src.vector_store import BaseVectorStore, VectorStore
import faiss
import numpy as np

class FaissVectorStore(BaseVectorStore):
    def __init__(self, dimension: int = 384):
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []
        self.metadata = []
    
    def add_vectors(self, texts, embeddings, metadata=None):
        embeddings = np.array([e.astype(np.float32) for e in embeddings])
        self.index.add(embeddings)
        self.texts.extend(texts)
        self.metadata.extend(metadata or [{}] * len(texts))
    
    def search(self, query_embedding, k=5):
        query_embedding = query_embedding.astype(np.float32).reshape(1, -1)
        distances, indices = self.index.search(query_embedding, k)
        return [(self.texts[i], -distances[0][j]) 
                for j, i in enumerate(indices[0])]

# Usage
from src.vector_store import VectorStore
store = VectorStore(store=FaissVectorStore(dimension=384))
```

### 2. Pinecone (Cloud)

Pinecone is a serverless vector database.

```python
pip install pinecone-client

from pinecone import Pinecone
from src.vector_store import BaseVectorStore

class PineconeVectorStore(BaseVectorStore):
    def __init__(self, api_key: str, index_name: str = "rag"):
        self.pc = Pinecone(api_key=api_key)
        self.index = self.pc.Index(index_name)
    
    def add_vectors(self, texts, embeddings, metadata=None):
        vectors = []
        for i, (text, embedding) in enumerate(zip(texts, embeddings)):
            meta = (metadata[i] if metadata else {})
            meta['text'] = text
            vectors.append((f"id-{i}", embedding.tolist(), meta))
        self.index.upsert(vectors=vectors)
    
    def search(self, query_embedding, k=5):
        results = self.index.query(
            vector=query_embedding.tolist(),
            top_k=k,
            include_metadata=True
        )
        return [(m['metadata']['text'], m['score']) 
                for m in results['matches']]

# Usage
store = VectorStore(
    store=PineconeVectorStore(
        api_key='your-api-key',
        index_name='rag-index'
    )
)
```

### 3. Weaviate

Weaviate offers both open-source and cloud options.

```python
pip install weaviate-client

from weaviate import Client
from src.vector_store import BaseVectorStore

class WeaviateVectorStore(BaseVectorStore):
    def __init__(self, url: str = "http://localhost:8080"):
        self.client = Client(url)
    
    def add_vectors(self, texts, embeddings, metadata=None):
        schema = {
            "class": "Document",
            "properties": [
                {"name": "content", "dataType": ["text"]},
                {"name": "embedding", "dataType": ["number[]"]},
            ]
        }
        
        for text, embedding, meta in zip(
            texts, embeddings, metadata or [{}] * len(texts)
        ):
            self.client.data_object.create(
                class_name="Document",
                data_object={
                    "content": text,
                    "embedding": embedding.tolist(),
                    **meta
                }
            )
    
    def search(self, query_embedding, k=5):
        # Use Weaviate's GraphQL
        results = self.client.query.get("Document").with_near_vector(
            {"vector": query_embedding.tolist()},
            k=k
        ).with_fields(["content"]).do()
        
        return [(r['content'], r['_additional']['distance']) 
                for r in results['data']['Get']['Document']]

# Usage
store = VectorStore(store=WeaviateVectorStore())
```

### 4. Qdrant

Qdrant is another excellent open-source option.

```python
pip install qdrant-client

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from src.vector_store import BaseVectorStore

class QdrantVectorStore(BaseVectorStore):
    def __init__(self, url: str = "http://localhost:6333", 
                 collection: str = "rag"):
        self.client = QdrantClient(url=url)
        self.collection = collection
        self.counter = 0
    
    def add_vectors(self, texts, embeddings, metadata=None):
        points = []
        for text, embedding, meta in zip(
            texts, embeddings, metadata or [{}] * len(texts)
        ):
            self.counter += 1
            points.append({
                "id": self.counter,
                "vector": embedding.tolist(),
                "payload": {"text": text, **meta}
            })
        
        self.client.upsert(
            collection_name=self.collection,
            points=points
        )
    
    def search(self, query_embedding, k=5):
        results = self.client.search(
            collection_name=self.collection,
            query_vector=query_embedding.tolist(),
            limit=k
        )
        return [(r.payload['text'], r.score) for r in results]

# Usage
store = VectorStore(store=QdrantVectorStore())
```

## LLM Provider Integration

### 1. Anthropic Claude

```python
pip install anthropic

from src.llm import BaseLLM, LLMProvider

class ClaudeLLM(BaseLLM):
    def __init__(self, api_key: str, model: str = "claude-3-sonnet-20240229"):
        self.api_key = api_key
        self.model = model
        import anthropic
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=kwargs.get('max_tokens', 1024),
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

# Usage
llm = LLMProvider(llm=ClaudeLLM(api_key='your-api-key'))
response = llm.generate("Your prompt here")
```

### 2. Ollama (Local Models)

```python
# Install Ollama: https://ollama.ai
# Run: ollama serve
# Pull models: ollama pull llama2

from src.llm import BaseLLM, LLMProvider
import requests

class OllamaLLM(BaseLLM):
    def __init__(self, model: str = "llama2", url: str = "http://localhost:11434"):
        self.model = model
        self.url = url
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = requests.post(
            f"{self.url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "temperature": kwargs.get('temperature', 0.7),
            }
        )
        return response.json()['response']

# Usage
llm = LLMProvider(llm=OllamaLLM(model="llama2"))
```

### 3. Hugging Face Models

```python
pip install transformers torch

from src.llm import BaseLLM, LLMProvider

class HuggingFaceLLM(BaseLLM):
    def __init__(self, model_id: str = "gpt2"):
        from transformers import pipeline
        self.pipeline = pipeline("text-generation", model=model_id)
    
    def generate(self, prompt: str, **kwargs) -> str:
        result = self.pipeline(
            prompt,
            max_length=kwargs.get('max_tokens', 100),
            temperature=kwargs.get('temperature', 0.7),
            do_sample=True
        )
        return result[0]['generated_text']

# Usage
llm = LLMProvider(llm=HuggingFaceLLM())
```

### 4. Cohere API

```python
pip install cohere

from src.llm import BaseLLM, LLMProvider

class CohereLLM(BaseLLM):
    def __init__(self, api_key: str):
        import cohere
        self.client = cohere.Client(api_key)
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.generate(
            prompt=prompt,
            max_tokens=kwargs.get('max_tokens', 500),
            temperature=kwargs.get('temperature', 0.7)
        )
        return response.generations[0].text

# Usage
llm = LLMProvider(llm=CohereLLM(api_key='your-api-key'))
```

## Complete Integration Example

```python
from src.rag_system import RAGSystem
from src.vector_store import VectorStore
from src.llm import LLMProvider

# Setup Pinecone vector store
pinecone_store = VectorStore(
    store=PineconeVectorStore(api_key='your-key')
)

# Setup Claude LLM
claude_llm = LLMProvider(llm=ClaudeLLM(api_key='your-key'))

# Create RAG system with custom components
rag = RAGSystem()
rag.vector_store = pinecone_store
rag.llm_provider = claude_llm

# Use normally
rag.ingest_documents('./data/raw')
rag.build_index()
result = rag.query("Your question here")
```

## Performance Comparison

| DB | Latency | Cost | Setup | Scale |
|----|---------|------|-------|-------|
| In-Memory | <1ms | Free | Easy | <1M |
| Faiss | 1-10ms | Free | Medium | 1B |
| Qdrant | 5-50ms | Free/Paid | Medium | 1B |
| Pinecone | 50-200ms | Paid | Easy | ∞ |
| Weaviate | 50-200ms | Free/Paid | Medium | 1B |

## Recommendations

- **Development**: In-Memory or Faiss
- **Production (Single Server)**: Qdrant
- **Production (Distributed)**: Pinecone
- **Cost-Sensitive**: Qdrant or self-hosted Weaviate

---

See component documentation for more integration options.
