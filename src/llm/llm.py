"""
LLM Integration - Connect to various Language Models
"""

from abc import ABC, abstractmethod
from typing import List


class BaseLLM(ABC):
    """Base class for LLM providers"""
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text from prompt"""
        pass


class DummyLLM(BaseLLM):
    """Dummy LLM for testing"""
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Return dummy response"""
        return f"Dummy response to: {prompt[:50]}..."


class OpenAILLM(BaseLLM):
    """OpenAI LLM provider"""
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize OpenAI LLM
        
        Args:
            api_key: OpenAI API key
            model: Model name (default: gpt-3.5-turbo)
        """
        self.api_key = api_key
        self.model = model
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize OpenAI client"""
        try:
            import openai
            openai.api_key = self.api_key
            self.client = openai
        except ImportError:
            raise ImportError(
                "openai is required. Install with: pip install openai"
            )
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text using OpenAI"""
        try:
            response = self.client.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=kwargs.get("temperature", 0.7),
                max_tokens=kwargs.get("max_tokens", 500),
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error calling OpenAI: {str(e)}")


class LlamaLLM(BaseLLM):
    """Llama LLM provider via Ollama"""
    
    def __init__(self, model: str = "llama2", base_url: str = "http://localhost:11434"):
        """
        Initialize Llama LLM via Ollama
        
        Args:
            model: Model name (default: llama2, can be llama3.2, etc.)
            base_url: Ollama server URL (default: http://localhost:11434)
        """
        self.model = model
        self.base_url = base_url
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize Ollama client"""
        try:
            from langchain_community.llms import Ollama
            self.client = Ollama(
                model=self.model,
                base_url=self.base_url
            )
        except ImportError:
            raise ImportError(
                "langchain-community is required. Install with: pip install langchain-community"
            )
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text using Llama via Ollama"""
        try:
            response = self.client.invoke(prompt)
            return response
        except Exception as e:
            raise Exception(f"Error calling Llama via Ollama: {str(e)}")


class LLMProvider:
    """Main LLM provider interface"""
    
    def __init__(self, llm: BaseLLM = None):
        """Initialize LLM provider"""
        self.llm = llm or DummyLLM()
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text"""
        return self.llm.generate(prompt, **kwargs)
    
    def set_llm(self, llm: BaseLLM):
        """Change LLM"""
        self.llm = llm
