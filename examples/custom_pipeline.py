"""
Example: Building RAG with Custom Components
"""

from src.embeddings import EmbeddingGenerator, DummyEmbedder
from src.vector_store import VectorStore, InMemoryVectorStore
from src.retrieval import VectorRetriever, Retriever
from src.llm import LLMProvider, DummyLLM
import numpy as np


def example_custom_pipeline():
    """Example with custom components"""
    
    # Initialize components with custom configurations
    print("Initializing custom RAG pipeline...")
    
    # Use dummy embedder for demonstration
    embedder = EmbeddingGenerator(embedder=DummyEmbedder(dimension=384))
    
    # Initialize vector store
    vector_store = VectorStore(store=InMemoryVectorStore())
    
    # Create some sample documents and embeddings
    documents = [
        "Python is a high-level programming language",
        "Machine learning is a subset of artificial intelligence",
        "Deep learning uses neural networks with multiple layers",
    ]
    
    # Generate embeddings
    embeddings = embedder.embed_texts(documents)
    
    # Add to vector store
    vector_store.add(documents, embeddings)
    print(f"Added {len(documents)} documents to vector store")
    
    # Create retriever
    vector_retriever = VectorRetriever(embedder, vector_store)
    retriever = Retriever(retriever=vector_retriever)
    
    # Retrieve documents
    query = "Tell me about programming"
    results = retriever.retrieve(query, k=2)
    print(f"\nQuery: {query}")
    print("Retrieved documents:")
    for doc, score in results:
        print(f"  - {doc[:50]}... (score: {score:.4f})")
    
    # Generate response using LLM
    llm_provider = LLMProvider(llm=DummyLLM())
    prompt = f"Based on these documents: {[doc[0][:30] for doc in results]}, answer: {query}"
    response = llm_provider.generate(prompt)
    print(f"\nLLM Response: {response}")


if __name__ == '__main__':
    print("=" * 60)
    print("Custom RAG Pipeline Example")
    print("=" * 60)
    example_custom_pipeline()
