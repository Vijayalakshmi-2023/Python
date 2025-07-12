# Bank Transaction Logger

transactions = []

def add_transaction():
    try:
        amount = float(input("Enter transaction amount (use - for debit, + for credit): "))
        transactions.append(amount)
        print(f"✅ Transaction recorded: ₹{amount}")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

def view_balance():
    balance = sum(transactions)
    print(f"\n💰 Current Balance: ₹{balance:.2f}")

def show_last_three():
    print("\n🧾 Last 3 Transactions:")
    last_3 = transactions[-3:]
    if not last_3:
        print("No transactions yet.")
    else:
        for i, t in enumerate(last_3, start=1):
            print(f"{i}. ₹{t}")

def remove_transaction():
    try:
        amount = float(input("Enter the exact amount to remove: "))
        if amount in transactions:
            transactions.remove(amount)
            print(f"❌ Removed transaction: ₹{amount}")
        else:
            print("⚠️ Transaction not found.")
    except ValueError:
        print("❌ Invalid input.")

def main():
    while True:
        print("\n🏦 Bank Transaction Logger")
        print("1. Add a transaction")
        print("2. View current balance")
        print("3. Show last 3 transactions")
        print("4. Remove an incorrect transaction")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_balance()
        elif choice == "3":
            show_last_three()
        elif choice == "4":
            remove_transaction()
        elif choice == "5":
            print("👋 Exiting Transaction Logger. Stay financially smart!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
