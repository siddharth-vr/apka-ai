# src/google_api.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the SDK with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_response_with_google(context, query):
    """
    Generates a response using a Google Gemini model.
    """
    try:
        # Select the Gemini model to use
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Create the prompt, combining context and query
        prompt = f"Context:\n{context}\n\nQuestion: {query}"

        # Generate a response from the model
        response = model.generate_content(prompt)

        # Return the generated text
        return response.text.strip()

    except Exception as e:
        # Handle potential errors from the API call
        return f"Google API Error: {str(e)}"
