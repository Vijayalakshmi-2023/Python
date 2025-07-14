# Sample bank account data stored as a list of tuples
# Each tuple stores: (account_number, name, (balance, status))
bank_accounts = [
    (101, "Anu", (1000.50, "Active")),
    (102, "Banu", (1500.75, "Active")),
    (103, "Charu", (300.25, "Suspended")),
    (104, "Deva", (1200.10, "Active")),
    (105, "Elan", (0.00, "Inactive"))
]

# 1. Display all customer data
def display_accounts():
    for account in bank_accounts:
        account_number, name, (balance, status) = account
        print(f"Account Number: {account_number}, Name: {name}, Balance: ${balance:.2f}, Status: {status}")

# 2. Access customer data using indexing
def access_account(account_number):
    for account in bank_accounts:
        if account[0] == account_number:
            account_number, name, (balance, status) = account
            print(f"\nAccount Number: {account_number}")
            print(f"Name: {name}")
            print(f"Balance: ${balance:.2f}")
            print(f"Status: {status}")
            return
    print(f"\nAccount with number {account_number} not found.")

# 3. Unpack customer data for a report
def generate_report():
    print("\nGenerating Account Report...")
    for account in bank_accounts:
        account_number, name, (balance, status) = account
        print(f"Customer Report: {name} (Account: {account_number}) - Balance: ${balance:.2f}, Status: {status}")

# 4. Prevent Changes by Using Immutability
def try_to_modify_account(account_number, new_balance):
    for index, account in enumerate(bank_accounts):
        if account[0] == account_number:
            # Attempting to modify a tuple will result in an error because tuples are immutable
            try:
                # This will raise an error because we cannot modify a tuple directly
                bank_accounts[index] = (account[0], account[1], (new_balance, account[2][1]))
            except TypeError as e:
                print(f"\nError: {e}. Tuples are immutable, so the account cannot be modified.")
            return
    print(f"\nAccount with number {account_number} not found.")

# Testing the functions
display_accounts()
access_account(102)  # Accessing account for Bob
generate_report()  # Generating the report
try_to_modify_account(101, 2000.00)  # Trying to modify Alice's balance (which will fail)
