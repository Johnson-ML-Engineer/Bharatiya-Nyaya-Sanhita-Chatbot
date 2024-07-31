import streamlit as st
from config import setup_environment
from rag_initializer import initialize_rag_chain
from chatbot import chatbot_response

setup_environment()

st.set_page_config(page_title="Bharatiya Nyaya Sanhita Chatbot", page_icon="⚖️", layout="wide")

def main():
    st.title("Bharatiya Nyaya Sanhita Chatbot")
    st.sidebar.info("Bharatiya Nyaya Sanhita came into effect on 1 July, 2024 after being passed by the parliament in December 2023 to replace the Indian Penal Code (IPC), which dated back to the period of British India")
    st.sidebar.warning("Disclaimer: This chatbot provides information based on the Bharatiya Nyaya Sanhita for reference purposes only. It is not a substitute for professional legal advice.")

    rag_chain = initialize_rag_chain()
    
    if rag_chain is None:
        st.error("Failed to initialize the chatbot. Please try again later.")
        return
    
    st.write("Welcome! I'm here to help you with information about the Bharatiya Nyaya Sanhita. What would you like to know?")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Your question:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("AI is thinking..."):
                response = chatbot_response(prompt, rag_chain)
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    
if __name__ == "__main__":
    main()