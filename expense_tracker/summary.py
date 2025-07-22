# summary.py

from collections import defaultdict

def monthly_summary(expenses):
    month_totals = defaultdict(float)
    for date, _, amount in expenses:
        month = date[:7]  # 'YYYY-MM'
        month_totals[month] += amount
    return dict(month_totals)

def print_summary_by_category(grouped):
    print("\nExpense Summary by Category:")
    for cat, amt in grouped.items():
        print(f"{cat:<15}: ₹{amt:.2f}")

def print_monthly_summary(monthly):
    print("\nMonthly Summary:")
    for month, total in monthly.items():
        print(f"{month:<10}: ₹{total:.2f}")
