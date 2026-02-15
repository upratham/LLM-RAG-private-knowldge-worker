"""
Text Splitter - Split documents into chunks for embedding
"""

from typing import List
from abc import ABC, abstractmethod


class BaseSplitter(ABC):
    """Base class for text splitters"""
    
    @abstractmethod
    def split(self, text: str) -> List[str]:
        """Split text into chunks"""
        pass


class TextSplitter(BaseSplitter):
    """Simple fixed-size text splitter"""
    
    def __init__(self, chunk_size: int = 1000, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def split(self, text: str) -> List[str]:
        """Split text into chunks of fixed size"""
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.overlap):
            chunk = text[i:i + self.chunk_size]
            if chunk.strip():
                chunks.append(chunk)
        return chunks


class RecursiveCharacterSplitter(BaseSplitter):
    """Recursive character splitter - splits on meaningful boundaries"""
    
    def __init__(self, chunk_size: int = 1000, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.separators = ["\n\n", "\n", ". ", " ", ""]
    
    def split(self, text: str) -> List[str]:
        """Recursively split text on meaningful boundaries"""
        chunks = []
        good_splits = []
        
        for separator in self.separators:
            if separator == "":
                splits = list(text)
            else:
                splits = text.split(separator)
            
            good_splits = []
            for s in splits:
                if len(s) < self.chunk_size:
                    good_splits.append(s)
                else:
                    if good_splits:
                        merged = self._merge_splits(good_splits, separator)
                        chunks.extend(merged)
                        good_splits = []
                    if len(s) > self.chunk_size:
                        # Recursively split this part
                        chunks.extend(self.split(s))
                    else:
                        chunks.append(s)
            break
        
        if good_splits:
            merged = self._merge_splits(good_splits, separator)
            chunks.extend(merged)
        
        return [c.strip() for c in chunks if c.strip()]
    
    def _merge_splits(self, splits: List[str], separator: str) -> List[str]:
        """Merge splits with overlap"""
        merged_text = separator.join(splits)
        good_splits = [merged_text[max(0, i - self.overlap):i + self.chunk_size] 
                      for i in range(0, len(merged_text), self.chunk_size - self.overlap)]
        return good_splits
