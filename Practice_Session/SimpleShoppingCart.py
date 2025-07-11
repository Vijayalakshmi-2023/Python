# Simple Shopping Cart

# Step 1: Product dictionary
products = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40,
    "eggs": 60
}

# Step 2: Take user input for 3 items
cart = []
print("Available products:", list(products.keys()))

for i in range(3):
    item = input(f"Enter item {i+1}: ").lower()
    if item in products:
        cart.append(item)
    else:
        print(f"'{item}' is not available.")

# Step 3: Calculate total bill
total = 0
for item in cart:
    total += products[item]

# Step 4: Print final bill
print("\n----- Shopping Cart -----")
print(f"Items selected: {cart}")
print(f"Total bill: ₹{total}")
print("--------------------------")
