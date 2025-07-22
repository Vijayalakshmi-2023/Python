# expense_ops.py

def add_expense(expenses, amount, payer, participants, category):
    expense = {
        "amount": amount,
        "payer": payer,
        "participants": set(participants),
        "category": category
    }
    expenses.append(expense)
    return f"✅ Expense of ₹{amount} added under '{category}' by {payer}."

def get_unique_categories(expenses):
    return {e["category"] for e in expenses}
