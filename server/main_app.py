from flask import Flask, request, jsonify
from bardapi import Bard
import os
from dotenv.main import load_dotenv
# import sys
# import random
# import json
# import torch
import spacy
import re
import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics.pairwise import cosine_similarity

# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize


from flask_cors import CORS, cross_origin


# Load environment variables
load_dotenv()

# Access environment variables
token = os.environ.get("BARD_API_KEY")

# Create a Bard instance
bard = Bard(token=token)


# Create a Flask app instance
app = Flask(__name__)
CORS(app)


# D:\Neha\web development\Conversational-fashion-outfit-generator\server\main_app.py

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# base_path = os.path.abspath(os.path.dirname(__file__))
    
#     # Construct the relative path to intents.json
# relative_path = '.\chatbot\intents.json'
# file_path = os.path.join(base_path, relative_path)

#     # D:\Neha\web development\Conversational-fashion-outfit-generator\server\chatbot\intents.json
#     # Open and read the JSON file
    

# with open(file_path, 'r') as json_data:
#     intents = json.load(json_data)

# FILE = ".\chatbot\data.pth"
# data = torch.load(FILE)

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()








def bold_text(text):
    text1 = text.replace(" **", " <b>")
    text2 = text1.replace("** ", "</b> ")
    return text2

# def get_answer_bot(msg):
#     sentence = tokenize(msg)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 return random.choice(intent['responses'])
    
#     return "I do not understand..."

to_bard=False
count=0
initial_prompt=None


occasion=[]
required=["occasion","location","gender","age"]
location=None
gender=None
age=None
colourset=["pink"+"black"+"purple"]
colours = " ".join(colourset)
# required=[]

def get_location(prompt):
    

    csv_file_path = '.\data\indian_places.csv'
    # Load the specific CSV file
    data = pd.read_csv(csv_file_path, header=None, names=['place_name'])

    # Filter the dataset to include only Indian place names
    indian_places = data['place_name']


    detected_place=None
    main_string_lower = prompt.lower()
    
    for substring in indian_places:
        if substring.strip().lower() in main_string_lower:
            detected_place = substring.strip()
            print("detected_place:", detected_place)

    return detected_place





def check_prompt(prompt):
    global to_bard
    global required
    print("checking...")

    nlp1 = spacy.load(r"./models/ner_model_occasion/output/model-best") #load the best model
    nlp2 = spacy.load("en_core_web_md")

    # occasion=[]
    # location=[]
    # required=[]

    doc1 = nlp1(prompt) # input sample text

    for entity in doc1.ents:
        print("detected_occasion: ",end=" ")
        print(entity.text, entity.label_)
        occasion.append(entity.label_)

    if occasion:
        if "occasion" in required:
            required.remove("occasion")

    


    substrings = ["man", "woman", "girl", "boy","lady","male","female","baby"]

    main_string_lower = prompt.lower()
    global gender
    for substring in substrings:
        pattern = r'\b' + re.escape(substring.lower()) + r'\b'
        if re.search(pattern, main_string_lower):
            
            gender=substring
            print("detected_gender: "+gender)
    if gender:
        if "gender" in required:
            required.remove("gender")


    global location
    if not location:
        location=get_location(prompt)
    
    if location:
        if "location" in required:
            required.remove("location")
    
    pattern = r'\d+'  # Regular expression pattern for one or more digits
    global age
    if not age:
        
        age = re.findall(pattern, prompt)
        age2=" ".join(age)
        age=age2
        print("detected_age: "+age)
    if age:
        if "age" in required:
            required.remove("age")

    response=None  
    if not required:
        to_bard= True
        return response
    
    if required[0]=="occasion":
        response="Sure! Please add "+required[0]+" for which you want the suggestion"
    elif required[0]=="gender":
        response="Further tell me your "+required[0]
    elif required[0]=="location":
        response="Where is the "+required[0]+" you are from?"
    else:
        response="Finally tell me how old are you?"

    to_bard= False
    return response



def get_answer_bard(prompt):
    prompt+=", suggest a single entire outfit idea with top, bottom, shoes, jewelry and accessories. Do not give additional tips and information. Keep your response very short within 100 words."
    result = bard.get_answer(prompt)
    print(result)
    bard_response = result["content"]
    lines = bard_response.split("\n")
    filtered_lines = [line for line in lines if not line.startswith("[Image")]
    filtered_response = "\n".join(filtered_lines)
    return bold_text(filtered_response)



@app.route("/api/recommendations", methods=["POST"])
@cross_origin(origin="*")
def get_recommendations():
    user_message = request.json["userMessage"]
    global count


    if user_message:



        if to_bard==False:
                
                    count+=1
                    if count==1:
                        global initial_prompt
                        initial_prompt=user_message
                    resp=check_prompt(user_message)
                    if to_bard==True:
                        
                        occasion2=" ".join(occasion)
                        print("detected_occasion: "+occasion2)
                        user_message=initial_prompt+" I am "+age+" years old "+gender+" from "+location+", occasion is "+occasion2+", my colour preferences are "+colours

                    else:
                         bot_response=resp
                
                
        if to_bard==True:
                bot_response=get_answer_bard(user_message)
        
    
    return jsonify({"bot_response": bot_response})






@app.route('/fresh-chat', methods=['POST'])
def fresh_chat():
    print("creating new conversation thread with bard")
    
    # Additional cleanup or shutdown logic can be added here.
    
    # Restart the server by using sys.executable to run the current Python script.
    # os.execl(sys.executable, sys.executable, *sys.argv)
    global bard
    bard = Bard(token=token)
    return jsonify({"bot_response": "bot_response"})
   
    
if __name__ == '__main__':
    app.run(debug=True)

