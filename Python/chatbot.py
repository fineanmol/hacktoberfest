import random

# Define responses for the chatbot
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm functioning well. How about you?",
    "what is your name": "I'm just a chatbot, so I don't have a name. You can call me ChatGPT.",
    "bye": "Goodbye! If you have more questions in the future, feel free to ask."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Look for a response in the dictionary, or default to a generic response
    response = responses.get(user_input, "I'm not sure how to respond to that.")

    return response

print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    
    response = chatbot_response(user_input)
    print("Chatbot:", response)
