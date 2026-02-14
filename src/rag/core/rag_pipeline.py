"""Complete RAG pipeline integrating all components."""

from typing import List, Dict, Any
from .document_loader import DocumentLoader
from .embeddings import EmbeddingGenerator
from .vector_store import VectorStore
from .retriever import Retriever
from .llm import LLMInterface


class RAGPipeline:
    """
    Complete RAG (Retrieval-Augmented Generation) pipeline.
    
    This class integrates document loading, embedding generation,
    vector storage, retrieval, and LLM generation into a single pipeline.
    """
    
    def __init__(self, 
                 embedding_model: str = "default",
                 llm_model: str = "default",
                 vector_store_path: str = None):
        """
        Initialize the RAG pipeline.
        
        Args:
            embedding_model: Name of the embedding model
            llm_model: Name of the LLM model
            vector_store_path: Path to save/load vector store
        """
        self.document_loader = DocumentLoader()
        self.embedding_generator = EmbeddingGenerator(model_name=embedding_model)
        self.vector_store = VectorStore()
        self.retriever = Retriever(self.vector_store, self.embedding_generator)
        self.llm = LLMInterface(model_name=llm_model)
        self.vector_store_path = vector_store_path
        
        # Load existing vector store if path provided
        if vector_store_path:
            try:
                self.vector_store.load(vector_store_path)
                print(f"Loaded vector store from {vector_store_path}")
            except FileNotFoundError:
                print(f"No existing vector store found at {vector_store_path}")
    
    def index_documents(self, document_path: str, is_directory: bool = False):
        """
        Load and index documents.
        
        Args:
            document_path: Path to document or directory
            is_directory: Whether the path is a directory
        """
        # Load documents
        if is_directory:
            documents = self.document_loader.load_directory(document_path)
        else:
            documents = self.document_loader.load_document(document_path)
        
        if not documents:
            print("No documents loaded")
            return
        
        print(f"Loaded {len(documents)} documents")
        
        # Extract text and metadata
        texts = [doc.content for doc in documents]
        metadata = [doc.metadata for doc in documents]
        
        # Generate embeddings
        print("Generating embeddings...")
        embeddings = self.embedding_generator.embed_texts(texts)
        
        # Add to vector store
        self.vector_store.add(embeddings, texts, metadata)
        print(f"Indexed {len(documents)} documents")
        
        # Save vector store if path provided
        if self.vector_store_path:
            self.vector_store.save(self.vector_store_path)
            print(f"Saved vector store to {self.vector_store_path}")
    
    def query(self, question: str, k: int = 5, 
              include_sources: bool = True) -> Dict[str, Any]:
        """
        Query the RAG system.
        
        Args:
            question: User question
            k: Number of documents to retrieve
            include_sources: Whether to include source documents in response
            
        Returns:
            Dict containing answer and optionally source documents
        """
        # Retrieve relevant documents
        retrieved_docs = self.retriever.retrieve(question, k=k)
        
        if not retrieved_docs:
            return {
                'answer': "I don't have any relevant information to answer that question.",
                'sources': [] if include_sources else None
            }
        
        # Extract context
        context = [doc['content'] for doc in retrieved_docs]
        
        # Generate answer using LLM
        answer = self.llm.generate_with_context(question, context)
        
        # Prepare response
        response = {'answer': answer}
        
        if include_sources:
            response['sources'] = [
                {
                    'content': doc['content'][:200] + '...' if len(doc['content']) > 200 else doc['content'],
                    'score': doc['score'],
                    'metadata': doc['metadata']
                }
                for doc in retrieved_docs
            ]
        
        return response
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the RAG system."""
        return {
            'num_documents': len(self.vector_store),
            'embedding_model': self.embedding_generator.model_name,
            'llm_model': self.llm.model_name,
        }
