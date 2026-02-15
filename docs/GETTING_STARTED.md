# Getting Started Guide

## 1. Installation & Setup

### Step 1: Clone the Repository
```bash
cd LLM-RAG-private-knowledge-worker
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Requirements
```bash
pip install -r requirements.txt
```

**Key Dependencies** (installed automatically):
- `langchain` - Core LangChain framework
- `langchain-huggingface` - HuggingFace embeddings integration  
- `langchain-chroma` - Chroma vector store integration
- `chromadb` - Vector database
- `plotly` - Interactive visualizations
- `scikit-learn` - t-SNE for visualization

### Step 4: Configure Environment
```bash
cp .env.example .env
# Edit .env file with your API keys
```

**Required Environment Variables**:
```env
# For LLM generation (optional for embedding/indexing)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# For GitHub docs generation (optional)
GITHUB_USERNAME=your-username
GITHUB_TOKEN=ghp_...
```

## 2. Prepare Your Data

### Document Sources
Place your documents in `data/raw/` or process them to `data/processed/pdf_markdown/`:

```
data/
├── raw/                    # Original documents
│   ├── document1.pdf
│   └── research/
│       └── paper.pdf
└── processed/
    └── pdf_markdown/       # Converted markdown (recommended)
        ├── resume/
        ├── research_papers/
        └── projects/
```

### Convert PDFs to Markdown (Recommended)

For better text extraction, convert PDFs to markdown first:

```bash
python -m src.pdf_converter --input data/raw --output data/processed/pdf_markdown
```

**Supported Formats**:
- `.txt` - Plain text files
- `.md` - Markdown files (recommended after PDF conversion)
- `.pdf` - PDF documents (use pdf_converter for better results)

## 3. Quick Start (Jupyter Notebook)

The easiest way to get started is using the pipeline notebook:

```bash
jupyter notebook notebooks/pipeline.ipynb
```

This notebook walks you through:
1. Loading documents
2. Chunking text
3. Creating embeddings
4. Building vector store
5. Querying the system
6. Visualizing embeddings
## 4. Basic Usage (Python Script)

Create a file `my_rag.py`:

```python
from pathlib import Path
from src.data_ingestion import fetch_documents, chunking
from src.embedder import embedder

# Step 1: Collect document paths
data_dir = Path("data/processed/pdf_markdown")
filenames = [str(f) for f in data_dir.rglob("*.md")]

print(f"Found {len(filenames)} documents")

# Step 2: Load documents
documents = fetch_documents(filenames)

# Step 3: Chunk documents
chunks = chunking(documents, chunk_size=1000, chunk_overlap=200)

# Step 4: Create embeddings and vector store
vectorstore = embedder("./vectors", chunks)

# Step 5: Query the system
results = vectorstore.similarity_search("What is machine learning?", k=5)

for i, doc in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(f"Type: {doc.metadata['type']}")
    print(f"Source: {doc.metadata['source']}")
    print(f"Content: {doc.page_content[:300]}...")
```

Run it:
```bash
python my_rag.py
```

## 5. Load Existing Vector Store

If you've already created embeddings, load them without re-embedding:

```python
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize embeddings (must match original model)
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    encode_kwargs={"normalize_embeddings": True}
)

# Load existing vectorstore
vectorstore = Chroma(
    persist_directory="./vectors",
    embedding_function=embeddings
)

print(f"Loaded vectorstore with {vectorstore._collection.count()} documents")

# Query immediately
results = vectorstore.similarity_search("Python projects", k=3)
```

## 6. Visualize Your Embeddings

```python
from src.visualize_vector_db import visualize_2d, visualize_3d

# Create 2D visualization
fig_2d = visualize_2d(vectorstore, title="My Document Embeddings")
fig_2d.show()

# Create 3D visualization
fig_3d = visualize_3d(vectorstore)
fig_3d.write_html("embeddings_3d.html")  # Save to file
```

## 7. Advanced Querying

### With Metadata Filtering

```python
# Only search within research papers
results = vectorstore.similarity_search(
    query="neural networks",
    k=3,
    filter={"type": "research_papers"}
)
```

### With Scores

```python
results_with_scores = vectorstore.similarity_search_with_score(
    query="machine learning experience",
    k=5
)

for doc, score in results_with_scores:
    print(f"Score: {score:.3f}")
    print(f"Content: {doc.page_content[:200]}\n")
```

### Max Marginal Relevance (Diverse Results)

```python
# Get diverse results (avoid redundancy)
results = vectorstore.max_marginal_relevance_search(
    query="Python programming",
    k=5,
    fetch_k=20  # Fetch more candidates for diversity
)
```

## 8. Integrate with LLM

### Simple Question Answering

```python
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# Set API key
os.environ["OPENAI_API_KEY"] = "sk-..."

# Initialize LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5})
)

# Ask questions
response = qa_chain.invoke({"query": "What are my key accomplishments?"})

print(response["result"])
```

### Conversational RAG

```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

conversational_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory
)

# Multi-turn conversation
response1 = conversational_chain.invoke({"question": "What projects have I worked on?"})
response2 = conversational_chain.invoke({"question": "Tell me more about the machine learning ones"})
```

## 9. API Keys Setup

### OpenAI (for LLM responses)
1. Get API key from https://platform.openai.com/api-keys
2. Add to `.env`:
   ```env
   OPENAI_API_KEY=sk-...
   ```

### Anthropic Claude (alternative)
```env
ANTHROPIC_API_KEY=sk-ant-...
```

### HuggingFace (for custom models)
```env
HUGGINGFACE_API_TOKEN=hf_...
```

**Note**: Embeddings and vector storage work without API keys. Only LLM generation requires them.

## 10. Performance Tuning

### For Better Retrieval Quality
```python
# Larger chunks for more context
chunks = chunking(documents, chunk_size=2000, chunk_overlap=400)

# Retrieve more documents
results = vectorstore.similarity_search(query, k=10)
```

### For Faster Processing
```python
# Smaller chunks process faster
chunks = chunking(documents, chunk_size=500, chunk_overlap=50)

# Use smaller embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",  # 384-dim, faster
    encode_kwargs={"normalize_embeddings": True}
)
```

### For Lower Memory Usage
```python
# Process documents in batches
import numpy as np

for i in range(0, len(filenames), 100):  # Process 100 files at a time
    batch_files = filenames[i:i+100]
    docs = fetch_documents(batch_files)
    chunks = chunking(docs, chunk_size=800, chunk_overlap=100)
    vectorstore = embedder("./vectors", chunks)
```

## 11. Troubleshooting

### Issue: Out of Memory
```python
# Reduce batch size in embeddings
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Process smaller batches
# Use smaller chunks
```

### Issue: Slow Embedding Generation
```python
# Use GPU if available
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    model_kwargs={'device': 'cuda'},  # or 'mps' for Mac M1/M2
    encode_kwargs={"normalize_embeddings": True}
)
```

### Issue: Vector Store Not Found
```python
# Check if vectors directory exists
from pathlib import Path

if not Path("./vectors").exists():
    print("Vector store not found. Please create embeddings first.")
    # Run embedding creation
```

## 12. Next Steps

✅ **Explore Notebooks**: `notebooks/pipeline.ipynb` for interactive examples
✅ **Read API Reference**: [API_REFERENCE.md](API_REFERENCE.md) for detailed function docs
✅ **Check Architecture**: [ARCHITECTURE.md](ARCHITECTURE.md) for system design
✅ **Advanced Integration**: [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md) for production deployment

### Example Projects
1. **Personal Knowledge Base**: Index your notes, PDFs, research papers
2. **Resume Q&A Bot**: Build a chatbot about your experience
3. **Document Search Engine**: Create semantic search for your documents
4. **Research Assistant**: Query your research paper collection

---

**Need Help?**
- Check `notebooks/pipeline.ipynb` for working code
- Read component documentation in `docs/API_REFERENCE.md`
- View visualizations to debug retrieval quality
- Check vector store contents: `vectorstore._collection.count()`
