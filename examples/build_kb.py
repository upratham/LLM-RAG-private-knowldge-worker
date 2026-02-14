"""
Example: Building a knowledge base from documents
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rag_llm.ingestion import DocumentLoader, TextSplitter
from rag_llm.embeddings import EmbeddingModel, VectorStore
from rag_llm.utils import setup_logger


def build_knowledge_base():
    """Build a knowledge base from documents"""
    
    logger = setup_logger()
    
    logger.info("Starting knowledge base construction...")
    
    # Configuration
    documents_path = "data/documents"
    vector_store_path = "data/vector_store"
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Step 1: Load documents
    logger.info(f"Loading documents from: {documents_path}")
    loader = DocumentLoader(documents_path)
    documents = loader.load()
    logger.info(f"Loaded {len(documents)} documents")
    
    if not documents:
        logger.warning("No documents found. Please add documents to data/documents/")
        return
    
    # Step 2: Split into chunks
    logger.info("Splitting documents into chunks...")
    splitter = TextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    logger.info(f"Created {len(chunks)} chunks")
    
    # Step 3: Generate embeddings
    logger.info(f"Generating embeddings using {embedding_model_name}...")
    embedding_model = EmbeddingModel(embedding_model_name)
    embeddings = embedding_model.embed_texts([chunk['content'] for chunk in chunks])
    logger.info(f"Generated embeddings with shape: {embeddings.shape}")
    
    # Step 4: Store in vector database
    logger.info(f"Storing embeddings in: {vector_store_path}")
    vector_store = VectorStore(storage_path=vector_store_path)
    vector_store.add_documents(chunks, embeddings)
    vector_store.save()
    
    logger.info("Knowledge base built successfully!")
    logger.info(f"Total documents: {len(documents)}")
    logger.info(f"Total chunks: {len(chunks)}")
    logger.info(f"Vector store location: {vector_store_path}")


if __name__ == "__main__":
    build_knowledge_base()
