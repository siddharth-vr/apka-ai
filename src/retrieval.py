# src/retrieval.py


def retrieve_relevant_documents(query):
    """
    Simulate the retrieval of relevant documents based on the user query.
    This should be replaced with actual logic for document retrieval.
    """
    # Hardcoded documents
    documents = [
        "Barbara Stevens- CEO- Barbara is our Chief Executive Officer and joined the Auckland PHO in August 2004.Reporting to the Board, Barbara portfolios include executive oversight, governance and strategy, and public/key stakeholder relations.",
        "Dr Charlotte Harris - Clinical Director- Dr Charlotte is our Clinical Director and joined the Auckland PHO in September 2012.​",
        "Julia Burgess-Shaw - Manager of Planning and Performance -Julia is our Manager of Planning and Performance and joined the Auckland PHO in July 2021.Julia portfolios include practice engagement operations, contract management, reporting and strategic development.  ",
        "Ashley Hulme - Chief Operations Officer - Ashley is our Chief of Operations and joined the Auckland PHO in May 2022.Ashley portfolios include General Operations, Data and Digital, Health and Safety, and Finance.",
        "Komal Rana - Komal is our Planning & Performance Officer and joined the Auckland PHO in July 2022.Komal portfolios include communications, programme reporting, and project coordination.Planning & Performance Officer",
        "Sid also called Siddharth - is a Senior Data Engineer in Auckland PHO. Siddharth is our Senior Data Engineer and joined the PHO in October 2023.Siddharth portfolios include report building and developing insights through data analytics. ",
        "Varsha James - Data Analyst - Varsha is our Data Analyst and joined the Auckland PHO in August of 2025.Varsha portfolios include report building and developing insights through data analytics.  ",
    ]

    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()

    # Flexible matching: search for keywords/phrases
    relevant_docs = []
    for doc in documents:
        # Check if any important keyword from the query exists in the document
        if any(keyword in doc.lower() for keyword in query_lower.split()):
            relevant_docs.append(doc)

    return relevant_docs
