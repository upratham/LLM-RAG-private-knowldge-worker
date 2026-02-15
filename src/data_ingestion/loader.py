"""
Document Loader - Load files from various formats (PDF, TXT, DOCX, etc.)
"""

import os
from typing import List, Optional
from pathlib import Path
from abc import ABC, abstractmethod


class BaseLoader(ABC):
    """Base class for document loaders"""
    
    @abstractmethod
    def load(self, file_path: str) -> List[str]:
        """Load document and return list of pages/sections"""
        pass


class TextLoader(BaseLoader):
    """Load plain text files"""
    
    def load(self, file_path: str) -> List[str]:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [f.read()]


class DocumentLoader:
    """Main document loader supporting multiple formats"""
    
    SUPPORTED_FORMATS = {
        '.txt': TextLoader,
        # Add more format loaders as needed
        # '.pdf': PDFLoader,
        # '.docx': DocxLoader,
    }
    
    def __init__(self):
        self.loaders = self.SUPPORTED_FORMATS
    
    def load_from_directory(self, directory: str) -> List[dict]:
        """Load all supported documents from directory"""
        documents = []
        path = Path(directory)
        
        for file_path in path.rglob('*'):
            if file_path.is_file():
                doc = self.load_file(str(file_path))
                if doc:
                    documents.append(doc)
        
        return documents
    
    def load_file(self, file_path: str) -> Optional[dict]:
        """Load a single file"""
        try:
            suffix = Path(file_path).suffix.lower()
            
            if suffix not in self.loaders:
                print(f"Unsupported format: {suffix}")
                return None
            
            loader_class = self.loaders[suffix]
            loader = loader_class()
            content = loader.load(file_path)
            
            return {
                'file_path': file_path,
                'file_name': Path(file_path).name,
                'content': content,
                'format': suffix
            }
        
        except Exception as e:
            print(f"Error loading file {file_path}: {str(e)}")
            return None
