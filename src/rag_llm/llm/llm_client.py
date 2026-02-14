"""
LLM client for generating responses using various language models
"""

import os
from typing import Optional, Dict, Any


class LLMClient:
    """
    Client for interacting with Language Models (OpenAI, Anthropic, local models, etc.)
    """
    
    def __init__(
        self,
        model_name: str = "gpt-3.5-turbo",
        provider: str = "openai",
        api_key: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ):
        """
        Initialize LLM client
        
        Args:
            model_name: Name of the model to use
            provider: LLM provider (openai, anthropic, huggingface, local)
            api_key: API key for the provider
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
        """
        self.model_name = model_name
        self.provider = provider
        self.api_key = api_key or os.getenv(f"{provider.upper()}_API_KEY")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = None
        
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the LLM client based on provider"""
        if self.provider == "openai":
            self._initialize_openai()
        elif self.provider == "anthropic":
            self._initialize_anthropic()
        elif self.provider == "huggingface":
            self._initialize_huggingface()
        else:
            print(f"Provider {self.provider} not yet implemented")
    
    def _initialize_openai(self):
        """Initialize OpenAI client"""
        try:
            import openai
            openai.api_key = self.api_key
            self.client = openai
            print(f"Initialized OpenAI client with model: {self.model_name}")
        except ImportError:
            print("OpenAI not installed. Install with: pip install openai")
    
    def _initialize_anthropic(self):
        """Initialize Anthropic client"""
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
            print(f"Initialized Anthropic client with model: {self.model_name}")
        except ImportError:
            print("Anthropic not installed. Install with: pip install anthropic")
    
    def _initialize_huggingface(self):
        """Initialize HuggingFace client"""
        try:
            from transformers import pipeline
            self.client = pipeline("text-generation", model=self.model_name)
            print(f"Initialized HuggingFace client with model: {self.model_name}")
        except ImportError:
            print("Transformers not installed. Install with: pip install transformers")
    
    def generate(
        self,
        prompt: str,
        context: Optional[str] = None,
        system_message: Optional[str] = None
    ) -> str:
        """
        Generate a response from the LLM
        
        Args:
            prompt: User prompt/question
            context: Retrieved context from documents
            system_message: System message for the LLM
            
        Returns:
            Generated response
        """
        if self.client is None:
            return "LLM client not initialized. Please check your API key and provider settings."
        
        # Build the full prompt
        full_prompt = self._build_prompt(prompt, context, system_message)
        
        # Generate response based on provider
        if self.provider == "openai":
            return self._generate_openai(full_prompt, system_message)
        elif self.provider == "anthropic":
            return self._generate_anthropic(full_prompt, system_message)
        elif self.provider == "huggingface":
            return self._generate_huggingface(full_prompt)
        else:
            return "Provider not supported"
    
    def _build_prompt(
        self,
        prompt: str,
        context: Optional[str] = None,
        system_message: Optional[str] = None
    ) -> str:
        """Build the complete prompt with context"""
        parts = []
        
        if context:
            parts.append("Context from knowledge base:")
            parts.append(context)
            parts.append("")
        
        parts.append("Question:")
        parts.append(prompt)
        
        return "\n".join(parts)
    
    def _generate_openai(self, prompt: str, system_message: Optional[str] = None) -> str:
        """Generate response using OpenAI"""
        try:
            messages = []
            
            if system_message:
                messages.append({"role": "system", "content": system_message})
            else:
                messages.append({
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions based on the provided context."
                })
            
            messages.append({"role": "user", "content": prompt})
            
            response = self.client.ChatCompletion.create(
                model=self.model_name,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def _generate_anthropic(self, prompt: str, system_message: Optional[str] = None) -> str:
        """Generate response using Anthropic"""
        try:
            system = system_message or "You are a helpful assistant that answers questions based on the provided context."
            
            message = self.client.messages.create(
                model=self.model_name,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=system,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def _generate_huggingface(self, prompt: str) -> str:
        """Generate response using HuggingFace"""
        try:
            response = self.client(
                prompt,
                max_length=self.max_tokens,
                temperature=self.temperature,
                do_sample=True
            )
            return response[0]['generated_text']
        except Exception as e:
            return f"Error generating response: {str(e)}"
