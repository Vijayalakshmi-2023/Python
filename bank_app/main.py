# main.py

from auth import create_account, login
from banking import deposit, withdraw, view_statement, get_unique_transaction_types

# Store users
users = {}

# Create accounts
create_account(users, "user123", 1000)
create_account(users, "user456", 500)

# Login & perform actions
username = input("Enter username to login: ")

if login(users, username):
    print(f"✅ Welcome back, {username}!")
else:
    print(f"❌ User not found. Creating new account for '{username}'...")
    create_account(users, username, 500)
    print("✅ Account created.")

# Actions
deposit(users, username, 300)
withdraw(users, username, 200)
withdraw(users, username, 1000)  # Should fail due to overdraft check

# View statement
view_statement(users, username)

# Show unique transaction types
types = get_unique_transaction_types(users, username)
print("\n🔍 Unique transaction types:", ", ".join(types))
