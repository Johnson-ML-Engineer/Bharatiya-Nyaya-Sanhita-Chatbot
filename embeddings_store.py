from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def create_embeddings_and_store(doc_chunks):
    vectorstore = Chroma.from_documents(
        documents=doc_chunks, 
        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    )
    
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    
    system_prompt = """
You are an AI assistant for question-answering tasks about the Bharatiya Nyaya Sanhita.Bharatiya Nyaya Sanhita came into effect on 1 July, 2024 after being passed by the parliament in December 2023 to replace the Indian Penal Code (IPC), which dated back to the period of British India
 Analyze the provided context and answer the user's question concisely. Follow these guidelines:

1. Use only the given context to formulate your response.
2. If the answer cannot be derived from the context, state "I don't have enough information to answer this question."
3. Provide a clear, direct answer in seven sentences or fewer.

Context:
{context}
"""
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    llm_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3, max_tokens=250)
    
    question_answer_chain = create_stuff_documents_chain(llm_model, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)