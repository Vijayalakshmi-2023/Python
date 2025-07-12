# Simple Banking System

balance = 0.0
transactions = []

# Function to deposit money
def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("❌ Amount must be positive.\n")
            return
        balance += amount
        transactions.append(f"Deposited: ${amount:.2f}")
        print(f"✅ Deposited ${amount:.2f}\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")

# Function to withdraw money
def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("❌ Amount must be positive.\n")
            return
        if amount > balance:
            print("❌ Insufficient balance.\n")
            return
        balance -= amount
        transactions.append(f"Withdrew: ${amount:.2f}")
        print(f"✅ Withdrew ${amount:.2f}\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")

# Function to check current balance
def check_balance():
    print(f"\n💼 Current Balance: ${balance:.2f}\n")

# Function to print transaction history
def show_transactions():
    print("\n=== Transaction History ===")
    if not transactions:
        print("No transactions recorded.\n")
    else:
        for i, t in enumerate(transactions, start=1):
            print(f"{i}. {t}")
    print()

# Main menu loop
def main():
    while True:
        print("=== Simple Banking System ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            show_transactions()
        elif choice == "5":
            print("👋 Thank you for using the banking system!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Run the banking system
main()
