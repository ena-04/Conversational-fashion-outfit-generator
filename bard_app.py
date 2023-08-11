import streamlit as st
from bardapi import Bard
import os
from dotenv.main import load_dotenv

# Load environment variables
load_dotenv()
token = os.environ.get("BARD_API_KEY")

# Create a Streamlit app title
st.title("Fashion Outfit Designer with Bard API")

# Create a Bard instance
bard = Bard(token=token)

# Create a text input for user prompt
user_prompt = st.text_input("Enter your prompt:")

# If the user enters a prompt, get and display the response
if user_prompt:
    result = bard.get_answer(user_prompt)
    bard_response = result['content']

    # Remove image descriptions from each suggestion
    lines = bard_response.split('\n')
    filtered_lines = [line for line in lines if not line.startswith("[Image")]

    # Join the filtered lines back into a single string
    filtered_response = "\n".join(filtered_lines)

    st.write("Bard Response:", filtered_response)

# Sidebar contents and other layout elements
with st.sidebar:
    st.title('Fashion Outfit Designer Chat')
    st.markdown('''
    ## About
    This app combines Bard API with a fashion outfit designer chatbot built using LangChain.

    ''')

st.header("Your Fashion Outfit Designer 💬")

# Initialize session state lists
if 'user_inputs' not in st.session_state:
    st.session_state.user_inputs = []
if 'generated_responses' not in st.session_state:
    st.session_state.generated_responses = []

# Main loop
if st.session_state.user_inputs:
    for i in range(len(st.session_state.user_inputs)):
        st.write("You:", st.session_state.user_inputs[i])
        st.write("Outfit Designer:", st.session_state.generated_responses[i])
        