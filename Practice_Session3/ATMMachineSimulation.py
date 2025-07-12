# ATM Simulation

# Constants
USERNAME = "user"
PASSWORD = "1234"
MAX_ATTEMPTS = 3

# Global Variables
balance = 1000.0
transaction_history = []

# Functions
def login():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        if user == USERNAME and pwd == PASSWORD:
            print("Login successful!\n")
            return True
        else:
            attempts += 1
            print(f"Incorrect credentials. Attempts left: {MAX_ATTEMPTS - attempts}\n")
    print("Account locked due to too many failed attempts.\n")
    return False

def show_menu():
    print("=== ATM Menu ===")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

def check_balance():
    print(f"Your current balance is: ${balance:.2f}\n")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.\n")
        else:
            balance += amount
            transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.\n")
    except ValueError:
        print("Invalid amount entered.\n")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.\n")
        elif amount > balance:
            print("Insufficient balance.\n")
        else:
            balance -= amount
            transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.\n")
    except ValueError:
        print("Invalid amount entered.\n")

def show_history():
    if transaction_history:
        print("=== Transaction History ===")
        for transaction in transaction_history:
            print(transaction)
        print()
    else:
        print("No transactions yet.\n")

# Main Program
if login():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_history()
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
