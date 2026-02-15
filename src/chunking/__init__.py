"""
Text Chunking Module - Split documents into chunks for embedding
"""

from .text_splitter import TextSplitter, RecursiveCharacterSplitter

__all__ = [
    "TextSplitter",
    "RecursiveCharacterSplitter",
]
