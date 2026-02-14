# LL-RAG Private Knowledge Worker

A modular and extensible **RAG (Retrieval-Augmented Generation)** system for building private knowledge bases with Large Language Models.

## 🌟 Features

- **Modular Architecture**: Clean separation of concerns with dedicated modules for each component
- **Document Loading**: Support for multiple file formats (text, markdown, with easy extension for PDF, DOCX, etc.)
- **Embedding Generation**: Flexible embedding interface (ready for OpenAI, HuggingFace, or custom models)
- **Vector Storage**: In-memory vector store with save/load capabilities (ready for FAISS, Pinecone, Chroma integration)
- **Smart Retrieval**: Semantic search for finding relevant documents
- **LLM Integration**: Pluggable LLM interface (compatible with OpenAI, Anthropic, HuggingFace, local models)
- **Configuration Management**: Flexible configuration via files and environment variables

## 📁 Project Structure

```
LL-RAG-private-knowldge-worker/
├── src/
│   └── rag/
│       ├── core/              # Core RAG components
│       │   ├── document_loader.py   # Document loading and parsing
│       │   ├── embeddings.py        # Embedding generation
│       │   ├── vector_store.py      # Vector storage and search
│       │   ├── retriever.py         # Document retrieval
│       │   ├── llm.py              # LLM interface
│       │   └── rag_pipeline.py     # Complete RAG pipeline
│       └── utils/             # Utility modules
│           ├── config.py           # Configuration management
│           ├── logger.py           # Logging setup
│           └── text_processing.py  # Text utilities
├── data/
│   ├── documents/         # Source documents to index
│   └── vector_store/      # Stored vector embeddings
├── config/
│   └── default_config.json    # Default configuration
├── examples/
│   ├── basic_usage.py         # Basic usage example
│   └── config_example.py      # Configuration example
├── tests/                     # Unit tests (to be added)
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
└── README.md                 # This file
```

## 🚀 Quick Start

### 1. Installation

Clone the repository:
```bash
git clone https://github.com/upratham/LL-RAG-private-knowldge-worker.git
cd LL-RAG-private-knowldge-worker
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Or install in development mode:
```bash
pip install -e .
```

### 2. Configuration

Copy the environment template:
```bash
cp .env.example .env
```

Edit `.env` to add your API keys and configure settings:
```bash
# Example configuration
EMBEDDING_MODEL=default
LLM_MODEL=default
RETRIEVAL_K=5
```

### 3. Add Your Documents

Place your documents in the `data/documents/` directory:
```bash
cp your_document.txt data/documents/
cp your_notes.md data/documents/
```

### 4. Run the Example

```bash
python examples/basic_usage.py
```

## 💡 Usage

### Basic Usage

```python
from src.rag import RAGPipeline

# Initialize the pipeline
rag = RAGPipeline(
    embedding_model="default",
    llm_model="default",
    vector_store_path="data/vector_store/store.json"
)

# Index documents
rag.index_documents("data/documents", is_directory=True)

# Query the system
response = rag.query("What is RAG?", k=5)
print(response['answer'])

# View sources
for source in response['sources']:
    print(f"Score: {source['score']}")
    print(f"Content: {source['content']}")
```

### Using Configuration

```python
from src.rag.utils.config import Config
from src.rag import RAGPipeline

# Load configuration
config = Config("config/default_config.json")

# Create pipeline with config
rag = RAGPipeline(
    embedding_model=config.get('embedding.model'),
    llm_model=config.get('llm.model'),
    vector_store_path=config.get('paths.vector_store')
)
```

## 🔧 Customization

### Adding New Document Loaders

Extend the `BaseDocumentLoader` class in `src/rag/core/document_loader.py`:

```python
class PDFDocumentLoader(BaseDocumentLoader):
    def load(self, file_path: str) -> List[Document]:
        # Implement PDF loading
        pass
```

### Integrating Production Embeddings

Replace the placeholder in `src/rag/core/embeddings.py`:

```python
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator(BaseEmbedding):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def embed_text(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()
```

### Using Production Vector Stores

Replace the in-memory store with FAISS, Chroma, or Pinecone:

```python
import chromadb

class ChromaVectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("documents")
```

### Integrating Real LLMs

Update `src/rag/core/llm.py` with your preferred LLM:

```python
from openai import OpenAI

class LLMInterface(BaseLLM):
    def __init__(self, model_name: str = "gpt-4"):
        self.client = OpenAI()
        self.model_name = model_name
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
```

## 🧪 Testing

Run tests (when implemented):
```bash
pytest tests/
```

## 📝 Component Overview

### Core Components

1. **DocumentLoader** (`document_loader.py`): Loads and processes documents from various sources
2. **EmbeddingGenerator** (`embeddings.py`): Generates vector embeddings for text
3. **VectorStore** (`vector_store.py`): Stores and searches document embeddings
4. **Retriever** (`retriever.py`): Retrieves relevant documents for queries
5. **LLMInterface** (`llm.py`): Interfaces with language models
6. **RAGPipeline** (`rag_pipeline.py`): Orchestrates the complete RAG workflow

### Utilities

- **Config** (`config.py`): Manages configuration from files and environment
- **Logger** (`logger.py`): Sets up logging for the application
- **Text Processing** (`text_processing.py`): Text chunking and cleaning utilities

## 🛣️ Roadmap

- [ ] Add support for PDF documents
- [ ] Add support for Word documents (.docx)
- [ ] Integrate with production embedding models (OpenAI, HuggingFace)
- [ ] Add FAISS/Chroma vector store backends
- [ ] Implement LLM integrations (OpenAI, Anthropic, local models)
- [ ] Add comprehensive test suite
- [ ] Add CLI interface
- [ ] Add web API (FastAPI)
- [ ] Add document chunking strategies
- [ ] Implement query refinement
- [ ] Add conversation history support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern RAG architecture principles
- Inspired by LangChain, LlamaIndex, and similar frameworks
- Designed for privacy and customization
