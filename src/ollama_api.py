import subprocess

import unicodedata
import re


def clean_text(text):
    """
    Cleans the input text by:
    - Removing invisible/zero-width characters
    - Normalizing Unicode
    - Removing non-printable characters
    """
    # Normalize Unicode (NFKD separates combined characters)
    text = unicodedata.normalize("NFKD", text)

    # Remove zero-width and non-printable characters
    text = re.sub(r"[\u200b\u200c\u200d\uFEFF]", "", text)  # Remove zero-width stuff
    text = "".join(c for c in text if c.isprintable())

    return text.strip()


def generate_response_with_ollama(context, query):
    """
    Clean and pass the prompt to Ollama using stdin to avoid encoding issues.
    """
    context = clean_text(context)
    query = clean_text(query)

    prompt = f"{context}\n\nQuestion: {query}\nAnswer:"

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral:latest"],
            input=prompt,
            text=True,
            encoding="utf-8",  # Make sure to use UTF-8 to support all cleaned characters
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
        return f"Error generating response: {e.stderr.strip()}"
