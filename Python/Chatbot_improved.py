import re
import streamlit as st

def chatbot_response(user_input):
    user_input = user_input.lower()

    patterns = {
        # Basic greetings and conversation
        r"\b(hi|hello|hey|hola)\b": "Hello there! 👋 How can I help you today?",
        r"\b(how (are|r) you|how's it going)\b": "I'm doing great! Thanks for asking. How about you?",
        r"\b(what is your name|who are you)\b": "I'm ChatBot — your friendly AI assistant! 🤖",
        r"\b(help|support|assist|problem)\b": "I'll do my best to help! What specific issue are you facing?",
        r"\b(thank you|thanks|thx)\b": "You're welcome! Let me know if you need anything else! 😊",
        
        # Programming related queries
        r"\b(what is python|python)\b": "Python is a high-level, interpreted programming language known for its simplicity and readability. Great for beginners! 🐍",
        r"\b(programming language|which language)\b": "There are many programming languages! Popular ones include Python, JavaScript, Java, C++. The best one depends on your needs!",
        r"\b(learn (coding|programming))\b": "Great choice! I recommend starting with Python or JavaScript. Check out resources like freeCodeCamp, Codecademy, or The Odin Project!",
        r"\b(git|github)\b": "Git is a version control system, and GitHub is a platform for hosting code. Essential tools for every developer! 📚",
        
        # Fun responses
        r"\b(weather|temperature)\b": "I can't check the weather right now, but it's always sunny in my code! ☀️",
        r"\b(time)\b": "Time to code! (But also check your system clock 😉)",
        r"\b(joke|funny)\b": "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
        r"\b(another joke)\b": "What did the Java code say to the C code? You've got no class! 🤣",
        
        # Technical terms
        r"\b(api|apis)\b": "API (Application Programming Interface) allows different software applications to communicate with each other.",
        r"\b(framework)\b": "A framework is a pre-built structure that helps developers build applications more efficiently.",
        r"\b(database|db)\b": "A database is an organized collection of data stored electronically. Common ones include MySQL, PostgreSQL, MongoDB.",
        
        # General responses
        r"\b(ok|okay)\b": "Great! Anything else you'd like to know?",
        r"\b(bye|exit|quit|goodbye|see you)\b": "Goodbye! Happy coding! 👋",
        r"\b(why)\b": "That's a good question! Could you be more specific?",
        r"\b(no|nah|nope)\b": "Alright! Let me know if you need anything else!",
        r"\b(yes|yeah|yep|sure)\b": "Excellent! What would you like to know?"
    }

    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response

    return "Hmm, I didn't quite understand that. Could you try rephrasing?"

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

st.title("Chatbot")
st.markdown("A simple rule-based coding assistant that can answer basic programming questions! 🚀")

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
st.caption("A simple Chatbot that helps with programming concepts and technical queries! 💻")
