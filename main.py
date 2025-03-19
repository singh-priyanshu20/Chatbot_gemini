import streamlit as st
from langchain_utils import generate_response

st.set_page_config(page_title="LangChain Gemini Chatbot", layout="centered")

st.title("🤖 LangChain Demo with Gemini")
st.write("Powered by Google Gemini & LangChain")

# User Input
input_text = st.text_input("Enter your question here:")

# Display Response
if input_text:
    response = generate_response(input_text)
    st.write("### 🤖 Chatbot Response:")
    st.write(response)
