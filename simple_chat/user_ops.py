# user_ops.py

def add_user(users, username):
    if username in users:
        return f"⚠️ User '{username}' already exists."
    users.add(username)
    return f"✅ User '{username}' added."

def user_exists(users, username):
    return username in users
