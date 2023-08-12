import requests
import speech_recognition as sr
import pyttsx3
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access environment variables
bard_api_key = os.environ.get("BARD_API_KEY")

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Function to capture audio and convert it to text
def capture_audio(timeout_seconds=10):  # Increased timeout value
    with sr.Microphone() as source:
        source.energy_threshold = 300  # Adjust this value
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout_seconds)

    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError as e:
        print("Error recognizing audio:", e)
    except sr.RequestError as e:
        print("Error connecting to the Google API:", e)
    return None  # Return None in case of errors


# Function to convert JSON response to speech
def speak_json_response(response_json):
    # Extract relevant information from the JSON response
    # For example, you might assume the response has a key named "text"
    text_to_speak = response_json.get("text", "No text available.")

    # Use pyttsx3 to convert the extracted text to speech
    engine.say(text_to_speak)
    engine.runAndWait()


# Main loop
while True:
    user_voice_input = capture_audio()

    if user_voice_input:
        print("You said:", user_voice_input)

        # Assuming you make a request to the Bard API here and get a JSON response
        # Example JSON response
        response_json = {"text": "This is the text extracted from the JSON response."}

        speak_json_response(response_json)

    # Optional: Add a condition to break the loop
    if user_voice_input and user_voice_input.lower() == "stop":
        break

# Clean up resources
recognizer.close()  # Release microphone resources
engine.stop()  # Stop the text-to-speech engine
