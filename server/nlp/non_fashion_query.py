import spacy
from bardapi import Bard
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access environment variables
token = os.environ.get("BARD_API_KEY")

# Create a Bard instance
bard = Bard(token=token)

# Load the spaCy English model
nlp = spacy.load("en_core_web_lg")

def is_fashion_related(query):
    # Define fashion-related keywords
    fashion_keywords = ["outfit", "clothing", "style", "Fashion trends"]
    
    # Tokenize the query using spaCy
    doc = nlp(query.lower())
    
    # Check if any fashion keywords are present in the query
    for token in doc:
        if token.text in fashion_keywords:
            return True
    
    return False

def bold_text(text):
    return f"<b>{text}</b>"

def fashion_chatbot(user_message):
    if is_fashion_related(user_message):
        result = bard.get_answer(user_message)
        bard_response = result["content"]

        lines = bard_response.split("\n")
        filtered_lines = [line for line in lines if not line.startswith("[Image")]
        filtered_response = "\n".join(filtered_lines)

        bot_response = bold_text(filtered_response)
        return bot_response
    else:
        return "I'm here to talk about fashion trends and outfits. Please ask me a fashion-related question."

# Example usage
user_query = "What is the Fashion trends now?"
response = fashion_chatbot(user_query)
print(response)
