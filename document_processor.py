from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def read_documents(directory):
    return PyPDFDirectoryLoader(directory).load()

def chunk_data(docs, chunk_size=800, chunk_overlap=40):
    return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap).split_documents(docs)