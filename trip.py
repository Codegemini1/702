import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key='.....')

model = genai.GenerativeModel('gemini-1.5-flash')
# Function for generating output from our gemini pro model

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

def generate_trip_plan(duration,destination,style):
    prompt = f'Create a {duration} day trip plan for {destination} focusing on {style} travel. Include daily activities , must see attraction and also suggest stay plans.'
    response = model.generate_content(prompt)
    return response.text 

# Streamlit application

st.set_page_config(page_title = 'AI trip planner')

st.header('AI trip planner by VAIBHAV')

duration = st.number_input('Trip Duration (days)', min_value=1, step=1)
destination = st.text_input('Trip Destination')
style = st.selectbox('Trip Style',['Adventure', 'Relaxation', 'Cultural'])

submit = st.button('Generate trip plan')

trip_plan = None
if submit:
    trip_plan = generate_trip_plan(duration,destination,style) 
    
if trip_plan:
    st.subheader('Your trip plan')
    st.write(trip_plan)   