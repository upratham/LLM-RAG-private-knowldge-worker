# API Reference

## Core Components (LangChain-Based)

This project uses LangChain for document processing, embeddings, and vector storage. Below are the main components and their usage.

## Data Ingestion

### fetch_documents()
Load documents from file paths with metadata.

```python
from src.data_ingestion import fetch_documents

filenames = ['data/processed/pdf_markdown/resume/cv.md', 
             'data/processed/pdf_markdown/research_papers/paper1.md']
documents = fetch_documents(filenames)
```

**Returns**: List of dictionaries with keys: `type`, `source`, `text`

**Parameters**:
- `filenames` (List[str]): List of file paths to load

**Features**:
- Automatically extracts document type from folder name
- Stores source path for provenance tracking
- UTF-8 encoding support

### chunking()
Split documents into chunks using LangChain's RecursiveCharacterTextSplitter.

```python
from src.data_ingestion import chunking

chunks = chunking(documents, chunk_size=1000, chunk_overlap=200)
```

**Returns**: List of LangChain `Document` objects

**Parameters**:
- `documents` (List[dict]): Documents from `fetch_documents()`
- `chunk_size` (int): Maximum chunk size in characters
- `chunk_overlap` (int): Overlap between chunks

**Features**:
- Preserves metadata through splitting
- Maintains context across chunk boundaries
- Uses intelligent splitting on natural boundaries

## Embeddings

### embedder()
Generate embeddings and create Chroma vector store.

```python
from src.embedder import embedder

db_path = "./vectors"
vectorstore = embedder(db_path, chunks)
```

**Returns**: Chroma vectorstore instance

**Parameters**:
- `db_path` (str): Path to persist Chroma database
- `chunks` (List[Document]): LangChain Document objects from chunking

**Model Details**:
- Model: `intfloat/e5-large-v2`
- Dimensions: 1024
- Normalization: Enabled (cosine similarity optimized)

**Features**:
- Automatic collection reset if database exists
- Persistent storage to disk
- Prints document count after creation

## Vector Store (Chroma)

### Direct Chroma Usage

```python
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    encode_kwargs={"normalize_embeddings": True}
)

# Load existing vectorstore
vectorstore = Chroma(
    persist_directory="./vectors",
    embedding_function=embeddings
)
```

### Similarity Search

```python
# Query the vectorstore
results = vectorstore.similarity_search(
    query="What is machine learning?",
    k=5
)

# With scores
results_with_scores = vectorstore.similarity_search_with_score(
    query="What is machine learning?",
    k=5
)

# With metadata filtering
results = vectorstore.similarity_search(
    query="research papers",
    k=3,
    filter={"type": "research_papers"}
)
```

**Methods**:
- `similarity_search(query, k)`: Get top-k similar documents
- `similarity_search_with_score(query, k)`: Include similarity scores
- `similarity_search_with_relevance_scores(query, k)`: Normalized scores
- `max_marginal_relevance_search(query, k)`: Diverse results

## Visualization

### visualize_2d()
Create 2D t-SNE visualization of vector embeddings.

```python
from src.visualize_vector_db import visualize_2d

fig = visualize_2d(
    vectorstore,
    title="Document Embeddings Visualization",
    width=1000,
    height=700,
    random_state=42
)
fig.show()
```

**Parameters**:
- `vector_store`: Chroma vectorstore instance
- `colors` (Dict[str, str], optional): Custom color mapping for document types
- `random_state` (int): For reproducibility
- `title` (str): Plot title
- `width`, `height` (int): Figure dimensions

**Returns**: Plotly Figure object

### visualize_3d()
Create 3D t-SNE visualization of vector embeddings.

```python
from src.visualize_vector_db import visualize_3d

fig = visualize_3d(
    vectorstore,
    title="3D Document Embeddings",
    width=1200,
    height=800
)
fig.write_html("visualization.html")
```

**Parameters**: Same as `visualize_2d()`

**Features**:
- Interactive hover showing document text preview
- Color-coded by document type
- Exportable to HTML
- Rotatable 3D view

## Complete Pipeline Example

```python
from pathlib import Path
from src.data_ingestion import fetch_documents, chunking
from src.embedder import embedder
from src.visualize_vector_db import visualize_2d

# 1. Collect file paths
data_dir = Path("data/processed/pdf_markdown")
filenames = list(data_dir.rglob("*.md"))

# 2. Load documents
documents = fetch_documents([str(f) for f in filenames])

# 3. Chunk documents
chunks = chunking(documents, chunk_size=1000, chunk_overlap=200)

# 4. Create embeddings and vector store
vectorstore = embedder("./vectors", chunks)

# 5. Query the system
results = vectorstore.similarity_search("machine learning experience", k=5)
for doc in results:
    print(f"Type: {doc.metadata['type']}")
    print(f"Source: {doc.metadata['source']}")
    print(f"Content: {doc.page_content[:200]}...")
    print("-" * 80)

# 6. Visualize
fig = visualize_2d(vectorstore)
fig.show()
```

## Advanced Usage

### Custom Embeddings Model

```python
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Use different model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./vectors_custom"
)
```

### Alternative Vector Stores

```python
# Pinecone
from langchain_pinecone import PineconeVectorStore

vectorstore = PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name="your-index"
)

# FAISS (local, high-performance)
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("./faiss_index")
```

### Custom Text Splitter

```python
from langchain_text_splitters import CharacterTextSplitter, MarkdownHeaderTextSplitter

# Character-based splitting
splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=500,
    chunk_overlap=50
)

# Markdown-aware splitting
md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
    ]
)
```

## LLM Integration (Examples)

### OpenAI with RAG

```python
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model="gpt-4", temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5})
)

response = qa_chain.invoke({"query": "What is your experience in machine learning?"})
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
conversational_chain.invoke({"question": "What projects have you worked on?"})
conversational_chain.invoke({"question": "Tell me more about the first one"})
```

## Utility Functions

### Color Mapping for Visualization

```python
from src.visualize_vector_db import get_default_colors, map_colors

# Get default color scheme
colors = get_default_colors()
# {'extra cariculam': 'red', 'internships': 'blue', ...}

# Custom colors
custom_colors = {
    'resume': '#FF6B6B',
    'research_papers': '#4ECDC4',
    'projects': '#45B7D1'
}

# Map document types to colors
doc_types = ['resume', 'resume', 'projects']
colors_list = map_colors(doc_types, custom_colors)
```

### Prepare Visualization Data

```python
from src.visualize_vector_db import prepare_visualization_data

vectors, documents, doc_types, metadatas = prepare_visualization_data(vectorstore)

print(f"Total documents: {len(documents)}")
print(f"Vector dimensions: {vectors.shape}")
print(f"Document types: {set(doc_types)}")
```

## Configuration

### Environment Variables

```bash
# .env file
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
HUGGINGFACE_API_TOKEN=hf_...
```

### LangChain Settings

```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
os.environ["LANGCHAIN_PROJECT"] = "rag-knowledge-worker"
```

---

For Jupyter notebook examples, see `notebooks/pipeline.ipynb`
