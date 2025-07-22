# chat_ops.py

def get_chat_key(user1, user2):
    return tuple(sorted((user1, user2)))

def send_message(logs, sender, receiver, message):
    key = get_chat_key(sender, receiver)
    if key not in logs:
        logs[key] = []
    logs[key].append(f"{sender}: {message}")
    return "📨 Message sent."

def view_chat(logs, user1, user2):
    key = get_chat_key(user1, user2)
    if key in logs and logs[key]:
        return "\n".join(logs[key])
    return "💬 No messages yet."

def delete_chat(logs, user1, user2):
    key = get_chat_key(user1, user2)
    if key in logs:
        del logs[key]
        return "🗑️ Chat deleted."
    return "❌ No chat to delete."
