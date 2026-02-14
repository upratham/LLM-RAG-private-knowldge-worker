"""Document loader for various file formats."""

import os
from pathlib import Path
from typing import List, Dict, Any
from abc import ABC, abstractmethod


class Document:
    """Represents a document with content and metadata."""
    
    def __init__(self, content: str, metadata: Dict[str, Any] = None):
        self.content = content
        self.metadata = metadata or {}
        
    def __repr__(self):
        return f"Document(content_length={len(self.content)}, metadata={self.metadata})"


class BaseDocumentLoader(ABC):
    """Base class for document loaders."""
    
    @abstractmethod
    def load(self, file_path: str) -> List[Document]:
        """Load documents from a file."""
        pass


class TextDocumentLoader(BaseDocumentLoader):
    """Loader for plain text files."""
    
    def load(self, file_path: str) -> List[Document]:
        """Load a text file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = {
            'source': file_path,
            'file_type': 'text',
            'file_name': os.path.basename(file_path)
        }
        
        return [Document(content=content, metadata=metadata)]


class DocumentLoader:
    """Main document loader that handles multiple file types."""
    
    def __init__(self):
        self.loaders = {
            '.txt': TextDocumentLoader(),
            '.md': TextDocumentLoader(),
        }
    
    def load_document(self, file_path: str) -> List[Document]:
        """Load a single document."""
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        extension = path.suffix.lower()
        
        if extension not in self.loaders:
            raise ValueError(f"Unsupported file type: {extension}")
        
        loader = self.loaders[extension]
        return loader.load(file_path)
    
    def load_directory(self, dir_path: str) -> List[Document]:
        """Load all supported documents from a directory."""
        documents = []
        path = Path(dir_path)
        
        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {dir_path}")
        
        for file_path in path.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in self.loaders:
                try:
                    docs = self.load_document(str(file_path))
                    documents.extend(docs)
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
        
        return documents
