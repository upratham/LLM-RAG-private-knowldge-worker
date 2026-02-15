"""
RAG System - Main orchestrator for Retrieval-Augmented Generation
"""

from typing import List, Dict, Tuple
from src.data_ingestion import DataIngestionPipeline
from src.chunking import RecursiveCharacterSplitter
from src.embeddings import EmbeddingGenerator, HuggingFaceEmbedder
from src.vector_store import VectorStore, InMemoryVectorStore
from src.retrieval import Retriever, VectorRetriever
from src.llm import LLMProvider, DummyLLM
from src.utils import get_logger
import json


class RAGSystem:
    """Main RAG system orchestrator"""
    
    def __init__(self, config_path: str = None):
        """
        Initialize RAG system
        
        Args:
            config_path: Path to configuration JSON file
        """
        self.logger = get_logger(__name__)
        self.config = self._load_config(config_path)
        
        # Initialize components
        self.data_pipeline = DataIngestionPipeline()
        self.text_splitter = RecursiveCharacterSplitter(
            chunk_size=self.config.get('chunking', {}).get('chunk_size', 1000),
            overlap=self.config.get('chunking', {}).get('overlap', 100)
        )
        self.embedder = EmbeddingGenerator()
        self.vector_store = VectorStore()
        self.retriever = Retriever()
        self.llm_provider = LLMProvider()
        
        self.logger.info("RAG System initialized")
    
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration"""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        return {}
    
    def ingest_documents(self, data_path: str) -> int:
        """
        Ingest documents from directory
        
        Args:
            data_path: Path to directory containing documents
        
        Returns:
            Number of documents ingested
        """
        self.logger.info(f"Ingesting documents from {data_path}")
        documents = self.data_pipeline.ingest_from_directory(data_path)
        self.logger.info(f"Ingested {len(documents)} documents")
        return len(documents)
    
    def build_index(self) -> int:
        """
        Build vector index from ingested documents
        
        Returns:
            Number of chunks indexed
        """
        documents = self.data_pipeline.get_documents()
        total_chunks = 0
        
        for doc in documents:
            self.logger.info(f"Processing {doc['file_name']}")
            
            # Split document into chunks
            for content in doc['content']:
                chunks = self.text_splitter.split(content)
                
                # Generate embeddings
                embeddings = self.embedder.embed_texts(chunks)
                
                # Add to vector store
                metadata = [{'source': doc['file_name']} for _ in chunks]
                self.vector_store.add(chunks, embeddings, metadata)
                
                total_chunks += len(chunks)
        
        self.logger.info(f"Built index with {total_chunks} chunks")
        return total_chunks
    
    def query(self, query: str, top_k: int = 5) -> Dict:
        """
        Query the RAG system
        
        Args:
            query: User query
            top_k: Number of results to return
        
        Returns:
            Dictionary with results and context
        """
        self.logger.info(f"Processing query: {query}")
        
        # Retrieve relevant documents
        retrieved_docs = self.vector_store.search(
            self.embedder.embed_text(query),
            k=top_k
        )
        
        # Prepare context
        context = "\n\n".join([doc[0] for doc in retrieved_docs])
        
        # Generate response
        prompt = f"""Based on the following context, answer the query.

Context:
{context}

Query: {query}

Answer:"""
        
        response = self.llm_provider.generate(prompt)
        
        return {
            'query': query,
            'response': response,
            'sources': [doc[0][:100] for doc in retrieved_docs],
            'scores': [doc[1] for doc in retrieved_docs]
        }
    
    def save_index(self, path: str):
        """Save vector index to disk"""
        if hasattr(self.vector_store.store, 'save'):
            self.vector_store.store.save(path)
            self.logger.info(f"Index saved to {path}")
    
    def load_index(self, path: str):
        """Load vector index from disk"""
        if hasattr(self.vector_store.store, 'load'):
            self.vector_store.store.load(path)
            self.logger.info(f"Index loaded from {path}")


from pathlib import Path
