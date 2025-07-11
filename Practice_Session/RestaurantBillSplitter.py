# Restaurant Bill Splitter

# Step 1: Input prices of food items (example or user input)
prices = []

print("Enter prices of food items (enter 0 to stop):")
while True:
    price = float(input("Item price: ₹"))
    if price == 0:
        break
    prices.append(price)

# Step 2: Calculate total using a loop
total = 0
for price in prices:
    total += price

# Step 3: Input number of friends
friends = int(input("\nEnter number of friends to split the bill: "))

# Step 4: Calculate split amount
if friends > 0:
    per_person = total / friends
else:
    per_person = 0

# Step 5: Display results
print("\n----- Bill Summary -----")
print(f"Items: {prices}")
print(f"Total bill: ₹{total:.2f}")
print(f"Friends: {friends}")
if friends > 0:
    print(f"Amount per person: ₹{per_person:.2f}")
else:
    print("Cannot split the bill among 0 friends.")
print("-------------------------")
