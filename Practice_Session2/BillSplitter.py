# Input total bill and number of friends
total_bill = float(input("Enter the total bill amount: "))
num_friends = int(input("Enter the number of friends: "))

# Check if number of friends is at least 1
if num_friends >= 1:
    per_head = total_bill / num_friends  # Variable for calculation
    print(f"Each friend should contribute: ₹{per_head:.2f}")
else:
    print("❌ Error: Number of friends must be at least 1.")
