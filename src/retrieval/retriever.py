"""
Retriever - Retrieve relevant documents for queries
"""

from typing import List, Tuple
from abc import ABC, abstractmethod
import numpy as np


class BaseRetriever(ABC):
    """Base class for retrievers"""
    
    @abstractmethod
    def retrieve(self, query: str, k: int = 5) -> List[Tuple[str, float]]:
        """Retrieve relevant documents"""
        pass


class VectorRetriever(BaseRetriever):
    """Retriever using vector similarity"""
    
    def __init__(self, embedder, vector_store):
        """
        Initialize retriever
        
        Args:
            embedder: EmbeddingGenerator instance
            vector_store: VectorStore instance
        """
        self.embedder = embedder
        self.vector_store = vector_store
    
    def retrieve(self, query: str, k: int = 5) -> List[Tuple[str, float]]:
        """Retrieve documents similar to query"""
        # Generate embedding for query
        query_embedding = self.embedder.embed_text(query)
        
        # Search vector store
        results = self.vector_store.search(query_embedding, k)
        
        return results


class Retriever:
    """Main retriever interface"""
    
    def __init__(self, retriever: BaseRetriever = None):
        """Initialize retriever"""
        self.retriever = retriever
    
    def retrieve(self, query: str, k: int = 5) -> List[Tuple[str, float]]:
        """Retrieve documents"""
        if self.retriever is None:
            raise ValueError("No retriever set")
        return self.retriever.retrieve(query, k)
    
    def set_retriever(self, retriever: BaseRetriever):
        """Change retriever"""
        self.retriever = retriever
