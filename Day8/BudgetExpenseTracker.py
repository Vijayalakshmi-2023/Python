# Budget Expense Tracker
expenses = []

def show_menu():
    print("\n💰 Budget Expense Tracker")
    print("1. View all expenses")
    print("2. Add a new expense")
    print("3. Update an expense")
    print("4. Remove an expense")
    print("5. Show last 3 expenses")
    print("6. Exit")

def view_expenses():
    if not expenses:
        print("📭 No expenses recorded yet.")
    else:
        print("\n🧾 All Expenses:")
        for idx, amount in enumerate(expenses, 1):
            print(f"{idx}. ₹{amount:.2f}")

def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))
        expenses.append(amount)
        print(f"✅ ₹{amount:.2f} added to your expenses.")
    except ValueError:
        print("❌ Please enter a valid number.")

def update_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to update: ")) - 1
        if 0 <= index < len(expenses):
            new_amount = float(input("Enter new amount: ₹"))
            expenses[index] = new_amount
            print(f"🔄 Expense #{index + 1} updated to ₹{new_amount:.2f}")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ Please enter valid numbers.")

def remove_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to remove: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(f"🗑️ Removed ₹{removed:.2f} from your expenses.")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ Please enter valid numbers.")

def show_last_3():
    print("\n🕒 Last 3 Expenses:")
    if len(expenses) == 0:
        print("No expenses yet.")
    else:
        for amount in expenses[-3:]:
            print(f"- ₹{amount:.2f}")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–6): ")

    if choice == "1":
        view_expenses()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        remove_expense()
    elif choice == "5":
        show_last_3()
    elif choice == "6":
        print("✅ Exiting Budget Tracker. Stay financially smart! 💸")
        break
    else:
        print("❌ Invalid choice. Try again.")
