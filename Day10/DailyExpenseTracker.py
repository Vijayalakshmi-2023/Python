# Format: {date: {"food": amt, "transport": amt, "misc": amt}}
expenses = {
    "2025-07-01": {"food": 180, "transport": 50, "misc": 20},
    "2025-07-02": {"food": 250, "transport": 40, "misc": 30},
    "2025-07-03": {"food": 120, "transport": 70, "misc": 60},
    "2025-07-04": {"food": 300, "transport": 50, "misc": 25}
}
# Calculate daily totals
def daily_totals():
    print("\nDaily Totals:")
    for date, categories in expenses.items():
        total = sum(categories.values())
        print(f"  {date}: ₹{total}")

# Calculate monthly total
def monthly_total():
    return sum(sum(categories.values()) for categories in expenses.values())

#Filter days with highest spending
def highest_spending_day():
    return max(expenses.items(), key=lambda item: sum(item[1].values()))

#Copy and update structure for a new month
def new_month_template():
    # Copying structure but resetting values
    return {date.replace("2025-07", "2025-08"): {"food": 0, "transport": 0, "misc": 0}
            for date in expenses}

#Days with food expenses > 200 using dict comprehension
def high_food_days():
    return {date: data["food"] for date, data in expenses.items() if data["food"] > 200}
# Daily totals
daily_totals()

# Monthly total
print("\nMonthly Total: ₹", monthly_total())

# Highest spending day
high_day, data = highest_spending_day()
print(f"\nHighest Spending Day: {high_day} - ₹{sum(data.values())}")

# Copy structure for new month
august_expenses = new_month_template()
print("\nNew Month Template (August):", august_expenses)

# Days where food > 200
print("\nDays with food expense > ₹200:", high_food_days())
