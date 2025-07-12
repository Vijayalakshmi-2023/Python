# Expense Tracker with Categories

# List to store expenses
expenses = []

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.\n")
            return
        category = input("Enter category (e.g., Food, Rent, Utilities): ").strip().capitalize()
        expenses.append({"amount": amount, "category": category})
        print(f"✅ Added: ${amount:.2f} under '{category}'\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

# Function to show all expenses
def show_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n=== All Expenses ===")
    for i, item in enumerate(expenses, start=1):
        print(f"{i}. ${item['amount']:.2f} - {item['category']}")
    print()

# Function to show total spent
def show_total():
    total = sum(item['amount'] for item in expenses)
    print(f"\n💰 Total Spent: ${total:.2f}\n")

# Function to show category-wise totals
def show_category_totals():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    category_totals = {}
    for item in expenses:
        cat = item['category']
        category_totals[cat] = category_totals.get(cat, 0) + item['amount']
    
    print("\n=== Category-wise Totals ===")
    for cat, total in category_totals.items():
        print(f"{cat}: ${total:.2f}")
    print()

# Main menu loop
def main():
    while True:
        print("=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Spent")
        print("4. Show Category Totals")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_category_totals()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

# Run the program
main()
