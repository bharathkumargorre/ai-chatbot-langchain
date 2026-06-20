from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


def create_vector_store(
    chunks: list[Document],
    embeddings: Embeddings,
) -> FAISS:
    """
    Create and return a FAISS vector store.

    Args:
        chunks: List of split documents.
        embeddings: Embedding model.

    Returns:
        FAISS vector store.
    """

    return FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )