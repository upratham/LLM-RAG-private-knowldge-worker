"""
Text splitter for chunking documents into smaller pieces
"""

from typing import List, Dict, Any


class TextSplitter:
    """
    Split text into chunks for embedding and retrieval
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize text splitter
        
        Args:
            chunk_size: Maximum size of each chunk in characters
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def split_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Split documents into chunks
        
        Args:
            documents: List of document dictionaries
            
        Returns:
            List of chunk dictionaries with content and metadata
        """
        chunks = []
        
        for doc in documents:
            doc_chunks = self.split_text(doc['content'])
            
            for i, chunk_text in enumerate(doc_chunks):
                chunk = {
                    'content': chunk_text,
                    'metadata': {
                        **doc['metadata'],
                        'chunk_id': i,
                        'total_chunks': len(doc_chunks)
                    }
                }
                chunks.append(chunk)
        
        return chunks
    
    def split_text(self, text: str) -> List[str]:
        """
        Split text into chunks
        
        Args:
            text: Input text to split
            
        Returns:
            List of text chunks
        """
        if len(text) <= self.chunk_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + self.chunk_size
            
            # Try to split at sentence boundary
            if end < len(text):
                # Look for sentence endings
                for delimiter in ['. ', '.\n', '! ', '!\n', '? ', '?\n']:
                    last_delimiter = text.rfind(delimiter, start, end)
                    if last_delimiter != -1:
                        end = last_delimiter + len(delimiter)
                        break
            
            chunks.append(text[start:end].strip())
            start = end - self.chunk_overlap
            
            # Avoid infinite loop
            if start >= len(text):
                break
        
        return chunks
