"""
Example: Basic RAG pipeline usage
"""

from rag_llm.ingestion import DocumentLoader, TextSplitter
from rag_llm.embeddings import EmbeddingModel, VectorStore
from rag_llm.retrieval import Retriever
from rag_llm.llm import LLMClient
from rag_llm.query_processor import QueryProcessor


def main():
    print("=" * 80)
    print("RAG LLM - Basic Example")
    print("=" * 80)
    
    # Step 1: Load documents
    print("\n1. Loading documents...")
    loader = DocumentLoader("data/documents")
    documents = loader.load()
    print(f"   Loaded {len(documents)} documents")
    
    # Step 2: Split into chunks
    print("\n2. Splitting documents into chunks...")
    splitter = TextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    print(f"   Created {len(chunks)} chunks")
    
    # Step 3: Generate embeddings
    print("\n3. Generating embeddings...")
    embedding_model = EmbeddingModel()
    embeddings = embedding_model.embed_texts([chunk['content'] for chunk in chunks])
    print(f"   Generated embeddings with shape: {embeddings.shape}")
    
    # Step 4: Build vector store
    print("\n4. Building vector store...")
    vector_store = VectorStore()
    vector_store.add_documents(chunks, embeddings)
    vector_store.save()
    print("   Vector store saved")
    
    # Step 5: Initialize retriever
    print("\n5. Initializing retriever...")
    retriever = Retriever(vector_store, embedding_model)
    
    # Step 6: Initialize LLM client
    print("\n6. Initializing LLM client...")
    llm_client = LLMClient()
    
    # Step 7: Initialize query processor
    print("\n7. Initializing query processor...")
    processor = QueryProcessor(retriever, llm_client)
    
    # Step 8: Process a query
    print("\n8. Processing query...")
    query = "What is this document about?"
    result = processor.process_query(query)
    
    print("\n" + "=" * 80)
    print("RESULT:")
    print("=" * 80)
    print(f"Query: {result['query']}")
    print(f"\nAnswer: {result['answer']}")
    print(f"\nSources: {len(result['sources'])} documents retrieved")
    print("=" * 80)


if __name__ == "__main__":
    main()
