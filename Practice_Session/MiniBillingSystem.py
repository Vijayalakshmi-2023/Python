# Mini Billing System

# Step 1: Dictionary of items and their prices
items_prices = {
    "pen": 20,
    "notebook": 50,
    "bag": 700,
    "bottle": 150,
    "calculator": 300
}

# Step 2: List of items selected by the user
selected_items = ["pen", "notebook", "bottle", "bag"]  # Example selection

# Step 3: Calculate total using for loop
total = 0.0
for item in selected_items:
    if item in items_prices:
        total += items_prices[item]
    else:
        print(f"Item '{item}' not found in the store.")

# Step 4: Apply discount if total > 1000
if total > 1000:
    discount = total * 0.10
    total -= discount
    print(f"10% discount applied: ₹{discount:.2f}")
else:
    discount = 0.0

# Step 5: Print the bill
print("\n----- Final Bill -----")
print(f"Items      : {selected_items}")
print(f"Subtotal   : ₹{total + discount:.2f}")
print(f"Discount   : ₹{discount:.2f}")
print(f"Total Bill : ₹{total:.2f}")
print("------------------------")
