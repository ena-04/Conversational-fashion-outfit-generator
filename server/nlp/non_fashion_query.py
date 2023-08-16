from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bardapi import Bard
from dotenv import load_dotenv
import os
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.metrics import jaccard_distance

# Load environment variables
load_dotenv()

# Access environment variables
token = os.environ.get("BARD_API_KEY")

# Create a Bard instance
bard = Bard(token=token)

# Initialize the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Read the content of the text file
with open("D:\\conversational-fashion-outfit-generator\\server\\data\\fashion_keywords.txt", "r") as file:
    content = file.read()

# Split the content into phrases based on commas
phrases = content.split(',')

# Remove leading and trailing whitespace from each phrase and create a list
phrase_list = [phrase.strip() for phrase in phrases]

# Fit the vectorizer on your phrases
fashion_vectors = vectorizer.fit_transform(phrase_list)

def is_fashion_related(query, threshold=0.8):
    if not query.strip():  # Check if the query is empty or only whitespace
        return False

    # Transform the user query into a TF-IDF vector
    query_vector = vectorizer.transform([query])

    # Calculate cosine similarity between query vector and fashion vectors
    similarities = cosine_similarity(query_vector, fashion_vectors)[0]

    print("Similarities:", similarities)
    print("Threshold:", threshold)

    # Check if any similarity is above the threshold
    return any(similarity >= threshold for similarity in similarities)

def bold_text(text):
    return text.replace('**', '<b>').replace('</b>', '</b>')

def fashion_chatbot(user_message):
    # Tokenize user input into words
    user_tokens = word_tokenize(user_message.lower())

    # Preprocess user tokens
    stop_words = set(stopwords.words("english"))
    user_tokens = [token for token in user_tokens if token.isalpha() and token not in stop_words]

    # Calculate Jaccard similarity for each user token with phrase list
    matches = []
    for user_token in user_tokens:
        max_similarity = 0
        best_match = None
        for phrase in phrase_list:
            phrase_tokens = word_tokenize(phrase.lower())
            phrase_tokens = [token for token in phrase_tokens if token.isalpha() and token not in stop_words]
            jaccard_sim = 1 - jaccard_distance(set([user_token]), set(phrase_tokens))
            if jaccard_sim > max_similarity:
                max_similarity = jaccard_sim
                best_match = phrase
        matches.append((user_token, best_match, max_similarity))

    # Print the positive matches
    positive_matches = [(token, match, similarity) for token, match, similarity in matches if similarity > 0.7]


    for token, match, similarity in positive_matches:
        print(f"User Token: {token}")
        print(f"Best Match: {match}")
        print(f"Similarity: {similarity:.2f}")
        print()


    if positive_matches:
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
user_query = "Hello ! what is the news today ?"
response = fashion_chatbot(user_query)
print(response)
