"""
Configuration utilities
"""

import json
import os
from typing import Dict, Any
from pathlib import Path


def load_config(config_file: str) -> Dict[str, Any]:
    """
    Load configuration from file
    
    Args:
        config_file: Path to config file (JSON or Python)
    
    Returns:
        Configuration dictionary
    """
    config_file = Path(config_file)
    
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_file}")
    
    if config_file.suffix == '.json':
        with open(config_file, 'r') as f:
            return json.load(f)
    
    raise ValueError(f"Unsupported config format: {config_file.suffix}")


def load_env_config() -> Dict[str, Any]:
    """Load configuration from environment variables"""
    return {
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'vector_db_path': os.getenv('VECTOR_DB_PATH', './vectors'),
        'data_path': os.getenv('DATA_PATH', './data'),
        'embedding_model': os.getenv('EMBEDDING_MODEL', 'sentence-transformers/all-MiniLM-L6-v2'),
        'llm_model': os.getenv('LLM_MODEL', 'gpt-3.5-turbo'),
    }
