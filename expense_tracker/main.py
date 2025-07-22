# main.py

from tracker import add_expense, get_unique_categories, group_by_category
from summary import monthly_summary, print_summary_by_category, print_monthly_summary
from validator import validate_date, validate_amount

# Expense list
expenses = []

# Sample data
add_expense(expenses, "2025-07-01", "Food", 250)
add_expense(expenses, "2025-07-03", "Transport", 100)
add_expense(expenses, "2025-07-03", "Food", 150)
add_expense(expenses, "2025-06-28", "Shopping", 1200)
add_expense(expenses, "2025-06-01", "Food", 300)

# Input simulation with validation
print("Add your own expense:")
date = input("Enter date (YYYY-MM-DD): ")
category = input("Enter category: ")
amount_str = input("Enter amount: ")

if validate_date(date) and validate_amount(amount_str):
    add_expense(expenses, date, category, float(amount_str))
    print("Expense added successfully!")
else:
    print("Invalid input. Expense not added.")

# Group by category
grouped = group_by_category(expenses)
print_summary_by_category(grouped)

# Monthly summary
monthly = monthly_summary(expenses)
print_monthly_summary(monthly)

# Unique categories
print("\nUnique Categories Used:")
print(", ".join(get_unique_categories(expenses)))

