import streamlit as st
import random
import time

# Sample questions data
questions = [
    {
        "question": "Who invented Git?",
        "answer": "Linus Torvalds",
        "difficulty": "medium",
        "hint": "Also the founder of the Linux distribution system."
    },
    {
        "question": "What was the first name of Google?",
        "answer": "Backrub",
        "difficulty": "hard",
        "hint": "Rubbing your back in a word."
    },
    {
        "question": "What is WWW?",
        "answer": "World Wide Web",
        "difficulty": "easy",
        "hint": "World _ _ _ _ web."
    }
]

# Function to choose questions based on difficulty
def choose_question(questions, difficulty):
    return [question for question in questions if question['difficulty'] == difficulty]

# Function to display the current question
def display_question(questions, current_question, timer=10):
    question_list = questions[current_question]
    question = question_list['question']
    answer = question_list['answer']
    hint = question_list['hint']

    st.subheader(f"Question {current_question + 1}: {question}")
    user_answer = st.text_input("Your answer:")

    if st.button("Submit Answer"):
        if user_answer.strip().lower() == answer.lower():
            st.success("Correct!")
            st.session_state.score += 2 if not st.session_state.hint_used else 1
        else:
            st.error("Incorrect! The correct answer was: " + answer)
        
        st.session_state.current_question += 1  # Move to the next question
        st.session_state.hint_used = False  # Reset hint usage
        st.session_state.start_time = time.time()  # Reset timer

    if st.button("Get Hint") and not st.session_state.hint_used:
        st.info(f"Hint: {hint}")
        st.session_state.hint_used = True

    # Timer
    elapsed_time = time.time() - st.session_state.start_time
    remaining_time = timer - int(elapsed_time)
    st.write(f"Time remaining: {remaining_time} seconds")

    # Check if time has run out
    if remaining_time <= 0:
        st.error("Time's up! The correct answer was: " + answer)
        st.session_state.current_question += 1
        st.session_state.start_time = time.time()

# Main application code
st.title("Quiz Challenge")

# Initialize session state variables
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'hint_used' not in st.session_state:
    st.session_state.hint_used = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Difficulty selection and quiz start
difficulty = st.selectbox("Choose a difficulty", ["easy", "medium", "hard"])
if st.button("Start Quiz"):
    selected_flashcards = choose_question(questions, difficulty)
    random.shuffle(selected_flashcards)
    st.session_state.flashcards = selected_flashcards
    st.session_state.score = 0
    st.session_state.current_question = 0
    st.session_state.hint_used = False
    st.session_state.start_time = time.time()

# Quiz questions display
if "flashcards" in st.session_state:
    if st.session_state.current_question < len(st.session_state.flashcards):
        display_question(st.session_state.flashcards, st.session_state.current_question)
    else:
        st.write(f"Quiz Over! Your final score is {st.session_state.score}")
        if st.button("Play Again"):
            st.session_state.clear()
