# Sample product inventory as a list of tuples (product_id, name, price, in_stock)
inventory = [
    (101, "Laptop", 1200.99, 10),
    (102, "Smartphone", 799.99, 25),
    (103, "Headphones", 199.99, 50),
    (104, "Tablet", 499.99, 15),
    (105, "Smartwatch", 199.99, 30),
    (106, "Keyboard", 79.99, 0),   # Out of stock
    (107, "Mouse", 49.99, 100)
]

# 1. Calculate the total inventory value
def total_inventory_value():
    total_value = 0
    for product in inventory:
        price, in_stock = product[2], product[3]
        total_value += price * in_stock
    return total_value

# 2. Filter products that are in stock
def products_in_stock():
    in_stock_products = [product for product in inventory if product[3] > 0]
    return in_stock_products

# 3. Sort products by price (ascending order)
def sort_products_by_price():
    sorted_inventory = sorted(inventory, key=lambda x: x[2])  # Sort by price (x[2] is the price)
    return sorted_inventory

# 4. Print detailed reports (unpack tuple values)
def print_product_report():
    print("\nProduct Report:")
    for product in inventory:
        product_id, name, price, in_stock = product
        print(f"Product ID: {product_id}, Name: {name}, Price: ${price:.2f}, In Stock: {in_stock}")

# Testing the functions
print(f"Total Inventory Value: ${total_inventory_value():,.2f}")

print("\nProducts In Stock:")
in_stock = products_in_stock()
for product in in_stock:
    product_id, name, price, in_stock_qty = product
    print(f"{name} (Product ID: {product_id}) - Price: ${price:.2f}, In Stock: {in_stock_qty}")

print("\nSorted Products by Price:")
sorted_inventory = sort_products_by_price()
for product in sorted_inventory:
    product_id, name, price, in_stock_qty = product
    print(f"{name} - ${price:.2f}")

print_product_report()
