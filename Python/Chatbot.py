import re
import streamlit as st
from datetime import datetime

# ------------------------------
# 💬 Chatbot Response Function
# ------------------------------
def chatbot_response(user_input):
    """Generate a chatbot response using regex pattern matching."""
    user_input = user_input.lower().strip()

    patterns = {
        r"\b(hi|hello|hey|hola)\b": "Hello there! 👋 How can I help you today?",
        r"\b(how (are|r) you|how's it going)\b": "I'm doing great! Thanks for asking 😊 How about you?",
        r"\b(what is your name|who are you)\b": "I'm PyBot 🤖 — your friendly chatbot!",
        r"\b(help|support|assist|problem)\b": "Sure! Please tell me what issue you’re facing. 🛠️",
        r"\b(thank you|thanks|thx)\b": "You're most welcome! 🙏",
        r"\b(weather|temperature)\b": "I can’t check the weather right now, but it’s always sunny in my code! ☀️",
        r"\b(time)\b": f"The current time is {datetime.now().strftime('%I:%M %p')} 🕒",
        r"\b(ok|okay|fine)\b": "Okay! 👍 Anything else?",
        r"\b(bye|exit|quit|goodbye|see you)\b": "Bye! 👋 Have a fantastic day!",
        r"\b(joke|funny)\b": "😂 Why did the computer show up at work late? It had a hard drive!",
        r"\b(why)\b": "Because that's how my developer coded me 🤖",
        r"\b(no|nah|nope)\b": "Alright, no worries 🙂",
        r"\b(yes|yeah|yep|sure)\b": "Great! Let's continue 🚀"
    }

    # Match input with regex patterns
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response

    # Default response
    return "Hmm 🤔, I didn’t quite get that. Could you please rephrase?"

# ------------------------------
# ⚙️ Streamlit Page Config
# ------------------------------
st.set_page_config(page_title="PyBot Chat", page_icon="🤖", layout="centered")

# ------------------------------
# 🧠 Chat History Initialization
# ------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------------
# 🧾 App Title
# ------------------------------
st.markdown("<h1 style='text-align:center;'>🤖 PyBot - Your Mini Chat Assistant</h1>", unsafe_allow_html=True)
st.caption("A simple rule-based chatbot built using Python + Streamlit + Regex")

st.divider()

# ------------------------------
# 💬 Chat Input Area
# ------------------------------
user_input = st.chat_input("Type your message here...")

# If user sends a message
if user_input:
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("PyBot", response))

# ------------------------------
# 🗨️ Display Chat History
# ------------------------------
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(
            f"<div style='background-color:#DCF8C6;padding:10px;border-radius:10px;margin:5px 0;'><b>🧑 You:</b> {message}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#E6E6FA;padding:10px;border-radius:10px;margin:5px 0;'><b>🤖 PyBot:</b> {message}</div>",
            unsafe_allow_html=True
        )

# ------------------------------
# 🧹 Clear Chat Button
# ------------------------------
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()

st.divider()

# ------------------------------
# 📜 Footer
# ------------------------------
st.markdown("<center>Built with ❤️ using <b>Streamlit</b></center>", unsafe_allow_html=True)
