import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Global variable for storing expenses in memory
expenses = []

# Record a new expense
def record_expense(date, category, amount, description):
    expense = {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }
    expenses.append(expense)
    print(f"Expense of {amount} for '{category}' recorded successfully.")

# Display all recorded expenses
def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        df = pd.DataFrame(expenses)
        print(df)

# Generate a spending report (total amount spent per category)
def generate_report():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    df = pd.DataFrame(expenses)
    report = df.groupby("Category").agg({"Amount": "sum"}).sort_values("Amount", ascending=False)
    print("\nSpending Report:")
    print(report)

# Track monthly budget and compare it with total expenses
def track_monthly_budget(budget):
    if not expenses:
        print("No expenses recorded yet.")
        return

    df = pd.DataFrame(expenses)
    df["Month"] = pd.to_datetime(df["Date"]).dt.month
    monthly_expenses = df.groupby("Month")["Amount"].sum()
    
    print("\nMonthly Expenses vs Budget:")
    for month, total in monthly_expenses.items():
        status = "Over Budget" if total > budget else "Within Budget"
        print(f"Month {month}: {total} | Status: {status}")

# Visualize expenses using a simple pie chart
def visualize_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    df = pd.DataFrame(expenses)
    category_spending = df.groupby("Category")["Amount"].sum()

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(category_spending, labels=category_spending.index, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    plt.axis('equal')
    plt.show()

# Export expenses to a spreadsheet (Excel or CSV)
def export_to_spreadsheet(filename="expenses.xlsx"):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    df = pd.DataFrame(expenses)
    
    # Export to Excel or CSV based on file extension
    if filename.endswith(".xlsx"):
        df.to_excel(filename, index=False, engine='openpyxl')
    else:
        df.to_csv(filename, index=False)

    print(f"Data exported to {filename}")

# Main function for running the program
def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Record an expense")
        print("2. Display all expenses")
        print("3. Generate spending report")
        print("4. Track monthly budget")
        print("5. Visualize expenses")
        print("6. Export data to a spreadsheet")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Record a new expense
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Transportation, etc.): ")
            amount = float(input("Enter amount: "))
            description = input("Enter a description (optional): ")

            record_expense(date, category, amount, description)

        elif choice == '2':
            display_expenses()

        elif choice == '3':
            generate_report()

        elif choice == '4':
            budget = float(input("Enter your monthly budget: "))
            track_monthly_budget(budget)

        elif choice == '5':
            visualize_expenses()

        elif choice == '6':
            filename = input("Enter the filename to export (e.g., expenses.xlsx or expenses.csv): ")
            export_to_spreadsheet(filename)

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
