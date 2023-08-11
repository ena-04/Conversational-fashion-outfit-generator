from flask import Flask, render_template, request, jsonify
from bardapi import Bard
import os
from dotenv.main import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Access environment variables
token = os.environ.get("BARD_API_KEY")

# Create a Bard instance
bard = Bard(token=token)

# Create a Flask app instance
app = Flask(__name__)

# Define the index route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_prompt = request.form['user_prompt']

        if user_prompt:
            result = bard.get_answer(user_prompt)
            bard_response = result['content']
            
            lines = bard_response.split('\n')
            filtered_lines = [line for line in lines if not line.startswith("[Image")]
            filtered_response = "\n".join(filtered_lines)
            
            # Integrate recommendation API here
            recommendation_response = get_recommendations(user_prompt)
            
            return render_template('index.html', bard_response=filtered_response, user_prompt=user_prompt, recommendation_response=recommendation_response)

    return render_template('index.html', bard_response=None, user_prompt=None, recommendation_response=None)

def get_recommendations(user_message):
    # Replace this with your actual recommendation logic
    bot_response = "Here are some recommended outfits for: " + user_message
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
