# src/app.py
import streamlit as st
from retrieval import retrieve_relevant_documents
from ollama_api import generate_response_with_ollama
from openai_api import generate_response_with_openai
from google_api import generate_response_with_google  # Add this line


def main():
    st.title("💬APKA")

    # LLM Selection
    llm_choice = st.selectbox(
        "Choose a model:", ["Ollama (Mistral)", "OpenAI (GPT-3.5/4)", "Google (Gemini)"]
    )

    # User Input
    user_input = st.text_input("Enter your query:")

    if user_input:
        # Retrieve relevant documents
        relevant_docs = retrieve_relevant_documents(user_input)
        context = "\n".join(relevant_docs)

        if not relevant_docs:
            st.warning("No relevant documents found.")
            return

        # Choose LLM
        if llm_choice == "Ollama (Mistral)":
            response = generate_response_with_ollama(context, user_input)
        elif llm_choice == "OpenAI (GPT-3.5/4)":
            response = generate_response_with_openai(context, user_input)
        else:  # Handle the Google option
            response = generate_response_with_google(context, user_input)

        # Show output
        st.subheader("Answer:")
        st.write(response)


if __name__ == "__main__":
    main()
