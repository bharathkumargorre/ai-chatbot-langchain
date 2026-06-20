from langchain_community.vectorstores import Chroma

def create_vector_store(chunks, embeddings):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )