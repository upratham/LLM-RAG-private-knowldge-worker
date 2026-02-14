"""Tests for document loader."""

import pytest
from pathlib import Path
import tempfile
import os

# Assuming the test is run from the project root
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.rag.core.document_loader import DocumentLoader, Document


class TestDocumentLoader:
    """Test cases for DocumentLoader."""
    
    def test_load_text_file(self):
        """Test loading a text file."""
        # Create a temporary text file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("This is a test document.")
            temp_path = f.name
        
        try:
            loader = DocumentLoader()
            documents = loader.load_document(temp_path)
            
            assert len(documents) == 1
            assert documents[0].content == "This is a test document."
            assert documents[0].metadata['file_type'] == 'text'
        finally:
            os.unlink(temp_path)
    
    def test_load_markdown_file(self):
        """Test loading a markdown file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("# Heading\n\nContent here.")
            temp_path = f.name
        
        try:
            loader = DocumentLoader()
            documents = loader.load_document(temp_path)
            
            assert len(documents) == 1
            assert "# Heading" in documents[0].content
        finally:
            os.unlink(temp_path)
    
    def test_file_not_found(self):
        """Test handling of non-existent file."""
        loader = DocumentLoader()
        
        with pytest.raises(FileNotFoundError):
            loader.load_document("nonexistent_file.txt")
    
    def test_unsupported_file_type(self):
        """Test handling of unsupported file type."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xyz', delete=False) as f:
            f.write("Test content")
            temp_path = f.name
        
        try:
            loader = DocumentLoader()
            
            with pytest.raises(ValueError):
                loader.load_document(temp_path)
        finally:
            os.unlink(temp_path)


class TestDocument:
    """Test cases for Document class."""
    
    def test_document_creation(self):
        """Test creating a document."""
        doc = Document(content="Test content", metadata={'source': 'test.txt'})
        
        assert doc.content == "Test content"
        assert doc.metadata['source'] == 'test.txt'
    
    def test_document_without_metadata(self):
        """Test creating a document without metadata."""
        doc = Document(content="Test content")
        
        assert doc.content == "Test content"
        assert doc.metadata == {}
