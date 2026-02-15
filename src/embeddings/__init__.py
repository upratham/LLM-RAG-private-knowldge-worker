"""
Embeddings Module - Generate embeddings for text chunks
"""

from .embedder import EmbeddingGenerator, HuggingFaceEmbedder

__all__ = [
    "EmbeddingGenerator",
    "HuggingFaceEmbedder",
]
