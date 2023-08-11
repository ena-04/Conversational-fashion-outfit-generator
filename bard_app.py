from bardapi import Bard
import streamlit as st
import streamlit_chat as stc
import os

# Set your Bard API key
os.environ["_BARD_API_KEY"] = "your_api_key"

st.title("Google Bard")

def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    return message

def user_input():
    input_text = st.text_input("Enter Your Prompt:")
    return input_text

if 'generate' not in st.session_state:
    st.session_state['generate'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        stc.message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
        stc.message(st.session_state["generate"][i], key=str(i))
