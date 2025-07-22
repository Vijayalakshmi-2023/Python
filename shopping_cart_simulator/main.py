# main.py

from cart_ops import add_to_cart, remove_from_cart, get_unique_items, checkout
import discounts

# Products in stock
products = {
    101: ("T-shirt", 500, 10),
    102: ("Jeans", 1200, 5),
    103: ("Sneakers", 2000, 3),
    104: ("Cap", 300, 20),
}

# Empty cart
cart = []

# Add items
print(add_to_cart(cart, products, 101, 2))  # 2 T-shirts
print(add_to_cart(cart, products, 102, 1))  # 1 Jeans
print(add_to_cart(cart, products, 104, 3))  # 3 Caps

# Remove item
print(remove_from_cart(cart, 103))  # Not in cart
print(remove_from_cart(cart, 104))  # Remove Caps

# Show unique items
unique_items = get_unique_items(cart)
print(f"\n🛍️ Unique Products in Cart: {unique_items}")

# Checkout
print("\n🧾 Final Bill:")
print(checkout(cart, products, discounts.flat_discount))
