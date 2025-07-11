from datetime import datetime

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    elif 17 <= current_hour < 21:
        return "Good evening"
    else:
        return "Hello"

def greet_user():
    name = input("Enter your name: ")
    greeting = get_greeting()
    print(f"{greeting}, {name}! Hope you're having a great day.")

if __name__ == "__main__":
    greet_user()
