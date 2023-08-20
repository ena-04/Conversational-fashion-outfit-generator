item_list=['Anarkali suit in pink, black, and purple with a matching salwar.', 'Pumps in black or purple.', 'Traditional jewelry such as a necklace, earrings, and bangles.', 'A bindi and mehndi to complete the look.']

# from main_app import item_list
# * A long, pink maxi dress with a black belt and a slit up the side.

# * Black high heels or sandals.

# * A small, black clutch purse.

# * A silver necklace and bracelet.

# * Pink earrings.

import spacy
import string

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define your custom stopwords
custom_stopwords = ['matching','complete','look']

# Define a translation table to remove punctuations
translator = str.maketrans("", "", string.punctuation)

# Extend the stopwords list
nlp.Defaults.stop_words |= set(custom_stopwords)

filtered_list=[]

for item in item_list:

    # Process the text with spaCy
    doc = nlp(item)

    # Create a list of tokens without stopwords and punctuations
    filtered_tokens = [token.text.translate(translator) for token in doc if not token.is_stop]

    # Join the filtered tokens back into a sentence
    filtered_sentence = ' '.join(filtered_tokens)

    filtered_list.append(filtered_sentence)


