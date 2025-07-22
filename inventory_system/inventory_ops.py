# inventory_ops.py

def add_item(inventory, categories, suppliers, item, quantity, price, category, supplier):
    if item in inventory:
        return f"❗ Item '{item}' already exists."
    inventory[item] = (quantity, price)
    categories[item] = category
    suppliers[item] = supplier
    return f"✅ Added '{item}' with quantity {quantity} and price {price}."

def update_stock(inventory, item, quantity=None, price=None):
    if item not in inventory:
        return f"❌ Item '{item}' not found."
    current_quantity, current_price = inventory[item]
    new_quantity = quantity if quantity is not None else current_quantity
    new_price = price if price is not None else current_price
    inventory[item] = (new_quantity, new_price)
    return f"🔄 Updated '{item}' to quantity {new_quantity}, price {new_price}."

def remove_item(inventory, categories, suppliers, item):
    if item in inventory:
        del inventory[item]
        categories.pop(item, None)
        suppliers.pop(item, None)
        return f"🗑️ Removed '{item}' from inventory."
    return f"❌ Item '{item}' does not exist."

def list_by_category(inventory, categories, target_category):
    return [item for item, cat in categories.items() if cat == target_category]

def get_unique_categories(categories):
    return set(categories.values())

def get_unique_suppliers(suppliers):
    return set(suppliers.values())
