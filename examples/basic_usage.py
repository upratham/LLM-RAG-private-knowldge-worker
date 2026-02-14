"""Example usage of the RAG pipeline."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.rag import RAGPipeline


def main():
    """Main example function."""
    print("=" * 50)
    print("RAG Pipeline Example")
    print("=" * 50)
    
    # Initialize RAG pipeline
    print("\n1. Initializing RAG pipeline...")
    rag = RAGPipeline(
        embedding_model="default",
        llm_model="default",
        vector_store_path="data/vector_store/store.json"
    )
    
    # Index documents (if data/documents directory has files)
    documents_path = "data/documents"
    if Path(documents_path).exists():
        print(f"\n2. Indexing documents from {documents_path}...")
        try:
            rag.index_documents(documents_path, is_directory=True)
        except Exception as e:
            print(f"   Note: {e}")
            print("   No documents found to index. Add some .txt or .md files to data/documents/")
    else:
        print(f"\n2. Documents directory not found: {documents_path}")
        print("   Create the directory and add some .txt or .md files to test indexing")
    
    # Get system stats
    print("\n3. System statistics:")
    stats = rag.get_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    # Example query (only if documents are indexed)
    if len(rag.vector_store) > 0:
        print("\n4. Example query:")
        query = "What is this document about?"
        print(f"   Question: {query}")
        
        response = rag.query(query, k=3, include_sources=True)
        print(f"\n   Answer: {response['answer']}")
        
        if response.get('sources'):
            print(f"\n   Sources ({len(response['sources'])} documents):")
            for i, source in enumerate(response['sources'], 1):
                print(f"   {i}. Score: {source['score']:.3f}")
                print(f"      Content: {source['content']}")
                print(f"      Metadata: {source['metadata']}")
    else:
        print("\n4. No documents indexed yet. Add documents to query the system.")
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
