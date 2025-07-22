# cart_ops.py

def add_to_cart(cart, products, product_id, quantity):
    if product_id not in products:
        return "❌ Product not found."
    name, price, stock = products[product_id]
    if quantity > stock:
        return f"⚠️ Only {stock} items left in stock."
    cart.append((product_id, quantity))
    return f"✅ Added {quantity} x {name} to cart."

def remove_from_cart(cart, product_id):
    for i, (pid, _) in enumerate(cart):
        if pid == product_id:
            del cart[i]
            return "🗑️ Item removed from cart."
    return "❌ Item not found in cart."

def get_unique_items(cart):
    return {pid for pid, _ in cart}

def calculate_total(cart, products):
    total = 0
    for pid, qty in cart:
        price = products[pid][1]
        total += price * qty
    return total

def checkout(cart, products, discount_fn):
    bill_lines = []
    total = calculate_total(cart, products)
    discounted_total = discount_fn(total)
    for pid, qty in cart:
        name, price, _ = products[pid]
        line = f"{name} x {qty} = ₹{price * qty:.2f}"
        bill_lines.append(line)

    summary = "\n".join(bill_lines)
    summary += f"\n\nSubtotal: ₹{total:.2f}"
    summary += f"\nDiscounted Total: ₹{discounted_total:.2f}"
    return summary
