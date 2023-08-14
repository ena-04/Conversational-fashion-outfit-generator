from flask import Flask, render_template, request, jsonify
from bardapi import Bard
import os
from dotenv.main import load_dotenv
import sys


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


def bold_text(text):
    text1 = text.replace(" **", " <b>")
    text2 = text1.replace("** ", "</b> ")
    return text2


def get_recommendations(user_message):
    # Replace this with your actual recommendation logic
    bot_response = "Here are some recommended outfits for: " + user_message
    return bot_response


@app.route("/api/recommendations", methods=["POST"])
@cross_origin(origin="*")
def get_recommendations():
    user_message = request.json["userMessage"]
    # Replace this with your Gen AI integration logic

    if user_message:
        result = bard.get_answer(
            user_message
        )
        print(result)
        bard_response = result["content"]

        lines = bard_response.split("\n")
        filtered_lines = [line for line in lines if not line.startswith("[Image")]
        filtered_response = "\n".join(filtered_lines)

    app.logger.warning("A warning message.")
    bot_response = bold_text(filtered_response)
    return jsonify({"bot_response": bot_response})


if __name__ == "__main__":
    app.run(debug=True)
