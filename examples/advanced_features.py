"""
Example: Advanced RAG Features
"""

from src.data_ingestion import DataIngestionPipeline
from src.chunking import RecursiveCharacterSplitter
from src.embeddings import EmbeddingGenerator, DummyEmbedder
from src.vector_store import VectorStore, InMemoryVectorStore
from pathlib import Path
import json


def example_document_processing():
    """Example of document processing pipeline"""
    
    print("Document Processing Pipeline Example")
    print("-" * 40)
    
    # Initialize pipeline
    pipeline = DataIngestionPipeline()
    
    # Create sample documents
    sample_dir = Path('./data/raw/examples')
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Create multiple sample files
    documents = {
        'nlp.txt': """
        Natural Language Processing (NLP) is a branch of artificial intelligence
        that helps computers understand, interpret, and generate human language.
        NLP tasks include: tokenization, POS tagging, entity recognition, etc.
        """,
        'cv.txt': """
        Computer Vision is the field of artificial intelligence that deals with
        automated visual perception. Common tasks include image classification,
        object detection, and image segmentation.
        """,
    }
    
    for filename, content in documents.items():
        (sample_dir / filename).write_text(content)
    
    # Ingest documents
    docs = pipeline.ingest_from_directory(str(sample_dir))
    print(f"Ingested {len(docs)} documents")
    for doc in docs:
        print(f"  - {doc['file_name']}")
    
    # Process with text splitter
    print("\nProcessing with text splitter...")
    splitter = RecursiveCharacterSplitter(chunk_size=200, overlap=50)
    
    all_chunks = []
    for doc in pipeline.get_documents():
        for content in doc['content']:
            chunks = splitter.split(content)
            all_chunks.extend(chunks)
            print(f"  Split {doc['file_name']} into {len(chunks)} chunks")
    
    print(f"\nTotal chunks: {len(all_chunks)}")
    
    # Generate embeddings and store
    print("\nGenerating embeddings...")
    embedder = EmbeddingGenerator(embedder=DummyEmbedder(dimension=384))
    embeddings = embedder.embed_texts(all_chunks)
    
    # Create vector store
    vector_store = VectorStore(store=InMemoryVectorStore())
    vector_store.add(all_chunks, embeddings)
    
    print(f"Vector store contains {len(all_chunks)} vectors")
    
    # Perform search
    print("\nPerforming semantic search...")
    query = "machine learning and neural networks"
    query_embedding = embedder.embed_text(query)
    results = vector_store.search(query_embedding, k=3)
    
    print(f"Query: '{query}'")
    print("Top results:")
    for i, (doc, score) in enumerate(results, 1):
        print(f"  {i}. [Score: {score:.4f}] {doc[:60]}...")


if __name__ == '__main__':
    print("=" * 60)
    print("Advanced RAG Features Example")
    print("=" * 60)
    example_document_processing()
