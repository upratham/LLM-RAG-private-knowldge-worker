"""Main entry point for the RAG application."""

import argparse
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.rag import RAGPipeline
from src.rag.utils.config import Config
from src.rag.utils.logger import setup_logging


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='RAG Private Knowledge Worker')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Index command
    index_parser = subparsers.add_parser('index', help='Index documents')
    index_parser.add_argument('path', help='Path to document or directory')
    index_parser.add_argument('--config', default='config/default_config.json',
                             help='Configuration file')
    
    # Query command
    query_parser = subparsers.add_parser('query', help='Query the system')
    query_parser.add_argument('question', help='Question to ask')
    query_parser.add_argument('--config', default='config/default_config.json',
                             help='Configuration file')
    query_parser.add_argument('-k', type=int, default=5,
                             help='Number of documents to retrieve')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show system statistics')
    stats_parser.add_argument('--config', default='config/default_config.json',
                             help='Configuration file')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Load configuration
    config = Config(args.config if hasattr(args, 'config') else None)
    
    # Setup logging
    setup_logging(
        log_level=config.get('logging.level', 'INFO'),
        log_file=config.get('logging.file')
    )
    
    # Initialize pipeline
    rag = RAGPipeline(
        embedding_model=config.get('embedding.model'),
        llm_model=config.get('llm.model'),
        vector_store_path=config.get('paths.vector_store')
    )
    
    # Execute command
    if args.command == 'index':
        path = Path(args.path)
        is_directory = path.is_dir()
        
        print(f"Indexing {'directory' if is_directory else 'file'}: {args.path}")
        rag.index_documents(args.path, is_directory=is_directory)
        print("Indexing complete!")
        
    elif args.command == 'query':
        print(f"Question: {args.question}")
        print("-" * 50)
        
        response = rag.query(args.question, k=args.k, include_sources=True)
        
        print(f"\nAnswer: {response['answer']}")
        print("\nSources:")
        for i, source in enumerate(response.get('sources', []), 1):
            print(f"\n{i}. [Score: {source['score']:.3f}]")
            print(f"   {source['content']}")
            if source['metadata']:
                print(f"   Metadata: {source['metadata']}")
        
    elif args.command == 'stats':
        stats = rag.get_stats()
        print("System Statistics:")
        print("-" * 50)
        for key, value in stats.items():
            print(f"{key}: {value}")


if __name__ == '__main__':
    main()
