# Format: {item_name: {"stock": ..., "min_required": ..., "supplier": ...}}
inventory = {
    "Laptop": {"stock": 10, "min_required": 5, "supplier": "TechCorp"},
    "Smartphone": {"stock": 50, "min_required": 20, "supplier": "MobileWorld"},
    "Headphones": {"stock": 3, "min_required": 10, "supplier": "SoundMax"},
    "Keyboard": {"stock": 25, "min_required": 10, "supplier": "TechShop"},
    "Mouse": {"stock": 2, "min_required": 5, "supplier": "QuickGadgets"}
}
# Alert items that are below the minimum required stock
def alert_low_stock():
    print("\nLow Stock Alerts:")
    for item, data in inventory.items():
        if data["stock"] < data["min_required"]:
            print(f"  {item} - Stock: {data['stock']} (Minimum Required: {data['min_required']})")

# Add a new item using setdefault
def add_new_item(item_name, stock, min_required, supplier):
    inventory.setdefault(item_name, {"stock": stock, "min_required": min_required, "supplier": supplier})
    print(f"\nAdded new item: {item_name} with {stock} stock.")

# Delete discontinued items
def delete_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"\nDeleted discontinued item: {item_name}.")
    else:
        print(f"\nItem '{item_name}' not found in the inventory.")

# Export low-stock items using dictionary comprehension
def export_low_stock_items():
    low_stock_items = {item: data for item, data in inventory.items() if data["stock"] < data["min_required"]}
    print("\nLow Stock Items:")
    if low_stock_items:
        for item, data in low_stock_items.items():
            print(f"  {item} - Stock: {data['stock']} (Minimum Required: {data['min_required']})")
    else:
        print("No items are below the minimum required stock.")
# Alert for low stock
alert_low_stock()

# Add a new item using setdefault
add_new_item("Tablet", 30, 10, "GadgetWorld")

# Delete a discontinued item
delete_item("Mouse")

# Alert for low stock after adding a new item and deleting an old one
alert_low_stock()

# Export low-stock items using dictionary comprehension
export_low_stock_items()
