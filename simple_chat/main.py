# main.py

from user_ops import add_user, user_exists
from chat_ops import send_message, view_chat, delete_chat

users = set()
chat_logs = {}

# Sample interaction loop
print("📲 Simple CLI Chat App\n")

# Add users
print(add_user(users, "alice"))
print(add_user(users, "bob"))
print(add_user(users, "charlie"))

# Chat operations
print(send_message(chat_logs, "alice", "bob", "Hey Bob!"))
print(send_message(chat_logs, "bob", "alice", "Hey Alice, what's up?"))
print(send_message(chat_logs, "charlie", "alice", "Hello Alice!"))

# View chats
print("\n🔍 Alice & Bob's chat:")
print(view_chat(chat_logs, "alice", "bob"))

print("\n🔍 Alice & Charlie's chat:")
print(view_chat(chat_logs, "alice", "charlie"))

# Delete chat
print("\n🗑️ Deleting Alice & Bob's chat...")
print(delete_chat(chat_logs, "alice", "bob"))

# View after deletion
print("\n🔍 Alice & Bob's chat:")
print(view_chat(chat_logs, "alice", "bob"))
