"""Configuration management."""

import os
from pathlib import Path
from typing import Any, Dict
import json


class Config:
    """Configuration class for RAG system."""
    
    def __init__(self, config_file: str = None):
        """
        Initialize configuration.
        
        Args:
            config_file: Path to configuration file (JSON)
        """
        self.config: Dict[str, Any] = self._load_defaults()
        
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        
        # Override with environment variables
        self._load_from_env()
    
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default configuration."""
        return {
            'embedding': {
                'model': 'default',
                'dimension': 768,
            },
            'llm': {
                'model': 'default',
                'max_tokens': 500,
                'temperature': 0.7,
            },
            'retrieval': {
                'k': 5,
                'similarity_threshold': 0.7,
            },
            'paths': {
                'documents': 'data/documents',
                'vector_store': 'data/vector_store/store.json',
            },
            'logging': {
                'level': 'INFO',
                'file': None,
            }
        }
    
    def _load_from_env(self):
        """Load configuration from environment variables."""
        # Embedding configuration
        if 'EMBEDDING_MODEL' in os.environ:
            self.config['embedding']['model'] = os.environ['EMBEDDING_MODEL']
        
        # LLM configuration
        if 'LLM_MODEL' in os.environ:
            self.config['llm']['model'] = os.environ['LLM_MODEL']
        
        if 'LLM_MAX_TOKENS' in os.environ:
            self.config['llm']['max_tokens'] = int(os.environ['LLM_MAX_TOKENS'])
        
        if 'LLM_TEMPERATURE' in os.environ:
            self.config['llm']['temperature'] = float(os.environ['LLM_TEMPERATURE'])
        
        # Retrieval configuration
        if 'RETRIEVAL_K' in os.environ:
            self.config['retrieval']['k'] = int(os.environ['RETRIEVAL_K'])
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key (supports nested keys with dots, e.g., 'llm.model')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """
        Set configuration value.
        
        Args:
            key: Configuration key (supports nested keys with dots)
            value: Value to set
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def save(self, config_file: str):
        """
        Save configuration to file.
        
        Args:
            config_file: Path to save configuration
        """
        config_dir = os.path.dirname(config_file)
        if config_dir:
            os.makedirs(config_dir, exist_ok=True)
        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
