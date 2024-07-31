def chatbot_response(query, rag_chain):
    try:
        return rag_chain.invoke({"input": query})["answer"]
    except Exception as e:
        return f"Error processing query: {str(e)}"