"""Tests for text processing utilities."""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.rag.utils.text_processing import chunk_text, clean_text, extract_sentences


class TestTextProcessing:
    """Test cases for text processing utilities."""
    
    def test_chunk_text_basic(self):
        """Test basic text chunking."""
        text = "A" * 1000
        chunks = chunk_text(text, chunk_size=100, overlap=10)
        
        assert len(chunks) > 1
        assert all(len(chunk) <= 100 for chunk in chunks)
    
    def test_chunk_text_with_overlap(self):
        """Test that chunks have proper overlap."""
        text = "ABCDEFGHIJ" * 10  # 100 characters
        chunks = chunk_text(text, chunk_size=20, overlap=5)
        
        # Check that overlap exists
        assert len(chunks) > 1
        # Adjacent chunks should share some content
        for i in range(len(chunks) - 1):
            # The end of one chunk should relate to the start of the next
            assert len(chunks[i]) <= 20
    
    def test_chunk_text_invalid_params(self):
        """Test chunk_text with invalid parameters."""
        text = "Test text"
        
        with pytest.raises(ValueError):
            chunk_text(text, chunk_size=0, overlap=0)
        
        with pytest.raises(ValueError):
            chunk_text(text, chunk_size=10, overlap=-1)
        
        with pytest.raises(ValueError):
            chunk_text(text, chunk_size=10, overlap=10)
    
    def test_clean_text(self):
        """Test text cleaning."""
        text = "  This   has    extra    spaces  "
        cleaned = clean_text(text)
        
        assert cleaned == "This has extra spaces"
    
    def test_clean_text_with_newlines(self):
        """Test cleaning text with newlines."""
        text = "Line 1\n\n\nLine 2\n   Line 3"
        cleaned = clean_text(text)
        
        assert "  " not in cleaned
        assert cleaned.startswith("Line 1")
        assert cleaned.endswith("Line 3")
    
    def test_extract_sentences(self):
        """Test sentence extraction."""
        text = "First sentence. Second sentence! Third sentence?"
        sentences = extract_sentences(text)
        
        assert len(sentences) == 3
        assert "First sentence" in sentences[0]
        assert "Second sentence" in sentences[1]
        assert "Third sentence" in sentences[2]
    
    def test_extract_sentences_empty(self):
        """Test sentence extraction from empty text."""
        sentences = extract_sentences("")
        assert len(sentences) == 0
