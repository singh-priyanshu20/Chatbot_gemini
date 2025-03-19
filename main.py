import streamlit as st
import speech_recognition as sr
import pyttsx3
import json
from langchain_utils import generate_response

st.set_page_config(page_title="AI Chatbot with Features", layout="centered")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize voice engine
engine = pyttsx3.init()

# Title & description
st.title("🤖 AI Chatbot with Gemini")
st.write("**Features:** Chat history, voice input/output, personality modes, and more!")

# Select chatbot persona
persona = st.selectbox("Choose a Chatbot Personality:", ["Friendly", "Professional", "Humorous"])

# User input text box
user_input = st.text_input("Enter your question here:")

# 🎙️ **Voice Input Button**
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Could not understand audio")
            return None
        except sr.RequestError:
            st.write("Speech recognition service unavailable")
            return None

if st.button("🎙️ Speak"):
    user_input = voice_input()

# Process chatbot response
if user_input:
    response = generate_response(user_input, persona)
    
    # Save conversation to history
    st.session_state.chat_history.append({"User": user_input, "Bot": response})

    # Display response
    st.write("### 🤖 Chatbot Response:")
    st.write(response)

    # 🔊 **Voice Output**
    if st.button("🔊 Hear Response"):
        engine.say(response)
        engine.runAndWait()

# 🔄 **Chat History Display**
st.write("## 📝 Chat History")
for chat in st.session_state.chat_history:
    st.write(f"**User:** {chat['User']}")
    st.write(f"**Bot:** {chat['Bot']}")
    st.write("---")

# 📤 **Export Chat History**
def export_chat():
    chat_json = json.dumps(st.session_state.chat_history, indent=4)
    return chat_json

st.download_button(
    label="📥 Download Chat History",
    data=export_chat(),
    file_name="chat_history.json",
    mime="application/json"
)
