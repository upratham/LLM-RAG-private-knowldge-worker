"""
Example: Querying the knowledge base
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rag_llm.embeddings import EmbeddingModel, VectorStore
from rag_llm.retrieval import Retriever
from rag_llm.llm import LLMClient
from rag_llm.query_processor import QueryProcessor
from rag_llm.utils import setup_logger


def query_knowledge_base(query: str):
    """Query the knowledge base"""
    
    logger = setup_logger()
    
    logger.info("Loading knowledge base...")
    
    # Configuration
    vector_store_path = "data/vector_store"
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    llm_model = "gpt-3.5-turbo"
    llm_provider = "openai"
    
    # Load vector store
    vector_store = VectorStore(storage_path=vector_store_path)
    vector_store.load()
    logger.info("Vector store loaded")
    
    # Initialize components
    embedding_model = EmbeddingModel(embedding_model_name)
    retriever = Retriever(vector_store, embedding_model)
    llm_client = LLMClient(model_name=llm_model, provider=llm_provider)
    
    # Initialize query processor
    processor = QueryProcessor(retriever, llm_client, k=5)
    
    # Process query
    logger.info(f"Processing query: {query}")
    result = processor.process_query(query)
    
    # Display results
    print("\n" + "=" * 80)
    print("QUERY:")
    print(query)
    print("\n" + "=" * 80)
    print("ANSWER:")
    print(result['answer'])
    print("\n" + "=" * 80)
    print("RETRIEVED SOURCES:")
    for i, source in enumerate(result['sources'], 1):
        print(f"\n{i}. Relevance Score: {source['score']:.4f}")
        print(f"   Source: {source['metadata'].get('source', 'Unknown')}")
        print(f"   Content Preview: {source['content']}")
    print("=" * 80)


if __name__ == "__main__":
    # Example queries
    queries = [
        "What is the main topic discussed in the documents?",
        "Can you summarize the key points?",
    ]
    
    # Use first query or get from command line
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = queries[0]
    
    query_knowledge_base(query)
