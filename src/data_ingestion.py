
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def fetch_documents(filenames):
    documents = []
    for filename in filenames:
        folder=Path(filename).parent.name.lower()
        with open(filename, "r", encoding="utf-8") as f:
            documents.append({"type": folder, "source": filename, "text": f.read()})
    print(f"Loaded {len(documents)} documents")
    return documents

def chunking(documents):
    docs = [
    Document(page_content=d["text"], metadata={"type": d["type"], "source": d["source"]})
    for d in documents]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    print(f"Divided into {len(chunks)} chunks")
    print(f"First chunk:\n\n{chunks[45]}")
    return chunks