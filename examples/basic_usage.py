"""
Example: Basic RAG System Usage
"""

from src.rag_system import RAGSystem
from src.embeddings import EmbeddingGenerator, DummyEmbedder
from pathlib import Path
import json


def example_basic_usage():
    """Basic RAG system usage example"""
    
    # Initialize RAG system
    rag = RAGSystem(config_path='./config/config.json')
    
    # Create sample data for demonstration
    sample_dir = Path('./data/raw')
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a sample document
    sample_data = """
    Machine Learning is a subset of Artificial Intelligence that focuses on
    training algorithms to learn from data. It involves using statistical
    techniques to give computer systems the ability to improve from experience.
    
    There are three main types of machine learning:
    1. Supervised Learning - learning from labeled data
    2. Unsupervised Learning - finding patterns in unlabeled data
    3. Reinforcement Learning - learning through rewards and punishments
    """
    
    sample_file = sample_dir / 'sample.txt'
    sample_file.write_text(sample_data)
    
    # Ingest documents
    print("Ingesting documents...")
    rag.ingest_documents(str(sample_dir))
    
    # Build index
    print("Building index...")
    chunks = rag.build_index()
    print(f"Indexed {chunks} chunks")
    
    # Query the system
    print("\nQuerying the system...")
    query = "What are the types of machine learning?"
    results = rag.query(query, top_k=3)
    
    print(f"\nQuery: {results['query']}")
    print(f"Response: {results['response']}")
    print(f"\nSimilarity Scores: {results['scores']}")
    
    # Save index
    print("\nSaving index...")
    rag.save_index('./vectors/index.json')


def example_custom_embedder():
    """Example with custom embedder"""
    
    from src.embeddings import EmbeddingGenerator, DummyEmbedder
    
    # Use dummy embedder for quick testing
    dummy_embedder = DummyEmbedder(dimension=384)
    embedder = EmbeddingGenerator(embedder=dummy_embedder)
    
    text = "This is a test document"
    embedding = embedder.embed_text(text)
    print(f"Embedding shape: {embedding.shape}")


if __name__ == '__main__':
    print("=" * 60)
    print("RAG System - Basic Usage Example")
    print("=" * 60)
    example_basic_usage()
    
    print("\n" + "=" * 60)
    print("Custom Embedder Example")
    print("=" * 60)
    example_custom_embedder()
