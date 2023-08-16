# from __future__ import unicode_literals, print_function
# import plac
# import random
# from pathlib import Path
# import spacy
# from tqdm import tqdm

# nlp1 = spacy.load("en_core_web_md")

TRAIN_DATA =[["She wore a beautiful white dress to the party.\r",{"entities":[[21,26,"COLOUR"]]}],["He prefers to wear a black suit for formal events.\r",{"entities":[[21,26,"COLOUR"]]}],["Her yellow scarf added a vibrant touch to her outfit.\r",{"entities":[[4,10,"COLOUR"]]}],["The red shoes perfectly matched her red lipstick.\r",{"entities":[[4,7,"COLOUR"],[36,39,"COLOUR"]]}],["His blue tie complemented his blue shirt elegantly.\r",{"entities":[[4,8,"COLOUR"],[30,34,"COLOUR"]]}],["She looked lovely in her pink blouse and skirt.\r",{"entities":[[25,29,"COLOUR"]]}],["The beige jacket provided a neutral contrast.\r",{"entities":[[4,9,"COLOUR"]]}],["His brown leather shoes completed the classic look.\r",{"entities":[[4,9,"COLOUR"]]}],["She chose a cream-colored dress for the summer wedding.\r",{"entities":[[12,25,"COLOUR"]]}],["The dark blue jeans were a stylish choice for the day.\r",{"entities":[[4,13,"COLOUR"]]}],["The dark green hat added a pop of color to his attire.\r",{"entities":[[4,14,"COLOUR"]]}],["The gold accents on her accessories sparkled in the light.\r",{"entities":[[4,8,"COLOUR"]]}],["The green jacket suited his adventurous personality.\r",{"entities":[[4,9,"COLOUR"]]}],["The grey sweater kept her warm on the chilly day.\r",{"entities":[[4,8,"COLOUR"]]}],["His khaki pants were comfortable for the outdoor event.\r",{"entities":[[4,9,"COLOUR"]]}],["She loved the light blue dress for its simplicity.\r",{"entities":[[14,24,"COLOUR"]]}],["The light green scarf matched the spring theme.\r",{"entities":[[4,15,"COLOUR"]]}],["The maroon tie added a touch of sophistication.\r",{"entities":[[4,10,"COLOUR"]]}],["The multicolor skirt was a cheerful and vibrant choice.\r",{"entities":[[4,14,"COLOUR"]]}],["The navy blue blazer completed his professional look.\r",{"entities":[[4,13,"COLOUR"]]}],["Her orange scarf brightened up the entire outfit.\r",{"entities":[[4,10,"COLOUR"]]}],["The purple handbag added a touch of elegance.\r",{"entities":[[4,10,"COLOUR"]]}],["His silver watch was a stylish accessory.",{"entities":[[4,10,"COLOUR"]]}]]

import pandas as pd
import spacy
import os
from tqdm import tqdm
from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_sm")

db = DocBin() # create a DocBin object

for text, annot in tqdm(TRAIN_DATA): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("./train.spacy") # save the docbin object

nlp1 = spacy.load(r"./output/model-best") #load the best model


doc = nlp1("I am looking for a executive black flip-flops") # input sample text
for entity in doc.ents:
    print(entity.text, entity.label_)
