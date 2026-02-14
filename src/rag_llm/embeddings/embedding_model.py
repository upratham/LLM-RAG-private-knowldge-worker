"""
Embedding model for generating vector representations of text
"""

from typing import List, Union
import numpy as np


class EmbeddingModel:
    """
    Generate embeddings for text using various embedding models
    """
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize embedding model
        
        Args:
            model_name: Name of the embedding model to use
        """
        self.model_name = model_name
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load the embedding model"""
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(self.model_name)
            print(f"Loaded embedding model: {self.model_name}")
        except ImportError:
            print("sentence-transformers not installed. Install with: pip install sentence-transformers")
            self.model = None
    
    def embed_text(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single text
        
        Args:
            text: Input text
            
        Returns:
            Embedding vector as numpy array
        """
        if self.model is None:
            # Fallback to random embeddings for testing
            np.random.seed(hash(text) % 2**32)
            return np.random.rand(384)
        
        return self.model.encode(text, convert_to_numpy=True)
    
    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for multiple texts
        
        Args:
            texts: List of input texts
            
        Returns:
            Array of embedding vectors
        """
        if self.model is None:
            # Fallback to random embeddings for testing
            embeddings = []
            for text in texts:
                np.random.seed(hash(text) % 2**32)
                embeddings.append(np.random.rand(384))
            return np.array(embeddings)
        
        return self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
    
    def get_embedding_dimension(self) -> int:
        """
        Get the dimension of the embeddings
        
        Returns:
            Embedding dimension
        """
        if self.model is None:
            return 384  # Default dimension for fallback
        
        return self.model.get_sentence_embedding_dimension()
