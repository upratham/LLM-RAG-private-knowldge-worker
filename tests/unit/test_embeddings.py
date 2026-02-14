"""
Unit tests for embedding module
"""

import unittest
import numpy as np
from rag_llm.embeddings import EmbeddingModel


class TestEmbeddingModel(unittest.TestCase):
    """Test EmbeddingModel functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.model = EmbeddingModel()
    
    def test_embed_single_text(self):
        """Test embedding a single text"""
        text = "This is a test sentence."
        embedding = self.model.embed_text(text)
        
        self.assertIsInstance(embedding, np.ndarray)
        self.assertEqual(len(embedding.shape), 1)
        self.assertGreater(len(embedding), 0)
    
    def test_embed_multiple_texts(self):
        """Test embedding multiple texts"""
        texts = [
            "First sentence.",
            "Second sentence.",
            "Third sentence."
        ]
        embeddings = self.model.embed_texts(texts)
        
        self.assertIsInstance(embeddings, np.ndarray)
        self.assertEqual(len(embeddings.shape), 2)
        self.assertEqual(embeddings.shape[0], len(texts))
    
    def test_embedding_dimension(self):
        """Test getting embedding dimension"""
        dimension = self.model.get_embedding_dimension()
        
        self.assertIsInstance(dimension, int)
        self.assertGreater(dimension, 0)


if __name__ == '__main__':
    unittest.main()
