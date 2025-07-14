# Sample e-commerce order data as a list of tuples (order_id, customer_name, (items in order))
orders = [
    (101, "Anu", ("Laptop", "Mouse", "Headphones")),
    (102, "Banu", ("Smartphone", "Charger", "Headphones")),
    (103, "Charu", ("Tablet", "Keyboard", "Stylus")),
    (104, "Deva", ("Smartwatch", "Earbuds")),
    (105, "Elan", ("Monitor", "HDMI Cable", "Speakers", "Keyboard"))
]

# 1. Generate Order Report
def generate_order_report():
    print("Order Report:")
    for order in orders:
        order_id, customer_name, items = order  # Unpacking tuple
        print(f"Order ID: {order_id}, Customer: {customer_name}")
        print("Items Ordered:")
        # Nested loop to unpack and display items
        for item in items:
            print(f" - {item}")
        print("-" * 30)

# 2. Prevent accidental changes by using immutability
def display_order_items(order_id):
    # Search for the specific order by order_id
    for order in orders:
        if order[0] == order_id:  # Unpacking and checking for matching order_id
            order_id, customer_name, items = order
            print(f"\nItems for Order ID {order_id} (Customer: {customer_name}):")
            # Display the ordered items using unpacking
            for item in items:
                print(f" - {item}")
            break
    else:
        print(f"Order ID {order_id} not found.")

# Testing the functions
generate_order_report()  # Display the order report

# Display specific order items (example: order_id 103)
display_order_items(103)
