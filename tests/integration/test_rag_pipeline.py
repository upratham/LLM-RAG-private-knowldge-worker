"""
Integration tests for the complete RAG pipeline
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from rag_llm.ingestion import DocumentLoader, TextSplitter
from rag_llm.embeddings import EmbeddingModel, VectorStore
from rag_llm.retrieval import Retriever


class TestRAGPipeline(unittest.TestCase):
    """Test complete RAG pipeline"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_documents = [
            {
                'content': "Python is a high-level programming language. It is widely used for web development, data science, and automation.",
                'metadata': {'source': 'test1.txt'}
            },
            {
                'content': "Machine learning is a subset of artificial intelligence. It enables computers to learn from data without explicit programming.",
                'metadata': {'source': 'test2.txt'}
            }
        ]
    
    def test_end_to_end_pipeline(self):
        """Test the complete pipeline from ingestion to retrieval"""
        
        # Step 1: Split documents
        splitter = TextSplitter(chunk_size=100, chunk_overlap=20)
        chunks = splitter.split_documents(self.test_documents)
        self.assertGreater(len(chunks), 0)
        
        # Step 2: Generate embeddings
        embedding_model = EmbeddingModel()
        embeddings = embedding_model.embed_texts([chunk['content'] for chunk in chunks])
        self.assertEqual(embeddings.shape[0], len(chunks))
        
        # Step 3: Build vector store
        vector_store = VectorStore(storage_path="/tmp/test_vector_store")
        vector_store.add_documents(chunks, embeddings)
        
        # Step 4: Test retrieval
        retriever = Retriever(vector_store, embedding_model)
        results = retriever.retrieve("What is Python?", k=2)
        
        self.assertGreater(len(results), 0)
        self.assertIn('content', results[0])
        self.assertIn('metadata', results[0])
        self.assertIn('score', results[0])


if __name__ == '__main__':
    unittest.main()
