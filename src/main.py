"""
Main entry point for RAG LLM application
"""

import argparse
from pathlib import Path
from rag_llm.ingestion import DocumentLoader, TextSplitter
from rag_llm.embeddings import EmbeddingModel, VectorStore
from rag_llm.retrieval import Retriever
from rag_llm.llm import LLMClient
from rag_llm.query_processor import QueryProcessor
from rag_llm.utils import setup_logger


def build_knowledge_base(
    documents_path: str,
    vector_store_path: str = "data/vector_store",
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
):
    """
    Build knowledge base from documents
    
    Args:
        documents_path: Path to documents directory
        vector_store_path: Path to save vector store
        embedding_model: Name of embedding model to use
    """
    logger = setup_logger()
    logger.info(f"Building knowledge base from: {documents_path}")
    
    # Load documents
    logger.info("Loading documents...")
    loader = DocumentLoader(documents_path)
    documents = loader.load()
    logger.info(f"Loaded {len(documents)} documents")
    
    if not documents:
        logger.warning("No documents loaded. Please check the documents path.")
        return
    
    # Split documents into chunks
    logger.info("Splitting documents into chunks...")
    splitter = TextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    logger.info(f"Created {len(chunks)} chunks")
    
    # Generate embeddings
    logger.info("Generating embeddings...")
    embedding_model = EmbeddingModel(embedding_model)
    embeddings = embedding_model.embed_texts([chunk['content'] for chunk in chunks])
    logger.info(f"Generated embeddings with shape: {embeddings.shape}")
    
    # Store in vector database
    logger.info("Storing embeddings in vector store...")
    vector_store = VectorStore(storage_path=vector_store_path)
    vector_store.add_documents(chunks, embeddings)
    vector_store.save()
    logger.info("Knowledge base built successfully!")


def query_knowledge_base(
    query: str,
    vector_store_path: str = "data/vector_store",
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
    llm_model: str = "gpt-3.5-turbo",
    llm_provider: str = "openai",
    k: int = 5
):
    """
    Query the knowledge base
    
    Args:
        query: User query
        vector_store_path: Path to vector store
        embedding_model: Name of embedding model
        llm_model: Name of LLM model
        llm_provider: LLM provider
        k: Number of documents to retrieve
    """
    logger = setup_logger()
    logger.info(f"Processing query: {query}")
    
    # Load vector store
    logger.info("Loading vector store...")
    vector_store = VectorStore(storage_path=vector_store_path)
    vector_store.load()
    
    # Initialize components
    embedding_model = EmbeddingModel(embedding_model)
    retriever = Retriever(vector_store, embedding_model)
    llm_client = LLMClient(model_name=llm_model, provider=llm_provider)
    
    # Initialize query processor
    processor = QueryProcessor(retriever, llm_client, k=k)
    
    # Process query
    logger.info("Processing query...")
    result = processor.process_query(query)
    
    # Display results
    print("\n" + "="*80)
    print("QUERY:")
    print(query)
    print("\n" + "="*80)
    print("ANSWER:")
    print(result['answer'])
    print("\n" + "="*80)
    print("SOURCES:")
    for i, source in enumerate(result['sources'], 1):
        print(f"\n{i}. Score: {source['score']:.4f}")
        print(f"   Source: {source['metadata'].get('source', 'Unknown')}")
        print(f"   Content: {source['content']}")
    print("="*80)


def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(description="RAG LLM - Private Knowledge Worker")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Build command
    build_parser = subparsers.add_parser('build', help='Build knowledge base from documents')
    build_parser.add_argument('documents_path', help='Path to documents directory')
    build_parser.add_argument('--vector-store', default='data/vector_store', help='Path to vector store')
    build_parser.add_argument('--embedding-model', default='sentence-transformers/all-MiniLM-L6-v2', help='Embedding model')
    
    # Query command
    query_parser = subparsers.add_parser('query', help='Query the knowledge base')
    query_parser.add_argument('query', help='Query string')
    query_parser.add_argument('--vector-store', default='data/vector_store', help='Path to vector store')
    query_parser.add_argument('--embedding-model', default='sentence-transformers/all-MiniLM-L6-v2', help='Embedding model')
    query_parser.add_argument('--llm-model', default='gpt-3.5-turbo', help='LLM model name')
    query_parser.add_argument('--llm-provider', default='openai', help='LLM provider')
    query_parser.add_argument('--k', type=int, default=5, help='Number of documents to retrieve')
    
    args = parser.parse_args()
    
    if args.command == 'build':
        build_knowledge_base(
            args.documents_path,
            args.vector_store,
            args.embedding_model
        )
    elif args.command == 'query':
        query_knowledge_base(
            args.query,
            args.vector_store,
            args.embedding_model,
            args.llm_model,
            args.llm_provider,
            args.k
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
