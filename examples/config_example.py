"""Example showing how to use configuration."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.rag.utils.config import Config
from src.rag import RAGPipeline


def main():
    """Main example function."""
    print("=" * 50)
    print("Configuration Example")
    print("=" * 50)
    
    # Create configuration
    print("\n1. Creating configuration...")
    config = Config()
    
    # Display default configuration
    print("\n2. Default configuration:")
    print(f"   Embedding model: {config.get('embedding.model')}")
    print(f"   LLM model: {config.get('llm.model')}")
    print(f"   Retrieval K: {config.get('retrieval.k')}")
    print(f"   Vector store path: {config.get('paths.vector_store')}")
    
    # Modify configuration
    print("\n3. Modifying configuration...")
    config.set('llm.temperature', 0.8)
    config.set('retrieval.k', 10)
    print(f"   New LLM temperature: {config.get('llm.temperature')}")
    print(f"   New retrieval K: {config.get('retrieval.k')}")
    
    # Save configuration
    config_file = "config/config.json"
    print(f"\n4. Saving configuration to {config_file}...")
    config.save(config_file)
    print("   Configuration saved!")
    
    # Load configuration and create pipeline
    print("\n5. Loading configuration and creating pipeline...")
    loaded_config = Config(config_file)
    rag = RAGPipeline(
        embedding_model=loaded_config.get('embedding.model'),
        llm_model=loaded_config.get('llm.model'),
        vector_store_path=loaded_config.get('paths.vector_store')
    )
    print("   Pipeline created with loaded configuration!")
    
    print("\n" + "=" * 50)
    print("Configuration example completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
