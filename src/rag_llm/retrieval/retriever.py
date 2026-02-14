"""
Retriever for finding relevant documents based on query
"""

from typing import List, Dict, Any
from ..embeddings import EmbeddingModel, VectorStore


class Retriever:
    """
    Retrieve relevant documents for a given query
    """
    
    def __init__(self, vector_store: VectorStore, embedding_model: EmbeddingModel):
        """
        Initialize retriever
        
        Args:
            vector_store: Vector store containing document embeddings
            embedding_model: Embedding model for query encoding
        """
        self.vector_store = vector_store
        self.embedding_model = embedding_model
    
    def retrieve(self, query: str, k: int = 5, score_threshold: float = None) -> List[Dict[str, Any]]:
        """
        Retrieve relevant documents for a query
        
        Args:
            query: Search query
            k: Number of documents to retrieve
            score_threshold: Optional minimum similarity score
            
        Returns:
            List of relevant documents with metadata and scores
        """
        # Generate query embedding
        query_embedding = self.embedding_model.embed_text(query)
        
        # Search vector store
        results = self.vector_store.search(query_embedding, k=k)
        
        # Filter by score threshold if provided
        if score_threshold is not None:
            results = [(doc, score) for doc, score in results if score >= score_threshold]
        
        # Format results
        retrieved_docs = []
        for doc, score in results:
            retrieved_doc = {
                'content': doc['content'],
                'metadata': doc['metadata'],
                'score': score
            }
            retrieved_docs.append(retrieved_doc)
        
        return retrieved_docs
    
    def retrieve_with_context(self, query: str, k: int = 5) -> str:
        """
        Retrieve documents and format them as context for LLM
        
        Args:
            query: Search query
            k: Number of documents to retrieve
            
        Returns:
            Formatted context string
        """
        docs = self.retrieve(query, k=k)
        
        if not docs:
            return "No relevant documents found."
        
        context_parts = []
        for i, doc in enumerate(docs, 1):
            context_parts.append(f"Document {i}:")
            context_parts.append(doc['content'])
            context_parts.append("")  # Empty line between documents
        
        return "\n".join(context_parts)
