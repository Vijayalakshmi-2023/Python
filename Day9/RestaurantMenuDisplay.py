# Sample menu data as a list of tuples (item_id, item_name, price)
menu = [
    (101, "Burger", 8.99),
    (102, "Pizza", 12.99),
    (103, "Pasta", 10.50),
    (104, "Salad", 7.00),
    (105, "Steak", 18.50),
    (106, "Ice Cream", 4.50)
]

# 1. Display the menu with formatted output
def display_menu():
    print("Restaurant Menu:")
    print("-" * 30)
    print(f"{'Item ID':<10} {'Item Name':<15} {'Price':>10}")
    print("-" * 30)
    for item in menu:
        item_id, item_name, price = item  # Unpacking the tuple
        print(f"{item_id:<10} {item_name:<15} ${price:>9.2f}")  # Displaying formatted output
    print("-" * 30)

# 2. Find the most expensive item using max() and a lambda function
def find_expensive_item():
    expensive_item = max(menu, key=lambda item: item[2])  # Compare based on price (item[2])
    item_id, item_name, price = expensive_item
    print(f"The most expensive item is: {item_name} (ID: {item_id}), priced at ${price:.2f}")

# Testing the functions
display_menu()  # Display the menu
find_expensive_item()  # Find and display the most expensive item
