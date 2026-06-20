import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader

from utils.text_splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store


def load_pdf(pdf_path):
    """
    Load a PDF and return LangChain Documents.
    """
    loader = PyPDFLoader(pdf_path)
    return loader.load()


def process_uploaded_pdf(uploaded_file):
    """
    Save, process and index an uploaded PDF.
    """

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join(
        "data",
        uploaded_file.name,
    )

    # Save uploaded file
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing PDF..."):

        documents = load_pdf(pdf_path)

        chunks = split_documents(documents)

        embeddings = get_embeddings()

        vector_store = create_vector_store(
            chunks,
            embeddings,
        )

        st.session_state.vector_store = vector_store

    st.success("✅ PDF indexed successfully!")