# Initial empty cart
cart = {}

# Add or update an item
def add_or_update_item(name, quantity, price):
    if name in cart:
        cart[name]["quantity"] += quantity  # Update quantity
    else:
        cart[name] = {"quantity": quantity, "price": price}

# Remove an item
def remove_item(name):
    if name in cart:
        del cart[name]

# Remove out-of-stock items using pop()
def remove_out_of_stock():
    out_of_stock = [item for item, info in cart.items() if info["quantity"] == 0]
    for item in out_of_stock:
        cart.pop(item)

# Calculate total bill
def calculate_total():
    return sum(info["quantity"] * info["price"] for info in cart.values())

# Show highest value item (based on quantity × price)
def highest_value_item():
    if not cart:
        return None
    return max(cart.items(), key=lambda item: item[1]["quantity"] * item[1]["price"])

# Show cart summary
def cart_summary():
    print("\nCart Summary:")
    for item, info in cart.items():
        subtotal = info["quantity"] * info["price"]
        print(f"{item}: {info['quantity']} @ ${info['price']} each = ${subtotal:.2f}")
    print(f"Total Bill: ${calculate_total():.2f}")

# --- Demo Usage ---
add_or_update_item("Laptop", 1, 1200)
add_or_update_item("Headphones", 2, 150)
add_or_update_item("Mouse", 3, 40)
add_or_update_item("USB Cable", 0, 10)  # Will be removed later

print("\nInitial Cart:")
cart_summary()

# Remove out-of-stock items
remove_out_of_stock()

# Show highest value item
item, info = highest_value_item()
print(f"\nHighest Value Item: {item} - ${info['quantity'] * info['price']:.2f}")

# Check if "Mouse" is in cart
print("\nIs 'Mouse' in cart?", "Mouse" in cart)

# Final cart after removing out-of-stock items
cart_summary()
