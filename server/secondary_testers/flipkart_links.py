import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def generate_flipkart_url(search_query, filters):
    base_url = "https://www.flipkart.com/search?q="
    search_query = search_query.replace(" ", "%20")
    url = f"{base_url}{search_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

    if filters:
        filter_string = "&" + "&".join(filters)
        url += filter_string

    return url

# Ask the user for a search query
search_query = input("Enter your search query: ")

# Process the search query with spaCy
doc = nlp(search_query)

occasion = None
color = None

# Iterate through the tokens in the processed query
for token in doc:
    if token.dep_ == "attr" and token.head.text.lower() == "suit":
        occasion = token.text
    if token.text.lower() in ["pink", "purple", "black"]:
        color = token.text

print("Extracted Occasion:", occasion)
print("Extracted Color:", color)

occasion_filter = occasion
color_filter = color

final_url = generate_flipkart_url(search_query, occasion_filter, color_filter)
print("Generated Flipkart URL:")
print(final_url)
