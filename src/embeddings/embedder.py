"""
Embedding Generator - Create embeddings for text chunks
"""

from typing import List
from abc import ABC, abstractmethod
import numpy as np


class BaseEmbedder(ABC):
    """Base class for embedding generators"""
    
    @abstractmethod
    def embed(self, text: str) -> np.ndarray:
        """Generate embedding for a single text"""
        pass
    
    @abstractmethod
    def embed_batch(self, texts: List[str]) -> List[np.ndarray]:
        """Generate embeddings for multiple texts"""
        pass


class DummyEmbedder(BaseEmbedder):
    """Dummy embedder for testing - returns random vectors"""
    
    def __init__(self, dimension: int = 384):
        self.dimension = dimension
    
    def embed(self, text: str) -> np.ndarray:
        """Generate random embedding"""
        return np.random.randn(self.dimension).astype(np.float32)
    
    def embed_batch(self, texts: List[str]) -> List[np.ndarray]:
        """Generate random embeddings for batch"""
        return [self.embed(text) for text in texts]


class HuggingFaceEmbedder(BaseEmbedder):
    """HuggingFace-based embedder"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize HuggingFace embedder
        
        Args:
            model_name: HuggingFace model identifier
        """
        self.model_name = model_name
        self.model = None
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the embedder model"""
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(self.model_name)
        except ImportError:
            raise ImportError(
                "sentence-transformers is required. Install with: "
                "pip install sentence-transformers"
            )
    
    def embed(self, text: str) -> np.ndarray:
        """Generate embedding for text"""
        if self.model is None:
            self._initialize_model()
        return self.model.encode(text, convert_to_numpy=True)
    
    def embed_batch(self, texts: List[str]) -> List[np.ndarray]:
        """Generate embeddings for batch of texts"""
        if self.model is None:
            self._initialize_model()
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return [emb for emb in embeddings]


class EmbeddingGenerator:
    """Main embedding generator interface"""
    
    def __init__(self, embedder: BaseEmbedder = None):
        """Initialize with embedder"""
        self.embedder = embedder or DummyEmbedder()
    
    def embed_text(self, text: str) -> np.ndarray:
        """Generate embedding for text"""
        return self.embedder.embed(text)
    
    def embed_texts(self, texts: List[str]) -> List[np.ndarray]:
        """Generate embeddings for texts"""
        return self.embedder.embed_batch(texts)
    
    def set_embedder(self, embedder: BaseEmbedder):
        """Change embedder"""
        self.embedder = embedder
