# RAG LLM Private Knowledge Worker

A comprehensive Retrieval-Augmented Generation (RAG) system for building intelligent private knowledge workers powered by Large Language Models.

## Features

- **Document Ingestion**: Load and process multiple document formats (TXT, PDF, DOCX)
- **Smart Chunking**: Recursive text splitting with overlap support
- **Embeddings**: Generate embeddings using HuggingFace sentence transformers
- **Vector Store**: In-memory vector storage with semantic search capabilities
- **Retrieval**: Retrieve relevant documents based on semantic similarity
- **LLM Integration**: Seamless integration with OpenAI and other LLM providers
- **GitHub Documentation Generator**: Automatically generate comprehensive documentation for GitHub repositories
- **Modular Architecture**: Easily swap components for customization

## Project Structure

```
rag-knowledge-worker/
├── src/                           # Source code
│   ├── data_ingestion/           # Document loading and processing
│   ├── chunking/                 # Text splitting strategies
│   ├── embeddings/               # Embedding generation
│   ├── vector_store/             # Vector database management
│   ├── retrieval/                # Retrieval mechanisms
│   ├── llm/                      # LLM integrations
│   ├── github_docs/              # GitHub documentation generator
│   ├── utils/                    # Utility functions
│   └── rag_system.py             # Main RAG orchestrator
├── config/                        # Configuration files
├── data/                          # Data storage
│   ├── raw/                      # Raw documents
│   └── processed/                # Processed documents
├── vectors/                       # Vector database storage
├── tests/                         # Unit tests
├── examples/                      # Example scripts
├── docs/                          # Documentation
├── logs/                          # Application logs
├── main.py                        # Entry point
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
└── README.md                      # This file
```

## Quick Start

### Installation

1. **Clone or setup the project**
   ```bash
   cd LLM-RAG-private-knowldge-worker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and settings
   ```

### Basic Usage

```python
from src.rag_system import RAGSystem

# Initialize RAG system
rag = RAGSystem(config_path='./config/config.json')

# Ingest documents from directory
rag.ingest_documents('./data/raw')

# Build vector index
rag.build_index()

# Query the system
results = rag.query("Your question here", top_k=5)
print(results['response'])
```

### GitHub Documentation Generator

Generate comprehensive documentation for your GitHub repositories:

```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the documentation generator
python src/github_docs/github_docs_generator.py
```

Required environment variables in `.env`:
- `GITHUB_USERNAME`: Your GitHub username
- `GITHUB_TOKEN`: GitHub personal access token (optional, for higher API rate limits)
- `OPENAI_API_KEY`: OpenAI API key for documentation generation

The generator will:
1. Fetch all repositories for the specified GitHub username
2. Analyze repository structure, files, and configurations
3. Generate comprehensive markdown documentation using AI
4. Save output to `data/raw/repo_summaries/`

Features:
- Automatic repository discovery and processing
- Intelligent file selection (README, configs, source code)
- AI-powered documentation generation
- Progress tracking with detailed status updates
- Configurable processing limits and model selection

For detailed documentation, see [docs/GITHUB_DOCS_GENERATOR.md](docs/GITHUB_DOCS_GENERATOR.md)

## Components

### 1. Data Ingestion (src/data_ingestion/)
Handles loading documents from various formats.

- `DocumentLoader`: Load files (TXT, PDF, DOCX, etc.)
- `DataIngestionPipeline`: Orchestrate document processing

### 2. Text Chunking (src/chunking/)
Split documents into optimized chunks for embedding.

- `TextSplitter`: Fixed-size splitting
- `RecursiveCharacterSplitter`: Smart splitting on boundaries

### 3. Embeddings (src/embeddings/)
Generate vector embeddings for text.

- `HuggingFaceEmbedder`: Using sentence-transformers
- `DummyEmbedder`: For testing

### 4. Vector Store (src/vector_store/)
Store and retrieve embeddings efficiently.

- `InMemoryVectorStore`: Fast in-memory storage
- Support for Faiss, Pinecone, Weaviate (extensible)

### 5. Retrieval (src/retrieval/)
Retrieve relevant documents based on queries.

- `VectorRetriever`: Semantic similarity-based retrieval

### 6. LLM Integration (src/llm/)
Connect to language models for response generation.

- `OpenAILLM`: GPT-3.5, GPT-4 support
- `DummyLLM`: For testing

### 7. GitHub Documentation Generator (src/github_docs/)
Generate comprehensive documentation for GitHub repositories.

- **github_docs_generator.py**: Main script for automated documentation generation
- Fetches repository structure and content via GitHub API
- Uses OpenAI API to generate structured markdown documentation
- Processes repositories with intelligent file selection
- Outputs detailed documentation to `data/raw/repo_summaries/`

## Configuration

### config/config.json
Main configuration file:

```json
{
  "embedding": {
    "model": "sentence-transformers/all-MiniLM-L6-v2",
    "dimension": 384
  },
  "chunking": {
    "chunk_size": 1000,
    "overlap": 100
  },
  "llm": {
    "provider": "openai",
    "model": "gpt-3.5-turbo"
  },
  "github_docs": {
    "model": "gpt-4.1-nano",
    "max_tree_items": 800,
    "max_file_chars": 12000,
    "max_source_files": 12,
    "output_dir": "./data/raw/repo_summaries"
  }
}
```

### .env File
Set environment variables:

```env
# OpenAI API Key (required for RAG and GitHub docs)
OPENAI_API_KEY=your_key_here

# GitHub Configuration (for documentation generator)
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_personal_access_token

# Data paths
VECTOR_DB_PATH=./vectors
DATA_PATH=./data
```

## Examples

See [examples/](examples/) directory for detailed examples:

- **basic_usage.py**: Simple RAG workflow
- **custom_pipeline.py**: Custom components
- **advanced_features.py**: Advanced configurations

Run examples:
```bash
python examples/basic_usage.py
python examples/custom_pipeline.py
python examples/advanced_features.py
```

## Testing

Run tests with pytest:

```bash
pytest tests/
pytest tests/ -v --cov=src
```

## Development

### Code Style
- Use Black for formatting: `black src/`
- Use Flake8 for linting: `flake8 src/`
- Use mypy for type checking: `mypy src/`

### Adding New Components

1. Create new module in `src/`
2. Implement base class and concrete implementations
3. Add tests in `tests/`
4. Update documentation

## Integration with Vector Databases

The system is extensible for different vector databases:

```python
# Faiss (local)
from faiss_adapter import FaissVectorStore
vector_store = VectorStore(store=FaissVectorStore())

# Pinecone (cloud)
from pinecone_adapter import PineconeVectorStore
vector_store = VectorStore(store=PineconeVectorStore())

# Weaviate
from weaviate_adapter import WeaviateVectorStore
vector_store = VectorStore(store=WeaviateVectorStore())
```

## Performance Optimization

1. **Batch Processing**: Embed multiple documents at once
2. **Chunk Optimization**: Adjust chunk_size based on your data
3. **Model Selection**: Choose embedders based on accuracy vs speed tradeoff
4. **Caching**: Cache embeddings and retrieval results

## Troubleshooting

### Out of Memory Issues
- Reduce `embedding_batch_size` in config.json
- Use smaller embedding model
- Process documents in batches

### Low Retrieval Quality
- Increase `chunk_size` for better context
- Fine-tune `overlap` parameter
- Use higher-quality embedding model

### Slow Retrieval
- Implement approximate nearest neighbor search (ANN)
- Use Faiss or specialized vector databases
- Optimize chunking strategy

## API Reference

See [docs/API_REFERENCE.md](docs/API_REFERENCE.md) for detailed API documentation.

## Contributing

1. Create feature branch
2. Make changes and add tests
3. Run test suite: `pytest`
4. Format code: `black src/`
5. Submit pull request

## License

MIT License - See [LICENSE](LICENSE) file

## Author

PRATHAMESH SUHAS URAVANE

## Support

For issues and questions:
- Open an issue on GitHub
- Check documentation in `docs/`
- Review examples in `examples/`

## Roadmap

- [ ] GPU support for embeddings
- [ ] Advanced vector databases integration
- [ ] Fine-tuning support
- [ ] Multi-language support
- [ ] Web interface
- [ ] REST API
- [ ] Docker support

## Citation

If you use this project in your research, please cite:

```bibtex
@software{rag_knowledge_worker,
  author = {Uravane, Prathamesh Suhas},
  title = {RAG LLM Private Knowledge Worker},
  year = {2026},
  url = {https://github.com/yourusername/rag-knowledge-worker}
}
```

---

**Last Updated**: February 2026
