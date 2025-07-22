# main.py

from inventory_ops import add_item, update_stock, remove_item, list_by_category, get_unique_categories, get_unique_suppliers
from alerts import restock_alerts

inventory = {}
categories = {}
suppliers = {}

# Add items
print(add_item(inventory, categories, suppliers, "Apples", 50, 2.5, "Fruits", "FreshFarm Ltd"))
print(add_item(inventory, categories, suppliers, "Laptops", 10, 800.0, "Electronics", "TechSource Inc"))

# Update stock
print(update_stock(inventory, "Apples", quantity=8))

# Remove item
print(remove_item(inventory, categories, suppliers, "Laptops"))

# List by category
print("🍎 Fruits:", list_by_category(inventory, categories, "Fruits"))

# Unique sets
print("📦 Categories:", get_unique_categories(categories))
print("🚚 Suppliers:", get_unique_suppliers(suppliers))

# Restock alerts
print("🚨 Alerts:", restock_alerts(inventory))
