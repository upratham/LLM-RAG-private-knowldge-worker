"""
Vector store for storing and retrieving embeddings
"""

import os
import pickle
from typing import List, Dict, Any, Tuple
import numpy as np
from pathlib import Path


class VectorStore:
    """
    Store and retrieve document embeddings using FAISS or simple numpy-based search
    """
    
    def __init__(self, storage_path: str = "data/vector_store", use_faiss: bool = True):
        """
        Initialize vector store
        
        Args:
            storage_path: Path to store the vector database
            use_faiss: Whether to use FAISS for efficient similarity search
        """
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.use_faiss = use_faiss
        
        self.embeddings = []
        self.documents = []
        self.index = None
        
        if use_faiss:
            try:
                import faiss
                self.faiss = faiss
            except ImportError:
                print("FAISS not installed. Install with: pip install faiss-cpu")
                self.use_faiss = False
    
    def add_documents(self, documents: List[Dict[str, Any]], embeddings: np.ndarray):
        """
        Add documents and their embeddings to the vector store
        
        Args:
            documents: List of document dictionaries
            embeddings: Array of embedding vectors
        """
        self.documents.extend(documents)
        
        if len(self.embeddings) == 0:
            self.embeddings = embeddings
        else:
            self.embeddings = np.vstack([self.embeddings, embeddings])
        
        # Build or update the index
        self._build_index()
    
    def _build_index(self):
        """Build the search index"""
        if self.use_faiss and len(self.embeddings) > 0:
            dimension = self.embeddings.shape[1]
            self.index = self.faiss.IndexFlatL2(dimension)
            self.index.add(self.embeddings.astype('float32'))
    
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Tuple[Dict[str, Any], float]]:
        """
        Search for similar documents
        
        Args:
            query_embedding: Query embedding vector
            k: Number of results to return
            
        Returns:
            List of (document, score) tuples
        """
        if len(self.embeddings) == 0:
            return []
        
        if self.use_faiss and self.index is not None:
            return self._search_faiss(query_embedding, k)
        else:
            return self._search_numpy(query_embedding, k)
    
    def _search_faiss(self, query_embedding: np.ndarray, k: int) -> List[Tuple[Dict[str, Any], float]]:
        """Search using FAISS index"""
        query_embedding = query_embedding.reshape(1, -1).astype('float32')
        distances, indices = self.index.search(query_embedding, min(k, len(self.documents)))
        
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(self.documents):
                results.append((self.documents[idx], float(distance)))
        
        return results
    
    def _search_numpy(self, query_embedding: np.ndarray, k: int) -> List[Tuple[Dict[str, Any], float]]:
        """Search using numpy cosine similarity"""
        # Compute cosine similarity
        query_norm = query_embedding / np.linalg.norm(query_embedding)
        embeddings_norm = self.embeddings / np.linalg.norm(self.embeddings, axis=1, keepdims=True)
        similarities = np.dot(embeddings_norm, query_norm)
        
        # Get top k indices
        top_k_indices = np.argsort(similarities)[::-1][:k]
        
        results = []
        for idx in top_k_indices:
            results.append((self.documents[idx], float(similarities[idx])))
        
        return results
    
    def save(self, name: str = "vector_store"):
        """
        Save the vector store to disk
        
        Args:
            name: Name for the saved vector store
        """
        save_path = self.storage_path / f"{name}.pkl"
        
        data = {
            'embeddings': self.embeddings,
            'documents': self.documents
        }
        
        with open(save_path, 'wb') as f:
            pickle.dump(data, f)
        
        print(f"Vector store saved to {save_path}")
    
    def load(self, name: str = "vector_store"):
        """
        Load the vector store from disk
        
        Args:
            name: Name of the saved vector store
        """
        load_path = self.storage_path / f"{name}.pkl"
        
        if not load_path.exists():
            print(f"Vector store not found at {load_path}")
            return
        
        with open(load_path, 'rb') as f:
            data = pickle.load(f)
        
        self.embeddings = data['embeddings']
        self.documents = data['documents']
        
        # Rebuild index
        self._build_index()
        
        print(f"Vector store loaded from {load_path}")
    
    def clear(self):
        """Clear all documents and embeddings"""
        self.embeddings = []
        self.documents = []
        self.index = None
