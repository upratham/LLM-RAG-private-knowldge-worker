"""
Data Ingestion Pipeline - Orchestrate document loading and preprocessing
"""

from typing import List
from .loader import DocumentLoader


class DataIngestionPipeline:
    """Pipeline for ingesting and preparing documents for RAG"""
    
    def __init__(self):
        self.loader = DocumentLoader()
        self.documents = []
    
    def ingest_from_directory(self, directory: str) -> List[dict]:
        """Load documents from directory"""
        self.documents = self.loader.load_from_directory(directory)
        return self.documents
    
    def ingest_file(self, file_path: str) -> dict:
        """Load a single file"""
        doc = self.loader.load_file(file_path)
        if doc:
            self.documents.append(doc)
        return doc
    
    def get_documents(self) -> List[dict]:
        """Get loaded documents"""
        return self.documents
    
    def clear(self):
        """Clear loaded documents"""
        self.documents = []
