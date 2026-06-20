from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embeddings():
    """
    Returns the embedding model used for vector search.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )