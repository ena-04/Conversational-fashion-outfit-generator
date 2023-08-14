# # Step 1: Data Collection and Annotation
# [    ("What should I wear to a wedding?", {"entities": [(28, 35, "OCCASION")]}),
#     ("I'm going to a birthday party tonight.", {"entities": [(25, 38, "OCCASION")]}),
#     # Add more annotated examples
# ]


# Step 2: Data Preprocessing
import spacy
from spacy.training import Example
from spacy.scorer import Scorer
from spacy.training.example import Example

nlp = spacy.blank("en")  # Create a blank English model

# Annotated data
TRAIN_DATA = [
    ("What should I wear to a wedding?", {"entities": [(28, 35, "OCCASION")]}),
    ("I'm going to a birthday party tonight.", {"entities": [(25, 38, "OCCASION")]}),
    # Add more annotated examples
]

# Convert annotated data to Example objects
examples = []
for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    examples.append(example)


# Model Training
# Create a new NER component and add it to your pipeline.
nlp.add_pipe("ner", source=nlp.create_pipe("ner"))
ner = nlp.get_pipe("ner")

# Disable other pipeline components you don't intend to update during training (like tagger and parser).
disable_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*disable_pipes):
    optimizer = nlp.begin_training()

    for iteration in range(10):  # Number of training iterations
        for example in examples:
            nlp.update([example], drop=0.5, sgd=optimizer)



# Step 5: Model Deployment
output_dir = "path/to/output"
nlp.to_disk(output_dir)


loaded_nlp = spacy.load(output_dir)

# Step 4: Model Evaluation
# Prepare a separate evaluation dataset and evaluate the model's performance using metrics like precision, recall, and F1-score.
# Evaluation data
# EVAL_DATA = [
#     ("What should I wear to a wedding?", {"entities": [(28, 35, "OCCASION")]}),
#     ("I'm going to a birthday party tonight.", {"entities": [(25, 38, "OCCASION")]}),
#     # Add more annotated examples for evaluation
# ]


# Initialize scorer
# scorer = Scorer()

# # Evaluate the model
# for text, annotations in EVAL_DATA:
#     doc = loaded_nlp(text)
#     training_example = Example(doc, entities=annotations.get("entities"))
#     scorer.score(doc, training_example)

# # Calculate metrics
# precision = scorer.scores["ents_p"]
# recall = scorer.scores["ents_r"]
# f1_score = scorer.scores["ents_f"]

# print(f"Precision: {precision:.2f}")
# print(f"Recall: {recall:.2f}")
# print(f"F1-score: {f1_score:.2f}")



doc = loaded_nlp("What should I wear to a wedding?")
entities = [(ent.text, ent.label_) for ent in doc.ents]
