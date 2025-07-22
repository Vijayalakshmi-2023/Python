# tracker.py

def add_expense(expenses, date, category, amount):
    expenses.append((date, category, amount))

def get_unique_categories(expenses):
    return set(category for _, category, _ in expenses)

def group_by_category(expenses):
    category_totals = {}
    for _, category, amount in expenses:
        category_totals[category] = category_totals.get(category, 0) + amount
    return category_totals
