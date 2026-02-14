"""Vector store for storing and retrieving embeddings."""

from typing import List, Tuple, Dict, Any
import json
import os


class VectorStore:
    """
    In-memory vector store for document embeddings.
    
    In production, consider using:
    - FAISS
    - Pinecone
    - Weaviate
    - Chroma
    - Milvus
    """
    
    def __init__(self, dimension: int = 768):
        """
        Initialize the vector store.
        
        Args:
            dimension: Dimension of the embeddings
        """
        self.dimension = dimension
        self.vectors: List[List[float]] = []
        self.documents: List[str] = []
        self.metadata: List[Dict[str, Any]] = []
    
    def add(self, vectors: List[List[float]], documents: List[str], 
            metadata: List[Dict[str, Any]] = None):
        """
        Add vectors and associated documents to the store.
        
        Args:
            vectors: List of embedding vectors
            documents: List of document contents
            metadata: Optional list of metadata dicts
        """
        if len(vectors) != len(documents):
            raise ValueError("Number of vectors must match number of documents")
        
        if metadata is None:
            metadata = [{}] * len(documents)
        
        self.vectors.extend(vectors)
        self.documents.extend(documents)
        self.metadata.extend(metadata)
    
    def search(self, query_vector: List[float], k: int = 5) -> List[Tuple[str, float, Dict[str, Any]]]:
        """
        Search for the k most similar documents.
        
        Args:
            query_vector: Query embedding vector
            k: Number of results to return
            
        Returns:
            List of tuples (document, similarity_score, metadata)
        """
        if not self.vectors:
            return []
        
        # Simple cosine similarity (placeholder)
        # In production, use optimized similarity search
        similarities = []
        for i, vec in enumerate(self.vectors):
            similarity = self._cosine_similarity(query_vector, vec)
            similarities.append((i, similarity))
        
        # Sort by similarity (descending) and take top k
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_k = similarities[:k]
        
        results = []
        for idx, score in top_k:
            results.append((self.documents[idx], score, self.metadata[idx]))
        
        return results
    
    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = sum(a * a for a in vec1) ** 0.5
        norm2 = sum(b * b for b in vec2) ** 0.5
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)
    
    def save(self, file_path: str):
        """Save the vector store to disk."""
        data = {
            'dimension': self.dimension,
            'vectors': self.vectors,
            'documents': self.documents,
            'metadata': self.metadata
        }
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f)
    
    def load(self, file_path: str):
        """Load the vector store from disk."""
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        self.dimension = data['dimension']
        self.vectors = data['vectors']
        self.documents = data['documents']
        self.metadata = data['metadata']
    
    def __len__(self):
        """Return the number of vectors in the store."""
        return len(self.vectors)
