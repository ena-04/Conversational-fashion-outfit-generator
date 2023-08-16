import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_md")

# Example text containing Indian location
text = "Suggest outfit for teenager in muzaffarpur."

# Process the text with the NER model
doc = nlp(text)

# Iterate through entities and print them
for ent in doc.ents:
    print(ent.text, ent.label_)
