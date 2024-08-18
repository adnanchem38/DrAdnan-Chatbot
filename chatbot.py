import google.generativeai as genai
import streamlit as st
GOOGLE_API_KEY = "AIzaSyBLUmI6VCB2gmq6BCcZcwDRK9gRw23akDs"

genai.configure(api_key=GOOGLE_API_KEY)

# Model Initiate

model = genai.GenerativeModel('gemini-1.5-flash')

def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

st.title("Dr Adnan streamlitChatBot")
st.write("It uses GOOGLE API Key") 

# user_input = input("enter your prompt = ")
# output = getResponseFromModel(user_input)

# print(output)

with st.form(key="chat_form, clear_on_submit=true"):
    user_input = st.text_input("", max_chars=2000, label_visibility="collapsed")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.write(response)
        else:
            st.warning("please enter a prompt")