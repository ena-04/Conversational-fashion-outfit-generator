import joblib

# Load the trained model and vectorizer
loaded_model = joblib.load('D:\\conversational-fashion-outfit-generator\\server\\models\\trained_model.pkl')
loaded_vectorizer = joblib.load('D:\\conversational-fashion-outfit-generator\\server\\models\\vectorizer.pkl')

# Prepare new data
new_input = [
    "What should I wear for a formal event?",
    "Any suggestions for casual wear?",
    "Hi How are you"
]

# Transform new data using the loaded vectorizer
new_input_tfidf = loaded_vectorizer.transform(new_input)

# Make predictions
new_predictions = loaded_model.predict(new_input_tfidf)

# Interpret predictions
for text, prediction in zip(new_input, new_predictions):
    print(f"Input: {text}")
    print(f"Prediction: {'Suggestion' if prediction == 1 else 'Not a Suggestion'}\n")
