import re
import streamlit as st

def chatbot_response(user_input):
    user_input = user_input.lower()

    patterns = {
        r"\b(hi|hello|hey|hola)\b": "Hello there! 👋 How can I help you today?",
        r"\b(how (are|r) you|how's it going)\b": "I'm doing great! How about you?",
        r"\b(what is your name|who are you)\b": "I'm ChatBot — your non-friendly chatbot 🤖",
        r"\b(help|support|assist|problem)\b": "Sure! Please tell me what issue you’re facing.",
        r"\b(thank you|thanks|thx)\b": "You're welcome! 😊",
        r"\b(weather|temperature)\b": "I can’t check the weather right now, but it’s always sunny in my code!",
        r"\b(time)\b": "Check your system clock!",
        r"\b(ok)\b": "Ok,anything else",
        r"\b(bye|exit|quit|goodbye|see you)\b": "Bye! Have a great day! 👋",
        r"\b(joke|funny)\b": "Why did the computer show up at work late? It had a hard drive! 😂",
        r"\b(why)\b": "cause I am a bot",
        r"b(no|nah|nope)\b": "Okay",
        r"\b(yes|yeah|yep|sure)\b": "Great!"
    }

    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response

    return "Hmm, I didn’t quite understand that. Could you try rephrasing?"

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

st.title("Chatbot")
# st.markdown("Chat with a simple **rule-based chatbot** built using **Python + Streamlit + Regex**.")

# Initialize chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("PyBot", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"🧑 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")

# Footer note
st.markdown("---")
st.caption("A simple Chatbot ")
