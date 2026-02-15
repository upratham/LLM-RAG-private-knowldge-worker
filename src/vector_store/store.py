"""
Vector Store - Store and manage vector embeddings
"""

from typing import List, Dict, Tuple
from abc import ABC, abstractmethod
import numpy as np
import json
from pathlib import Path


class BaseVectorStore(ABC):
    """Base class for vector stores"""
    
    @abstractmethod
    def add_vectors(self, texts: List[str], embeddings: List[np.ndarray], metadata: List[Dict] = None):
        """Add vectors to store"""
        pass
    
    @abstractmethod
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Tuple[str, float]]:
        """Search for similar vectors"""
        pass


class InMemoryVectorStore(BaseVectorStore):
    """Simple in-memory vector store"""
    
    def __init__(self):
        self.vectors = []
        self.texts = []
        self.metadata = []
    
    def add_vectors(self, texts: List[str], embeddings: List[np.ndarray], metadata: List[Dict] = None):
        """Add vectors to store"""
        for i, (text, embedding) in enumerate(zip(texts, embeddings)):
            self.vectors.append(embedding)
            self.texts.append(text)
            self.metadata.append(metadata[i] if metadata else {})
    
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Tuple[str, float]]:
        """Search for similar vectors using cosine similarity"""
        if not self.vectors:
            return []
        
        # Normalize embeddings
        query_norm = query_embedding / (np.linalg.norm(query_embedding) + 1e-10)
        
        similarities = []
        for i, vec in enumerate(self.vectors):
            vec_norm = vec / (np.linalg.norm(vec) + 1e-10)
            similarity = np.dot(query_norm, vec_norm)
            similarities.append((self.texts[i], similarity, self.metadata[i]))
        
        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return [(text, score) for text, score, _ in similarities[:k]]
    
    def save(self, filepath: str):
        """Save vector store to disk"""
        data = {
            'vectors': [v.tolist() for v in self.vectors],
            'texts': self.texts,
            'metadata': self.metadata
        }
        with open(filepath, 'w') as f:
            json.dump(data, f)
    
    def load(self, filepath: str):
        """Load vector store from disk"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.vectors = [np.array(v) for v in data['vectors']]
        self.texts = data['texts']
        self.metadata = data['metadata']


class VectorStore:
    """Main vector store interface"""
    
    def __init__(self, store: BaseVectorStore = None):
        """Initialize with vector store"""
        self.store = store or InMemoryVectorStore()
    
    def add(self, texts: List[str], embeddings: List[np.ndarray], metadata: List[Dict] = None):
        """Add vectors"""
        self.store.add_vectors(texts, embeddings, metadata)
    
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Tuple[str, float]]:
        """Search vectors"""
        return self.store.search(query_embedding, k)
    
    def set_store(self, store: BaseVectorStore):
        """Change vector store"""
        self.store = store
