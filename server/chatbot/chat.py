import random
import json
import os
import torch
import spacy
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics.pairwise import cosine_similarity

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

base_path = os.path.abspath(os.path.dirname(__file__))
    
    # Construct the relative path to intents.json
relative_path = 'intents.json'
file_path = os.path.join(base_path, relative_path)
    
    # Open and read the JSON file
    

with open(file_path, 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

occasion=[]
location=None
gender=None
age=None
colourset=["pink"+"black"+"purple"]
colours = " ".join(colourset)
# required=[]

def get_location(prompt):
    

    csv_file_path = '..\data\indian_places.csv'
    # Load the specific CSV file
    data = pd.read_csv(csv_file_path, header=None, names=['place_name'])

    # Filter the dataset to include only Indian place names
    indian_places = data['place_name']


    # Initialize TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)

    # Transform the Indian place names into TF-IDF features
    indian_places_tfidf = tfidf_vectorizer.fit_transform(indian_places)

    # Initialize and train a Naive Bayes classifier
    naive_bayes_classifier = MultinomialNB()
    naive_bayes_classifier.fit(indian_places_tfidf, indian_places)


    # Tokenize and transform the user prompt into TF-IDF features
    user_prompt_tfidf = tfidf_vectorizer.transform([prompt])

    # Calculate cosine similarity between user prompt and Indian place names
    cosine_similarities = cosine_similarity(user_prompt_tfidf, indian_places_tfidf)

    # Find the index of the most similar Indian place
    most_similar_index = cosine_similarities.argmax()

    # Get the corresponding place name
    detected_place = indian_places.iloc[most_similar_index]
    print (detected_place)
    return detected_place


def check_prompt(prompt):
    print("checking...")

    nlp1 = spacy.load(r"../models/ner_model_occasion/output/model-best") #load the best model
    nlp2 = spacy.load("en_core_web_md")

    # occasion=[]
    # location=[]
    required=[]

    doc1 = nlp1(prompt) # input sample text

    for entity in doc1.ents:
        # print(entity.text, entity.label_)
        occasion.append(entity.label_)

    if not occasion:
        # print("occasion reqd")
        required.append("occasion")
    
    global location
    location=get_location(prompt)
    
    if not location:
        # print("location reqd")
        required.append("location")
    # else:
        # for loc in location: print ("**"+loc)


    substrings = ["man", "woman", "girl", "boy","lady","male","female","baby"]

    main_string_lower = prompt.lower()
    global gender
    for substring in substrings:
        if substring.lower() in main_string_lower:
            gender=substring
    if not gender:
        required.append("gender")

    
    pattern = r'\d+'  # Regular expression pattern for one or more digits
    global age
    age = re.findall(pattern, prompt)
    if not age:
        required.append("age")

        
    if not required:
        return True
    
    print("Please add ",end="")

    for index, req in enumerate(required):
        # print("printing reqd")
        print(req,end="")
        if index != (len(required) - 1):
            print(" and ",end="")

    print(" for which you want the suggestion")

    return False

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."

# from ../main_app import get_answer_bard

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    to_bard=False
    count=0
    initial_prompt=None
    while True:
        
        sentence = input("You: ")
        if sentence == "quit":
            break

        if to_bard==False:
            resp = get_response(sentence)
            # print(resp)

            if resp=='I do not understand...':
                count+=1
                if count==1:
                    initial_prompt=sentence
                to_bard=check_prompt(sentence)
                if to_bard==True:
                    
                    sentence=initial_prompt+" I am "+age+" years old "+gender+" from "+location+", occasion is "+occasion+", my colour preferences are "+colours
            
            else:
                print(resp)
        if to_bard==True:
            get_answer_bard(sentence)


