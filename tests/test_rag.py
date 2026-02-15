"""
Test suite for RAG system
"""

import pytest
import numpy as np
from src.data_ingestion import DataIngestionPipeline
from src.chunking import TextSplitter, RecursiveCharacterSplitter
from src.embeddings import EmbeddingGenerator, HuggingFaceEmbedder
from src.vector_store import VectorStore, InMemoryVectorStore
from src.retrieval import VectorRetriever
from src.llm import DummyLLM


class TestTextSplitter:
    """Test text splitting"""
    
    def test_simple_splitter(self):
        splitter = TextSplitter(chunk_size=50, overlap=10)
        text = "This is a long text that should be split into multiple chunks."
        chunks = splitter.split(text)
        assert len(chunks) > 1
        assert all(len(c) <= 50 for c in chunks)
    
    def test_recursive_splitter(self):
        splitter = RecursiveCharacterSplitter(chunk_size=50, overlap=10)
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        chunks = splitter.split(text)
        assert len(chunks) >= 1
        assert all(c.strip() for c in chunks)


class TestEmbeddings:
    """Test embedding generation"""
    
    def test_embedding_generator(self):
        embedder = EmbeddingGenerator()
        text = "This is a test text"
        embedding = embedder.embed_text(text)
        assert isinstance(embedding, np.ndarray)
        assert embedding.shape == (384,)
    
    def test_batch_embeddings(self):
        embedder = EmbeddingGenerator()
        texts = ["Text 1", "Text 2", "Text 3"]
        embeddings = embedder.embed_texts(texts)
        assert len(embeddings) == 3
        assert all(isinstance(e, np.ndarray) for e in embeddings)


class TestVectorStore:
    """Test vector store"""
    
    def test_add_and_search(self):
        store = InMemoryVectorStore()
        texts = ["Document 1", "Document 2"]
        embeddings = [np.random.randn(384) for _ in texts]
        
        store.add_vectors(texts, embeddings)
        
        query_embedding = embeddings[0]
        results = store.search(query_embedding, k=2)
        
        assert len(results) == 2
        assert results[0][0] == texts[0]


class TestDataIngestion:
    """Test data ingestion"""
    
    def test_pipeline_initialization(self):
        pipeline = DataIngestionPipeline()
        assert len(pipeline.get_documents()) == 0
    
    def test_clear_documents(self):
        pipeline = DataIngestionPipeline()
        pipeline.clear()
        assert len(pipeline.get_documents()) == 0


class TestLLM:
    """Test LLM"""
    
    def test_dummy_llm(self):
        llm = DummyLLM()
        response = llm.generate("Test prompt")
        assert "Dummy response" in response
