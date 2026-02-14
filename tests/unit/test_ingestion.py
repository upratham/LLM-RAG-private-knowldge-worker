"""
Unit tests for document ingestion module
"""

import unittest
from pathlib import Path
from rag_llm.ingestion import TextSplitter


class TestTextSplitter(unittest.TestCase):
    """Test TextSplitter functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.splitter = TextSplitter(chunk_size=100, chunk_overlap=20)
    
    def test_split_short_text(self):
        """Test splitting text shorter than chunk size"""
        text = "This is a short text."
        chunks = self.splitter.split_text(text)
        
        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0], text)
    
    def test_split_long_text(self):
        """Test splitting long text into multiple chunks"""
        text = "This is a sentence. " * 20  # Create long text
        chunks = self.splitter.split_text(text)
        
        self.assertGreater(len(chunks), 1)
        for chunk in chunks:
            self.assertLessEqual(len(chunk), 100 + 50)  # Allow some margin
    
    def test_split_documents(self):
        """Test splitting documents"""
        documents = [
            {
                'content': "This is document 1. " * 10,
                'metadata': {'source': 'test1.txt'}
            },
            {
                'content': "This is document 2. " * 10,
                'metadata': {'source': 'test2.txt'}
            }
        ]
        
        chunks = self.splitter.split_documents(documents)
        
        self.assertGreater(len(chunks), 2)
        for chunk in chunks:
            self.assertIn('content', chunk)
            self.assertIn('metadata', chunk)
            self.assertIn('chunk_id', chunk['metadata'])


if __name__ == '__main__':
    unittest.main()
