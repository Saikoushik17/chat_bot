def respond_to_query(query):
    query = query.lower()
    if "hello" in query:
        return "Hi there! How can I help you today?"
    elif "how are you" in query:
        return "I'm just a bot, but I'm doing great! How can I assist you?"
    elif "your name" in query:
        return "I'm a simple chatbot created to help you with basic queries."
    elif "bye" in query:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Can you please rephrase?"

def chatbot():
    print("Welcome to the simple chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = respond_to_query(user_input)
        print(f"Bot: {response}")
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chatbot()
