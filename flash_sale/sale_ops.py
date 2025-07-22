# sale_ops.py

from datetime import datetime

products = {
    "P001": {"name": "Headphones", "price": 2000, "stock": 10},
    "P002": {"name": "Keyboard", "price": 1500, "stock": 15},
    "P003": {"name": "Mouse", "price": 500, "stock": 30},
}

sales = []

def apply_discount(price, quantity):
    if quantity >= 5:
        return price * 0.8  # 20% discount
    elif quantity >= 3:
        return price * 0.9  # 10% discount
    return price

def make_sale(product_code, buyer_name, quantity):
    if product_code not in products:
        return "❌ Product code not found."

    product = products[product_code]

    if product["stock"] < quantity:
        return "❌ Not enough stock."

    discounted_price = apply_discount(product["price"], quantity)
    product["stock"] -= quantity
    sales.append((product_code, buyer_name, quantity, datetime.now().isoformat()))
    return f"✅ Sold {quantity} x {product['name']} to {buyer_name} at ₹{discounted_price * quantity:.2f}"
