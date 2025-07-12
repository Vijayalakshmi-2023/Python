import requests

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Basic predefined responses
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "what is your name?": "I am ChatPy, your friendly assistant.",
        "how are you?": "I'm just a program, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "help": "You can say Hi, ask my name, ask me to tell a joke, or say bye to exit."
    }

    if user_input == "tell me a joke":
        joke = fetch_joke()
        return joke if joke else "Sorry, I couldn't fetch a joke right now."

    return responses.get(user_input, "Sorry, I don't understand that. Try 'help'.")

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        joke_data = response.json()
        return f"{joke_data['setup']} ... {joke_data['punchline']}"
    except Exception:
        return None

def main():
    print("=== Simple Chatbot with API ===")
    print("Type your message (type 'bye' to exit):")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    main()
