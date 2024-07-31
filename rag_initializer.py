import streamlit as st
from document_processor import read_documents, chunk_data
from embeddings_store import create_embeddings_and_store

@st.cache_resource
def initialize_rag_chain():
    try:
        docs = read_documents("bns3.pdf")
        doc_chunks = chunk_data(docs)
        return create_embeddings_and_store(doc_chunks)
    except Exception as e:
        st.error(f"Error initializing RAG chain: {str(e)}")
        return None