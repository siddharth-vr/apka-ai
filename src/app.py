import streamlit as st
from retrieval import retrieve_relevant_documents
from ollama_api import generate_response_with_ollama


def main():
    st.title("APKA")

    # Text input for user query
    user_input = st.text_input("Enter your query:")

    if user_input:
        # Step 1: Retrieve relevant documents
        relevant_docs = retrieve_relevant_documents(user_input)
        context = "\n".join(
            relevant_docs
        )  # Combine relevant docs into a single context

        if not relevant_docs:
            st.warning("I couldn't find anything relevant, but here's what I know:")
            # st.write("No relevant documents found.")
            # return

        # Step 2: Generate response using Ollama
        response = generate_response_with_ollama(context, user_input)

        # Step 3: Display the result
        # st.write("### Relevant Documents:")
        # st.write(context)
        st.write("### Generated Response:")
        st.write(response)


if __name__ == "__main__":
    main()
