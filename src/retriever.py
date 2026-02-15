from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
def get_retriever(db_path):
    embeddings = HuggingFaceEmbeddings(
            model_name="intfloat/e5-large-v2",
            encode_kwargs={"normalize_embeddings": True},  # recommended for cosine similarity
        )
    vectorstore = Chroma(persist_directory=db_path, embedding_function=embeddings)
    retriever = vectorstore.as_retriever()
    return retriever