from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key='Keep_API_KEY')

model = genai.GenerativeModel('gemini-1.5-flash')
# Function for generating output from our gemini pro model

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app

st.set_page_config(page_title="Gemini Question answer testing")

st.header("Gemini LLM model by Vaibhav")

input = st.text_input('Input:',key='input')
submit = st.button('Ask your question')

# when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader('Your response is')
    st.write(response)