"""
Query processor that orchestrates the RAG pipeline
"""

from typing import Dict, Any, Optional
from ..retrieval import Retriever
from ..llm import LLMClient


class QueryProcessor:
    """
    Process queries through the complete RAG pipeline:
    1. Retrieve relevant documents
    2. Generate response using LLM with context
    """
    
    def __init__(
        self,
        retriever: Retriever,
        llm_client: LLMClient,
        k: int = 5,
        system_message: Optional[str] = None
    ):
        """
        Initialize query processor
        
        Args:
            retriever: Document retriever
            llm_client: LLM client for generation
            k: Number of documents to retrieve
            system_message: Optional system message for LLM
        """
        self.retriever = retriever
        self.llm_client = llm_client
        self.k = k
        self.system_message = system_message or (
            "You are a helpful AI assistant. Use the provided context to answer the user's question. "
            "If the context doesn't contain relevant information, say so clearly. "
            "Always cite which document you're referring to when answering."
        )
    
    def process_query(self, query: str, return_sources: bool = True) -> Dict[str, Any]:
        """
        Process a query through the RAG pipeline
        
        Args:
            query: User query
            return_sources: Whether to include source documents in response
            
        Returns:
            Dictionary containing answer and optionally source documents
        """
        # Step 1: Retrieve relevant documents
        retrieved_docs = self.retriever.retrieve(query, k=self.k)
        
        # Step 2: Format context for LLM
        context = self.retriever.retrieve_with_context(query, k=self.k)
        
        # Step 3: Generate response with LLM
        response = self.llm_client.generate(
            prompt=query,
            context=context,
            system_message=self.system_message
        )
        
        # Prepare result
        result = {
            'query': query,
            'answer': response,
        }
        
        if return_sources:
            result['sources'] = [
                {
                    'content': doc['content'][:200] + "..." if len(doc['content']) > 200 else doc['content'],
                    'metadata': doc['metadata'],
                    'score': doc['score']
                }
                for doc in retrieved_docs
            ]
        
        return result
    
    def process_query_stream(self, query: str):
        """
        Process query with streaming response (if supported by LLM)
        
        Args:
            query: User query
            
        Yields:
            Response chunks
        """
        # For now, return the full response
        # Streaming can be implemented based on LLM provider support
        result = self.process_query(query, return_sources=False)
        yield result['answer']
