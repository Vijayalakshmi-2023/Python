class InvalidCategoryError(Exception):
    """Raised when an invalid category is entered."""
    pass

def expense_tracker():
    allowed_categories = {"food", "transport", "utilities", "entertainment", "others"}
    expenses = []
    total = 0.0

    print("💰 Expense Tracker (type 'done' to finish)\nAllowed categories: food, transport, utilities, entertainment, others\n")

    try:
        while True:
            category = input("Enter category: ").strip().lower()
            if category == "done":
                break

            if category not in allowed_categories:
                raise InvalidCategoryError(f"'{category}' is not a valid category.")

            amount_input = input(f"Enter expense amount for {category}: ").strip()
            try:
                amount = float(amount_input)
                if amount < 0:
                    raise ValueError("Amount cannot be negative.")
            except ValueError as ve:
                print(f"❌ Invalid amount: {ve}")
                continue

            expenses.append((category, amount))
            total += amount

    except InvalidCategoryError as ice:
        print(f"❌ Category Error: {ice}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
    finally:
        print("\n📊 Summary:")
        print(f"Total Expenses: ₹{total:.2f}")
        category_totals = {}
        for cat, amt in expenses:
            category_totals[cat] = category_totals.get(cat, 0) + amt
        for cat, amt in category_totals.items():
            print(f"{cat.title()}: ₹{amt:.2f}")

# Run the tracker
if __name__ == "__main__":
    expense_tracker()
