"""LLM interface for generating responses."""

from typing import List, Dict, Any
from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """Base class for LLM interfaces."""
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response from the LLM."""
        pass


class LLMInterface(BaseLLM):
    """
    Interface for interacting with Large Language Models.
    
    This is a placeholder implementation. In production, integrate with:
    - OpenAI API
    - HuggingFace models
    - Anthropic Claude
    - Local LLMs (LLaMA, Mistral, etc.)
    """
    
    def __init__(self, model_name: str = "default", **config):
        """
        Initialize the LLM interface.
        
        Args:
            model_name: Name of the LLM to use
            **config: Additional configuration parameters
        """
        self.model_name = model_name
        self.config = config
        # TODO: Initialize actual LLM here
    
    def generate(self, prompt: str, max_tokens: int = 500, 
                 temperature: float = 0.7, **kwargs) -> str:
        """
        Generate a response from the LLM.
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional generation parameters
            
        Returns:
            Generated text response
        """
        # Placeholder implementation
        # In production, replace with actual LLM API call
        return f"[Placeholder response for prompt: {prompt[:50]}...]"
    
    def generate_with_context(self, query: str, context: List[str], 
                             system_prompt: str = None) -> str:
        """
        Generate a response using retrieved context.
        
        Args:
            query: User query
            context: List of relevant document snippets
            system_prompt: Optional system prompt
            
        Returns:
            Generated response
        """
        # Build prompt with context
        context_text = "\n\n".join([f"Document {i+1}:\n{doc}" 
                                    for i, doc in enumerate(context)])
        
        if system_prompt is None:
            system_prompt = (
                "You are a helpful assistant that answers questions based on "
                "the provided context. If the answer is not in the context, "
                "say so clearly."
            )
        
        full_prompt = f"""{system_prompt}

Context:
{context_text}

Question: {query}

Answer:"""
        
        return self.generate(full_prompt)
