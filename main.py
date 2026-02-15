"""
Main entry point for RAG system
"""

import sys
from pathlib import Path
from src.rag_system import RAGSystem
from src.utils import get_logger


def main():
    """Main entry point"""
    logger = get_logger(__name__, log_file='./logs/rag_system.log')
    
    try:
        # Initialize RAG system
        config_path = './config/config.json'
        rag = RAGSystem(config_path=config_path)
        
        # Example: Ingest documents
        data_path = './data/raw'
        if Path(data_path).exists():
            rag.ingest_documents(data_path)
            rag.build_index()
            
            # Example query
            results = rag.query("What is the main topic?", top_k=3)
            print(f"Query: {results['query']}")
            print(f"Response: {results['response']}")
        else:
            logger.warning(f"Data path not found: {data_path}")
    
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
