from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/api/recommendations', methods=['POST'])
@cross_origin(origin='*')
def get_recommendations():
    user_message = request.json['userMessage']
    # Replace this with your Gen AI integration logic
    app.logger.warning("A warning message.")
    bot_response = "Here are some recommended outfits!"
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
