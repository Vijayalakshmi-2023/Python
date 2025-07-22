# auth.py

def login(users, username):
    return username in users

def create_account(users, username, initial_balance=0.0):
    if username in users:
        return False
    users[username] = {
        "balance": float(initial_balance),
        "transactions": []
    }
    return True
