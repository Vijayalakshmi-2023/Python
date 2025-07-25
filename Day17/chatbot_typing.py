import time

def chatbot_typing(message, delay=0.1):
    index = 0
    while index < len(message):
        skip = yield message[index]
        if skip == "skip":
            break
        time.sleep(delay)
        index += 1
# Simulate typing for a chatbot message
msg = "Hello! How can I assist you today?"
gen = chatbot_typing(msg)

try:
    while True:
        char = next(gen)
        print(char, end='', flush=True)
except StopIteration:
    pass
gen = chatbot_typing("Typing will be interrupted...")

while True:
    try:
        char = gen.send(None)
        print(char, end='', flush=True)
        user_input = input("\nType 's' to skip typing or Enter to continue: ")
        if user_input.lower() == 's':
            gen.send("skip")
            break
    except StopIteration:
        break
