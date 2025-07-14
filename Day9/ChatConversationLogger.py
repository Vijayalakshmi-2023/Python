from datetime import datetime

# Sample chat messages: (timestamp, (sender, message))
chat_history = [
    (datetime(2025, 7, 15, 10, 30, 0), ("Alice", "Hey, how are you?")),
    (datetime(2025, 7, 15, 10, 32, 15), ("Bob", "I'm good! How about you?")),
    (datetime(2025, 7, 15, 10, 35, 0), ("Alice", "I'm doing great, thanks!")),
    (datetime(2025, 7, 15, 10, 40, 10), ("Bob", "Awesome to hear!")),
    (datetime(2025, 7, 15, 10, 45, 5), ("Alice", "By the way, are we meeting later?"))
]

# 1. Use slicing to get recent messages (e.g., last 3 messages)
def get_recent_messages(count=3):
    recent_messages = chat_history[-count:]  # Get the last 'count' messages using slicing
    print(f"Displaying the last {count} messages:\n")
    for timestamp, (sender, message) in recent_messages:
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {sender}: {message}")
    print("-" * 30)

# 2. Display all chat messages using unpacking
def display_all_messages():
    print("Full Chat History:\n")
    for timestamp, (sender, message) in chat_history:
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {sender}: {message}")
    print("-" * 30)

# 3. Prevent edit by immutability: message history is immutable due to tuple structure
def add_message(sender, message):
    # Create a new message with the current timestamp
    timestamp = datetime.now()
    chat_history.append((timestamp, (sender, message)))
    print(f"Message added: [{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {sender}: {message}")
    print("-" * 30)

# Testing the functions
get_recent_messages(3)  # Get the last 3 messages
display_all_messages()  # Display all messages in the chat history
add_message("Bob", "Looking forward to our meeting!")  # Add a new message
get_recent_messages(3)  # Get the last 3 messages again to see the updated history
