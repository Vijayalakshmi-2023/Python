from datetime import datetime

def format_chats(*messages):
    # Get current time in HH:MM format (or use hardcoded if needed)
    timestamp = datetime.now().strftime("[%H:%M]")

    # Lambda to capitalize and add timestamp
    formatter = lambda msg: f"{timestamp} {msg.capitalize()}"

    # Apply formatting to all messages
    formatted = list(map(formatter, messages))
    return formatted

# --- Example Usage ---
chats = format_chats("hello", "how are you?", "i'm doing great", "bye!")

print("🗨️ Formatted Chat Messages:")
for line in chats:
    print(line)
