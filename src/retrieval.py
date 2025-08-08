# src/retrieval.py

# A constant for the file path, making it easy to change later if needed.
DOCUMENTS_FILE_PATH = "documents.txt"


def load_documents_from_file():
    """
    Loads documents from a file, returning a list of strings.
    """
    try:
        with open(DOCUMENTS_FILE_PATH, "r", encoding="utf-8") as f:
            # Each line in the file is treated as a separate document
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{DOCUMENTS_FILE_PATH}' was not found.")
        return []


def retrieve_relevant_documents(query):
    """
    Retrieves relevant documents from a text file based on a user query.
    """
    documents = load_documents_from_file()

    if not documents:
        return []

    query_lower = query.lower()
    relevant_docs = []

    # Split the query into keywords to check against the documents
    query_keywords = query_lower.split()

    for doc in documents:
        # Check if any keyword from the query is present in the document
        if any(keyword in doc.lower() for keyword in query_keywords):
            relevant_docs.append(doc)

    return relevant_docs
