# main.py

from expense_ops import add_expense, get_unique_categories
from balance_ops import calculate_balances, show_summary, settle_balances

expenses = []
balances = {}

def main():
    while True:
        print("\n📌 Expense Splitter Menu")
        print("1. Add Expense")
        print("2. Show Balances")
        print("3. Show Unique Categories")
        print("4. Settle Balances")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: ₹"))
            payer = input("Who paid? ")
            participants = input("Enter participants (comma-separated): ").split(",")
            participants = [p.strip() for p in participants]
            category = input("Enter category: ")
            print(add_expense(expenses, amount, payer, participants, category))

        elif choice == "2":
            balances = calculate_balances(expenses)
            print(show_summary(balances))

        elif choice == "3":
            print("📂 Categories used:", get_unique_categories(expenses))

        elif choice == "4":
            print(settle_balances(balances))

        elif choice == "5":
            print("👋 Exiting Expense Splitter.")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
