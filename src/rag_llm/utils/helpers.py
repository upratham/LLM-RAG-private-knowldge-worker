"""
Helper functions for RAG LLM
"""

import yaml
import json
from typing import List, Dict, Any
from pathlib import Path


def format_documents(documents: List[Dict[str, Any]], max_length: int = 500) -> str:
    """
    Format documents for display
    
    Args:
        documents: List of document dictionaries
        max_length: Maximum length for each document content
        
    Returns:
        Formatted string
    """
    formatted = []
    
    for i, doc in enumerate(documents, 1):
        content = doc.get('content', '')
        if len(content) > max_length:
            content = content[:max_length] + "..."
        
        metadata = doc.get('metadata', {})
        source = metadata.get('source', 'Unknown')
        
        formatted.append(f"Document {i} (Source: {source}):")
        formatted.append(content)
        formatted.append("")
    
    return "\n".join(formatted)


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from YAML or JSON file
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    config_file = Path(config_path)
    
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_file, 'r') as f:
        if config_file.suffix in ['.yaml', '.yml']:
            config = yaml.safe_load(f)
        elif config_file.suffix == '.json':
            config = json.load(f)
        else:
            raise ValueError(f"Unsupported configuration file format: {config_file.suffix}")
    
    return config


def save_config(config: Dict[str, Any], config_path: str):
    """
    Save configuration to YAML or JSON file
    
    Args:
        config: Configuration dictionary
        config_path: Path to save configuration file
    """
    config_file = Path(config_path)
    config_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_file, 'w') as f:
        if config_file.suffix in ['.yaml', '.yml']:
            yaml.dump(config, f, default_flow_style=False)
        elif config_file.suffix == '.json':
            json.dump(config, f, indent=2)
        else:
            raise ValueError(f"Unsupported configuration file format: {config_file.suffix}")


def chunk_text_by_tokens(text: str, max_tokens: int = 512) -> List[str]:
    """
    Split text into chunks by approximate token count
    
    Args:
        text: Input text
        max_tokens: Maximum tokens per chunk
        
    Returns:
        List of text chunks
    """
    # Rough approximation: 1 token ≈ 4 characters
    max_chars = max_tokens * 4
    
    if len(text) <= max_chars:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + max_chars
        
        # Try to break at sentence boundary
        if end < len(text):
            for delimiter in ['. ', '.\n', '! ', '!\n', '? ', '?\n']:
                last_delimiter = text.rfind(delimiter, start, end)
                if last_delimiter != -1:
                    end = last_delimiter + len(delimiter)
                    break
        
        chunks.append(text[start:end].strip())
        start = end
    
    return chunks
