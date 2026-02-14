"""
Document loader for various file formats (PDF, TXT, DOCX, etc.)
"""

import os
from pathlib import Path
from typing import List, Dict, Any


class DocumentLoader:
    """
    Load and process documents from various file formats
    """
    
    SUPPORTED_FORMATS = ['.txt', '.pdf', '.docx', '.md', '.html']
    
    def __init__(self, document_path: str):
        """
        Initialize document loader
        
        Args:
            document_path: Path to document or directory
        """
        self.document_path = Path(document_path)
        
    def load(self) -> List[Dict[str, Any]]:
        """
        Load documents from the specified path
        
        Returns:
            List of document dictionaries with content and metadata
        """
        documents = []
        
        if self.document_path.is_file():
            doc = self._load_file(self.document_path)
            if doc:
                documents.append(doc)
        elif self.document_path.is_dir():
            for file_path in self.document_path.rglob('*'):
                if file_path.is_file() and file_path.suffix in self.SUPPORTED_FORMATS:
                    doc = self._load_file(file_path)
                    if doc:
                        documents.append(doc)
        
        return documents
    
    def _load_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Load a single file
        
        Args:
            file_path: Path to the file
            
        Returns:
            Document dictionary with content and metadata
        """
        try:
            if file_path.suffix == '.txt' or file_path.suffix == '.md':
                return self._load_text_file(file_path)
            elif file_path.suffix == '.pdf':
                return self._load_pdf_file(file_path)
            elif file_path.suffix == '.docx':
                return self._load_docx_file(file_path)
            elif file_path.suffix == '.html':
                return self._load_html_file(file_path)
        except Exception as e:
            print(f"Error loading {file_path}: {str(e)}")
            return None
    
    def _load_text_file(self, file_path: Path) -> Dict[str, Any]:
        """Load plain text or markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {
            'content': content,
            'metadata': {
                'source': str(file_path),
                'filename': file_path.name,
                'file_type': file_path.suffix
            }
        }
    
    def _load_pdf_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Load PDF file
        Note: Requires PyPDF2 or similar library
        """
        try:
            import PyPDF2
            
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                content = ""
                for page in pdf_reader.pages:
                    content += page.extract_text() + "\n"
            
            return {
                'content': content,
                'metadata': {
                    'source': str(file_path),
                    'filename': file_path.name,
                    'file_type': '.pdf',
                    'pages': len(pdf_reader.pages)
                }
            }
        except ImportError:
            print("PyPDF2 not installed. Install with: pip install PyPDF2")
            return None
    
    def _load_docx_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Load DOCX file
        Note: Requires python-docx library
        """
        try:
            from docx import Document
            
            doc = Document(file_path)
            content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            
            return {
                'content': content,
                'metadata': {
                    'source': str(file_path),
                    'filename': file_path.name,
                    'file_type': '.docx'
                }
            }
        except ImportError:
            print("python-docx not installed. Install with: pip install python-docx")
            return None
    
    def _load_html_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Load HTML file
        Note: Requires beautifulsoup4 library
        """
        try:
            from bs4 import BeautifulSoup
            
            with open(file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                content = soup.get_text()
            
            return {
                'content': content,
                'metadata': {
                    'source': str(file_path),
                    'filename': file_path.name,
                    'file_type': '.html'
                }
            }
        except ImportError:
            print("beautifulsoup4 not installed. Install with: pip install beautifulsoup4")
            return None
