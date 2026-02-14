# RAG LLM - Private Knowledge Worker

A comprehensive Retrieval-Augmented Generation (RAG) system for building private knowledge workers with Large Language Models. This project provides a complete pipeline for ingesting documents, creating embeddings, storing them in a vector database, and querying them using LLMs.

## 🚀 Features

- **Document Ingestion**: Support for multiple file formats (PDF, DOCX, TXT, MD, HTML)
- **Smart Text Splitting**: Intelligent chunking with configurable overlap
- **Embeddings**: Integration with sentence-transformers and other embedding models
- **Vector Store**: Efficient storage and retrieval using FAISS or numpy-based search
- **Multiple LLM Support**: OpenAI, Anthropic, HuggingFace, and local models
- **Complete RAG Pipeline**: End-to-end query processing with context retrieval
- **CLI Interface**: Easy-to-use command-line tools
- **Extensible Architecture**: Modular design for easy customization

## 📁 Project Structure

```
LL-RAG-private-knowldge-worker/
├── src/
│   ├── rag_llm/
│   │   ├── __init__.py
│   │   ├── ingestion/          # Document loading and splitting
│   │   │   ├── __init__.py
│   │   │   ├── document_loader.py
│   │   │   └── text_splitter.py
│   │   ├── embeddings/         # Embedding generation and vector storage
│   │   │   ├── __init__.py
│   │   │   ├── embedding_model.py
│   │   │   └── vector_store.py
│   │   ├── retrieval/          # Document retrieval
│   │   │   ├── __init__.py
│   │   │   └── retriever.py
│   │   ├── llm/                # LLM integration
│   │   │   ├── __init__.py
│   │   │   └── llm_client.py
│   │   ├── query_processor/    # Query orchestration
│   │   │   ├── __init__.py
│   │   │   └── query_processor.py
│   │   └── utils/              # Utilities
│   │       ├── __init__.py
│   │       ├── logger.py
│   │       └── helpers.py
│   └── main.py                 # Main CLI entry point
├── tests/
│   ├── unit/                   # Unit tests
│   │   ├── test_ingestion.py
│   │   └── test_embeddings.py
│   └── integration/            # Integration tests
│       └── test_rag_pipeline.py
├── data/
│   ├── documents/              # Place your documents here
│   └── vector_store/           # Vector database storage
├── config/
│   └── config.yaml             # Configuration file
├── examples/                   # Example scripts
│   ├── basic_usage.py
│   ├── build_kb.py
│   └── query_kb.py
├── docs/                       # Documentation
├── notebooks/                  # Jupyter notebooks
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/upratham/LL-RAG-private-knowldge-worker.git
   cd LL-RAG-private-knowldge-worker
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## 📖 Quick Start

### 1. Build Knowledge Base

Place your documents in the `data/documents/` directory, then:

```bash
# Using the CLI
python src/main.py build data/documents

# Or using the example script
python examples/build_kb.py
```

### 2. Query the Knowledge Base

```bash
# Using the CLI
python src/main.py query "What is RAG?"

# Or using the example script
python examples/query_kb.py "What is RAG?"
```

## 💡 Usage Examples

### Python API

```python
from rag_llm.ingestion import DocumentLoader, TextSplitter
from rag_llm.embeddings import EmbeddingModel, VectorStore
from rag_llm.retrieval import Retriever
from rag_llm.llm import LLMClient
from rag_llm.query_processor import QueryProcessor

# Load and process documents
loader = DocumentLoader("data/documents")
documents = loader.load()

splitter = TextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# Create embeddings
embedding_model = EmbeddingModel()
embeddings = embedding_model.embed_texts([c['content'] for c in chunks])

# Build vector store
vector_store = VectorStore()
vector_store.add_documents(chunks, embeddings)
vector_store.save()

# Query the system
retriever = Retriever(vector_store, embedding_model)
llm_client = LLMClient(model_name="gpt-3.5-turbo", provider="openai")
processor = QueryProcessor(retriever, llm_client)

result = processor.process_query("What is this about?")
print(result['answer'])
```

### CLI Commands

```bash
# Build knowledge base with custom settings
python src/main.py build data/documents \
  --vector-store data/my_vector_store \
  --embedding-model sentence-transformers/all-MiniLM-L6-v2

# Query with custom settings
python src/main.py query "Your question here" \
  --llm-model gpt-4 \
  --llm-provider openai \
  --k 10
```

## ⚙️ Configuration

Edit `config/config.yaml` to customize:

- Embedding model and dimensions
- Vector store settings
- Document processing parameters
- LLM provider and model
- Retrieval settings
- System messages

## 🧪 Testing

Run tests to ensure everything is working:

```bash
# Run all tests
python -m pytest tests/

# Run unit tests only
python -m pytest tests/unit/

# Run integration tests
python -m pytest tests/integration/
```

## 📚 Supported File Formats

- Plain Text (`.txt`)
- Markdown (`.md`)
- PDF (`.pdf`) - requires PyPDF2
- Word Documents (`.docx`) - requires python-docx
- HTML (`.html`) - requires beautifulsoup4

## 🔌 LLM Providers

- **OpenAI**: GPT-3.5, GPT-4, and other OpenAI models
- **Anthropic**: Claude models
- **HuggingFace**: Open-source models from HuggingFace Hub
- **Local Models**: Support for locally hosted models

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Sentence Transformers for embedding models
- FAISS for efficient similarity search
- LangChain for inspiration on RAG architecture
- OpenAI and Anthropic for LLM APIs

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

## 🗺️ Roadmap

- [ ] Web interface with Streamlit/FastAPI
- [ ] Support for more document formats
- [ ] Advanced retrieval strategies (hybrid search, reranking)
- [ ] Conversation memory and context management
- [ ] Multi-modal support (images, tables)
- [ ] Batch processing for large document sets
- [ ] Docker containerization
- [ ] Cloud deployment guides
