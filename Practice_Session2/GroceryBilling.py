# Predefined item-price dictionary
grocery_prices = {
    "rice": 80,
    "wheat": 60,
    "oil": 150,
    "milk": 50,
    "eggs": 6,
    "sugar": 45,
    "tea": 120
}

# List of items selected by the customer
selected_items = ["rice", "milk", "oil", "tea", "sugar"]

# Calculate total using for loop
total = 0
for item in selected_items:
    if item in grocery_prices:
        total += grocery_prices[item]
    else:
        print(f"Warning: {item} not found in price list.")

# Apply discount if total > ₹1000
if total > 1000:
    discount = total * 0.10
    final_total = total - discount
    print(f"Total before discount: ₹{total}")
    print(f"Discount applied: ₹{discount}")
else:
    final_total = total
    print("No discount applied.")

# Output final bill
print(f"Final bill amount: ₹{final_total}")
