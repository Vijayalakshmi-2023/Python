# Grocery Basket Price Calculator

# Step 1: Dictionary of grocery items with prices
grocery_prices = {
    "rice": 80,
    "wheat": 60,
    "milk": 50,
    "bread": 30,
    "eggs": 70,
    "oil": 120,
    "sugar": 40,
    "tea": 90
}

# Step 2: User-selected grocery items (sample list)
selected_items = ["milk", "bread", "eggs", "oil", "sugar", "tea"]  # 6 items

# Step 3: Calculate total using for loop
total = 0
for item in selected_items:
    if item in grocery_prices:
        total += grocery_prices[item]
    else:
        print(f"Item '{item}' not found in the store.")

# Step 4: Apply ₹50 discount if more than 5 items
discount = 0
if len(selected_items) > 5:
    discount = 50
    total -= discount

# Step 5: Print final bill
print("\n----- Grocery Basket Bill -----")
print(f"Items       : {selected_items}")
print(f"Subtotal    : ₹{total + discount}")
print(f"Discount    : ₹{discount}")
print(f"Total Price : ₹{total}")
print("--------------------------------")
