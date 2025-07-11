# Global inventory dictionary
inventory = {}

def add_items(**items):
    global inventory
    for item, quantity in items.items():
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

def total_items():
    global inventory
    return sum(inventory.values())

def get_all_items():
    global inventory
    # Return items sorted alphabetically as a list of tuples (item, quantity)
    return sorted(inventory.items())

# Example usage:
add_items(apples=4, bananas=2)
add_items(oranges=5, bananas=3)

print("Total items:", total_items())          # Total items: 14
print("All items:", get_all_items())          # [('apples', 4), ('bananas', 5), ('oranges', 5)]
