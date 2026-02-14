"""Retriever for finding relevant documents."""

from typing import List, Dict, Any
from .embeddings import EmbeddingGenerator
from .vector_store import VectorStore


class Retriever:
    """
    Retrieves relevant documents based on a query.
    """
    
    def __init__(self, vector_store: VectorStore, embedding_generator: EmbeddingGenerator):
        """
        Initialize the retriever.
        
        Args:
            vector_store: Vector store containing document embeddings
            embedding_generator: Embedding generator for query embedding
        """
        self.vector_store = vector_store
        self.embedding_generator = embedding_generator
    
    def retrieve(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve the k most relevant documents for a query.
        
        Args:
            query: Query string
            k: Number of documents to retrieve
            
        Returns:
            List of dicts containing document content, score, and metadata
        """
        # Generate embedding for the query
        query_embedding = self.embedding_generator.embed_text(query)
        
        # Search in vector store
        results = self.vector_store.search(query_embedding, k=k)
        
        # Format results
        formatted_results = []
        for doc, score, metadata in results:
            formatted_results.append({
                'content': doc,
                'score': score,
                'metadata': metadata
            })
        
        return formatted_results
