<!-- Generated: 2026-02-15T03:36:00.497898Z | Model: gpt-4.1-nano -->

# LLM-RAG-private-knowldge-worker

## Overview
The **LLM-RAG-private-knowldge-worker** is a retrieval-augmented generation (RAG) system designed to enable building private, intelligent knowledge workers powered by Large Language Models (LLMs). It facilitates document ingestion, semantic search, and question-answering by combining document processing, embedding generation, vector similarity search, and LLM-based response generation. This system is suitable for developers and data scientists aiming to create customized AI assistants that operate on private datasets.

## Key Features
- **Document Ingestion:** Load and process various document formats (TXT, PDF, DOCX) from directories.
- **Smart Chunking:** Recursive text splitting with overlap support for better context management.
- **Embeddings:** Generate semantic vector representations using HuggingFace sentence transformers.
- **Vector Store:** In-memory vector database supporting semantic search for relevant document retrieval.
- **Retrieval:** Semantic similarity-based document retrieval to find relevant context.
- **LLM Integration:** Connect seamlessly with OpenAI and other LLM providers for response generation.
- **Modular Architecture:** Components designed for easy customization and extension.
- **Configurable:** Use JSON config files and environment variables for flexible setup.

## Architecture / How it Works
The system orchestrates several components:
- **Data Ingestion:** Loads raw documents from specified directories.
- **Text Chunking:** Splits documents into manageable chunks with overlap to preserve context.
- **Embedding Generation:** Converts text chunks into vector embeddings.
- **Vector Store:** Stores embeddings and associated metadata for fast similarity search.
- **Retrieval:** Finds relevant document chunks based on query embedding.
- **LLM Response:** Uses retrieved context to generate answers via LLMs.
- **Main Orchestrator (`rag_system.py`):** Coordinates all components for ingestion, indexing, querying, and saving/loading indices.

## Notable Folders/Files
- **`src/`**: Core source code implementing ingestion, chunking, embeddings, retrieval, LLMs, and system orchestration.
- **`config/`**: Configuration files (e.g., `config.json`) for system parameters.
- **`data/`**: Raw and processed documents used for ingestion.
- **`vectors/`**: Persisted vector indices for fast retrieval.
- **`tests/`**: Unit tests for verifying system components.
- **`examples/`**: Sample scripts demonstrating usage and customization.
- **`docs/`**: Documentation including API references and architecture guides.
- **`logs/`**: Log files generated during system operation.

## Setup & Run
### Installation
```bash
# Clone the repository
git clone https://github.com/upratham/LLM-RAG-private-knowldge-worker.git
cd LLM-RAG-private-knowldge-worker

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration
- Copy example environment variables:
```bash
cp .env.example .env
# Edit `.env` to include your API keys and paths
```
- Update `config/config.json` with desired parameters (e.g., embedding model, chunk size).

### Running the System
- To process documents, build index, and query:
```python
from src.rag_system import RAGSystem

# Initialize system
rag = RAGSystem(config_path='./config/config.json')

# Ingest documents from data/raw
rag.ingest_documents('./data/raw')

# Build vector index
rag.build_index()

# Query the system
results = rag.query("Your question here", top_k=5)
print(results['response'])
```

- Or run the main script:
```bash
python main.py
```

## How to Use
### Basic Workflow
```python
from src.rag_system import RAGSystem

rag = RAGSystem(config_path='./config/config.json')
rag.ingest_documents('./data/raw')  # Load documents
rag.build_index()                     # Create vector index
response = rag.query("What is the main topic?", top_k=3)
print(response['response'])
```

### Example Queries
- Ask questions based on ingested documents.
- Retrieve relevant context snippets.
- Generate detailed answers using integrated LLMs.

### Customization
- Replace or extend components like embedder, retriever, or LLM provider.
- Adjust `config/config.json` for different models or parameters.
- Use examples provided in `examples/` for more advanced workflows.

## Testing / CI
- Tests are located in `tests/test_rag.py`.
- Run tests with:
```bash
pytest tests/
```
- Coverage and verbose output:
```bash
pytest tests/ -v --cov=src
```

## Deployment
- The system is designed for local or server deployment.
- Save and load vector indices:
```python
rag.save_index('./vectors/index.json')
rag.load_index('./vectors/index.json')
```
- For production, consider integrating with external vector databases like Faiss, Pinecone, or Weaviate for scalability.

## Contribution Notes
- Create feature branches.
- Implement components or fixes.
- Run tests and adhere to code style (`black`, `flake8`).
- Submit pull requests with clear descriptions.
- Update documentation as needed.

## Limitations / TODOs (Inferred)
- Currently supports in-memory vector store; external vector DB integration is extensible but not implemented by default.
- No explicit support for GPU acceleration; embeddings may be slow on large datasets.
- Limited to English documents; multi-language support is a potential future enhancement.
- No web interface or REST API; CLI or script-based interaction only.
- Fine-tuning of models and advanced customization are not included but can be added.

---

*Note:* Some features and configurations are inferred from the provided files and structure. For detailed API documentation, refer to `docs/API_REFERENCE.md`.
