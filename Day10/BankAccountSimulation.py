# Format: {account_number: {"name": ..., "balance": ...}}
accounts = {
    1001: {"name": "Alice", "balance": 5000},
    1002: {"name": "Bob", "balance": 1200},
    1003: {"name": "Charlie", "balance": 850},
    1004: {"name": "David", "balance": 2500},
}
# Deposit funds into an account
def deposit(account_number, amount):
    account = accounts.get(account_number)
    if account:
        account["balance"] += amount
        print(f"Deposited {amount} into account {account_number}. New balance: {account['balance']}")
    else:
        print(f"Account {account_number} not found.")

# Withdraw funds from an account
def withdraw(account_number, amount):
    account = accounts.get(account_number)
    if account:
        if account["balance"] >= amount:
            account["balance"] -= amount
            print(f"Withdrew {amount} from account {account_number}. New balance: {account['balance']}")
        else:
            print(f"Insufficient balance in account {account_number}.")
    else:
        print(f"Account {account_number} not found.")

# Flag low-balance accounts (< 1000)
def flag_low_balance_accounts():
    low_balance_accounts = {acc_num: data for acc_num, data in accounts.items() if data["balance"] < 1000}
    print("\nLow-Balance Accounts (< 1000):")
    if low_balance_accounts:
        for acc_num, data in low_balance_accounts.items():
            print(f"  Account {acc_num} ({data['name']}) - Balance: {data['balance']}")
    else:
        print("No accounts with low balance.")
# Deposit and withdraw funds
deposit(1001, 500)    # Deposit into Alice's account
withdraw(1002, 300)   # Withdraw from Bob's account
withdraw(1003, 1000)  # Attempt to withdraw more than Charlie's balance

# Flag low-balance accounts
flag_low_balance_accounts()
