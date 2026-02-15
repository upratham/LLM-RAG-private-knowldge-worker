# RAG LLM Private Knowledge Worker

A comprehensive Retrieval-Augmented Generation (RAG) system for building intelligent private knowledge workers powered by Large Language Models.

## Features

- **Document Ingestion**: Load and process multiple document formats (TXT, PDF, DOCX, MD)
- **PDF to Markdown Conversion**: Extract text from PDFs with detailed analysis
- **Smart Chunking**: LangChain's RecursiveCharacterTextSplitter with overlap support
- **High-Quality Embeddings**: e5-large-v2 model (1024-dim) via HuggingFace
- **Persistent Vector Store**: Chroma vector database with metadata support
- **Advanced Retrieval**: Semantic search, metadata filtering, MMR (Max Marginal Relevance)
- **Interactive Visualization**: 2D/3D t-SNE visualizations with Plotly
- **LLM Integration**: Seamless integration with OpenAI, Anthropic, and other providers via LangChain
- **GitHub Documentation Generator**: Automatically generate comprehensive documentation for GitHub repositories
- **Modular Architecture**: Built on LangChain for easy customization and extension

## Technology Stack

- **Framework**: LangChain & LangChain Community
- **Embeddings**: HuggingFace Transformers (e5-large-v2)
- **Vector Store**: ChromaDB with persistent storage
- **Visualization**: Plotly & scikit-learn (t-SNE)
- **LLM Providers**: OpenAI, Anthropic (via LangChain)
- **Document Processing**: PyPDF2, pdfplumber, LangChain text splitters

## Project Structure

```
rag-knowledge-worker/
├── src/                           # Source code
│   ├── data_ingestion.py          # Document loading and chunking (LangChain)
│   ├── embedder.py                # HuggingFace embeddings & Chroma integration
│   ├── visualize_vector_db.py     # t-SNE visualization utilities
│   ├── pdf_converter.py           # PDF to Markdown conversion
│   ├── rag_system.py              # Main RAG orchestrator (legacy)
│   ├── github_docs/               # GitHub documentation generator
│   ├── llm/                       # LLM integrations
│   ├── retrieval/                 # Retrieval mechanisms
│   ├── vector_store/              # Vector database management (legacy)
│   └── utils/                     # Utility functions
├── notebooks/                     # Jupyter notebooks
│   └── pipeline.ipynb             # Complete RAG pipeline demonstration
├── config/                        # Configuration files
├── data/                          # Data storage
│   ├── raw/                      # Raw documents
│   └── processed/                # Processed documents
│       ├── pdf_markdown/         # Converted PDFs
│       └── repo_summaries/       # GitHub repo documentation
├── vectors/                       # Chroma vector database storage
│   ├── chroma.sqlite3             # Metadata database
│   └── [collection-id]/           # Vector data and indices
├── docs/                          # Documentation
├── logs/                          # Application logs
├── main.py                        # Entry point
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Modules

### PDF Converter

Convert PDF files to Markdown format for easy ingestion into the RAG system.

```bash
python -m src.pdf_converter --input data/raw --output data/processed/pdf_markdown
```

Features:
- Extracts text from text-based PDFs
- Preserves folder structure in output
- Logs and skips image-based PDFs (scanned documents)
- Handles encrypted PDFs gracefully
- Provides detailed analysis reports

**CLI Usage:**
```bash
# Convert PDFs
python -m src.pdf_converter --input data/raw --output data/processed/pdf_markdown

# Analyze only (no conversion)
python -m src.pdf_converter --input data/raw --analyze-only
```

**Programmatic Usage:**
```python
from src.pdf_converter import convert_all_pdfs, analyze_pdfs
from pathlib import Path

stats = convert_all_pdfs(Path("data/raw"), Path("data/processed/pdf_markdown"))
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
   # Edit .env with your API keys (optional for embedding/indexing)
   ```

### Basic Usage (Python)

```python
from pathlib import Path
from src.data_ingestion import fetch_documents, chunking
from src.embedder import embedder

# 1. Collect document paths
data_dir = Path("data/processed/pdf_markdown")
filenames = [str(f) for f in data_dir.rglob("*.md")]

# 2. Load and chunk documents
documents = fetch_documents(filenames)
chunks = chunking(documents, chunk_size=1000, chunk_overlap=200)

# 3. Create embeddings and vector store
vectorstore = embedder("./vectors", chunks)

# 4. Query the system
results = vectorstore.similarity_search("machine learning projects", k=5)

for doc in results:
    print(f"Type: {doc.metadata['type']}")
    print(f"Content: {doc.page_content[:200]}...\n")
```

### With LLM Integration

```python
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import os

os.environ["OPENAI_API_KEY"] = "sk-..."

llm = ChatOpenAI(model="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5})
)

response = qa_chain.invoke({"query": "What are my key accomplishments?"})
print(response["result"])
```

### Visualize Embeddings

```python
from src.visualize_vector_db import visualize_2d, visualize_3d

# Create interactive 2D visualization
fig = visualize_2d(vectorstore, title="Document Embeddings")
fig.show()

# Export 3D visualization
fig_3d = visualize_3d(vectorstore)
fig_3d.write_html("embeddings_3d.html")
```

### Jupyter Notebook

For a complete walkthrough, see `notebooks/pipeline.ipynb`:

```bash
jupyter notebook notebooks/pipeline.ipynb
```
- Progress tracking with detailed status updates
- Configurable processing limits and model selection

For detailed documentation, see [docs/GITHUB_DOCS_GENERATOR.md](docs/GITHUB_DOCS_GENERATOR.md)

## Components

### 1. Data Ingestion (src/data_ingestion.py)
Handles loading documents and creating LangChain Document objects.

- `fetch_documents()`: Load files with automatic type detection from folder structure
- `chunking()`: Split documents using LangChain's RecursiveCharacterTextSplitter

### 2. Embeddings (src/embedder.py)
Generate high-quality vector embeddings using HuggingFace models.

- **Model**: `intfloat/e5-large-v2` (1024-dimensional)
- **Features**: Normalized embeddings for cosine similarity
- **Integration**: Direct Chroma vector store creation

### 3. Vector Store (Chroma)
Persistent vector database with metadata support.

- **Storage**: SQLite + file-based persistence in `vectors/`
- **Search**: Similarity search, metadata filtering, MMR
- **Scalability**: Handles up to 10M vectors efficiently

### 4. Visualization (src/visualize_vector_db.py)
Interactive visualization of vector embeddings.

- `visualize_2d()`: 2D t-SNE scatter plot with hover information
- `visualize_3d()`: 3D t-SNE interactive visualization
- **Features**: Color-coded by document type, exportable to HTML

### 5. PDF Converter (src/pdf_converter.py)
Convert PDF files to Markdown format.

- Extract text from text-based PDFs
- Preserve folder structure
- Detailed analysis reports
- Handle encrypted/scanned PDFs gracefully

### 6. LLM Integration (src/llm/)
Connect to language models for response generation.

- **OpenAI**: GPT-3.5, GPT-4 support
- **LangChain Integration**: Easy provider switching
- **Retrieval QA**: Built-in question answering chains

### 7. GitHub Documentation Generator (src/github_docs/)
Generate comprehensive documentation for GitHub repositories.

- **github_docs_generator.py**: Automated documentation generation
- Fetches repository structure and content via GitHub API
- Uses OpenAI API for structured markdown generation
- Outputs to `data/raw/repo_summaries/`

## Configuration

### Environment Variables (.env)

```env
# OpenAI API Key (for LLM generation, optional for embedding)
OPENAI_API_KEY=sk-...

# Anthropic API Key (alternative LLM provider)
ANTHROPIC_API_KEY=sk-ant-...

# GitHub Configuration (for documentation generator)
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=ghp_...

# Paths (optional, defaults exist)
VECTOR_DB_PATH=./vectors
DATA_PATH=./data
```

### Configuration File (config/config.json)

```json
{
  "chunking": {
    "chunk_size": 1000,
    "chunk_overlap": 200
  },
  "embedding": {
    "model": "intfloat/e5-large-v2",
    "dimension": 1024,
    "normalize": true
  },
  "retrieval": {
    "top_k": 5,
    "search_type": "similarity"
  },
  "llm": {
    "provider": "openai",
    "model": "gpt-4",
    "temperature": 0.7
  },
  "github_docs": {
    "model": "gpt-4.1-nano",
    "max_tree_items": 800,
    "max_file_chars": 12000,
    "output_dir": "./data/raw/repo_summaries"
  }
}
```

## Advanced Features

### Metadata Filtering

```python
# Search only within specific document types
results = vectorstore.similarity_search(
    query="neural networks",
    k=3,
    filter={"type": "research_papers"}
)
```

### Max Marginal Relevance (Diverse Results)

```python
# Get diverse results to avoid redundancy
results = vectorstore.max_marginal_relevance_search(
    query="Python programming",
    k=5,
    fetch_k=20
)
```

### Load Existing Vector Store

```python
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    encode_kwargs={"normalize_embeddings": True}
)

vectorstore = Chroma(
    persist_directory="./vectors",
    embedding_function=embeddings
)
```

### Custom Embedding Models

```python
# Use different HuggingFace model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={'device': 'cuda'},  # GPU support
    encode_kwargs={"normalize_embeddings": True}
)
```

### Conversational RAG

```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory
)
```

## Integration with Vector Databases

The system supports multiple vector databases via LangChain:

```python
# Chroma (current default - persistent, local)
from langchain_chroma import Chroma
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./vectors")

# Pinecone (cloud-based, scalable)
from langchain_pinecone import PineconeVectorStore
vectorstore = PineconeVectorStore.from_documents(chunks, embeddings, index_name="your-index")

# FAISS (high-performance, local)
from langchain_community.vectorstores import FAISS
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("./faiss_index")

# Weaviate (hybrid search, cloud/local)
from langchain_weaviate import WeaviateVectorStore
vectorstore = WeaviateVectorStore.from_documents(chunks, embeddings, client=client)
```

## Performance Optimization

1. **Batch Processing**: Process documents in batches to manage memory
2. **Chunk Optimization**: Adjust chunk_size (1000-2000) and overlap (100-400) based on your data
3. **Model Selection**: 
   - Fast: `sentence-transformers/all-MiniLM-L6-v2` (384-dim)
   - Balanced: `intfloat/e5-large-v2` (1024-dim, current default)
   - High Quality: `sentence-transformers/all-mpnet-base-v2` (768-dim)
4. **GPU Support**: Use `model_kwargs={'device': 'cuda'}` for faster embedding generation
5. **Vector Store**: Chroma (current) handles <10M vectors efficiently
6. **Caching**: Persistent Chroma storage eliminates re-embedding on restarts

## Troubleshooting

### Out of Memory Issues
- Process documents in smaller batches (100 files at a time)
- Use smaller embedding model: `all-MiniLM-L6-v2`
- Reduce chunk size to 500-800 characters
- Set `os.environ["TOKENIZERS_PARALLELISM"] = "false"`

### Low Retrieval Quality
- Increase chunk_size to 1500-2000 for more context
- Increase chunk_overlap to 300-400
- Use higher-quality embedding model: `all-mpnet-base-v2`
- Verify vector store has documents: `vectorstore._collection.count()`
- Use visualization to check embedding quality

### Slow Embedding Generation
- Enable GPU: `model_kwargs={'device': 'cuda'}` or `'mps'` (Mac)
- Use smaller/faster model: `all-MiniLM-L6-v2`
- Process documents in parallel batches

### Vector Store Issues
- Check if `vectors/` directory exists and has `chroma.sqlite3`
- Ensure consistent embedding model when loading existing store
- Delete `vectors/` folder to reset and recreate

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

- [x] LangChain integration for document processing
- [x] Chroma persistent vector store
- [x] High-quality e5-large-v2 embeddings
- [x] Interactive 2D/3D visualizations
- [x] Metadata-based filtering
- [ ] Streamlit/Gradio web interface
- [ ] REST API with FastAPI
- [ ] Docker containerization
- [ ] Multi-language document support
- [ ] Advanced RAG techniques (HyDE, RAG-Fusion)
- [ ] Fine-tuning support for custom domains
- [ ] Cloud deployment guides (AWS, GCP, Azure)

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
