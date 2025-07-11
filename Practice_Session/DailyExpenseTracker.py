# Daily Expense Tracker

# Step 1: Input 7 daily expenses (example list or user input)
expenses = []

print("Enter your expenses for 7 days:")
for i in range(7):
    amount = float(input(f"Day {i+1} expense: ₹"))
    expenses.append(amount)

# Step 2: Calculate total using for loop
total = 0
for expense in expenses:
    total += expense

# Step 3: Suggest savings if total > 3000
print("\n----- Weekly Expense Summary -----")
print(f"Expenses: {expenses}")
print(f"Total spent: ₹{total:.2f}")

if total > 3000:
    print("Advice: Cut down on expenses!")
else:
    print("Good job managing your expenses!")
print("----------------------------------")
