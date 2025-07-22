# banking.py

MIN_BALANCE = 100.0  # Minimum balance required

def deposit(users, username, amount):
    if amount > 0:
        users[username]["balance"] += amount
        users[username]["transactions"].append(("deposit", amount))
        return True
    return False

def withdraw(users, username, amount):
    if amount > 0 and users[username]["balance"] - amount >= MIN_BALANCE:
        users[username]["balance"] -= amount
        users[username]["transactions"].append(("withdraw", amount))
        return True
    return False

def view_statement(users, username):
    print(f"\n💼 Statement for {username}:")
    for t_type, amount in users[username]["transactions"]:
        print(f"{t_type.capitalize():<10} ₹{amount:.2f}")
    print(f"Available Balance: ₹{users[username]['balance']:.2f}")

def get_unique_transaction_types(users, username):
    return set(t_type for t_type, _ in users[username]["transactions"])
