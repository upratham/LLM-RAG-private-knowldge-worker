from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os
def embedder(db_path, chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/e5-large-v2",
        encode_kwargs={"normalize_embeddings": True},  # recommended for cosine similarity
    )
    if os.path.exists(db_path):
        Chroma(persist_directory=db_path, embedding_function=embeddings).delete_collection()
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_path)
    print(f"Vectorstore created with {vectorstore._collection.count()} documents")
    return vectorstore

