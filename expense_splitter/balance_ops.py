# balance_ops.py

from collections import defaultdict

def calculate_balances(expenses):
    balances = defaultdict(float)

    for exp in expenses:
        split_amount = exp["amount"] / len(exp["participants"])
        for person in exp["participants"]:
            balances[person] -= split_amount
        balances[exp["payer"]] += exp["amount"]
    
    return dict(balances)

def show_summary(balances):
    summary = "\n💰 Balance Summary:\n"
    for name, bal in balances.items():
        status = "owes" if bal < 0 else "is owed"
        summary += f"{name}: {status} ₹{abs(bal):.2f}\n"
    return summary

def settle_balances(balances):
    print("⚖️ Settling balances (simplified)...")
    for name in balances:
        balances[name] = 0.0
    return "✅ Balances settled."
