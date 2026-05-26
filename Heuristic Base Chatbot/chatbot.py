# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! ",
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great ",
        "what is your name": "I'm a simple Python chatbot ",
        "bye": "Goodbye! Have a nice day ",
        "thanks": "You're welcome! th"
    }

    return responses.get(user_input, "Sorry, I don't understand that 🤔")

print("Chatbot is ready! Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot:", chatbot_response("bye"))
        break

    print("Bot:", chatbot_response(user))