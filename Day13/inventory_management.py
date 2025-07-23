# ----------------------
# Supplier with Encapsulation
# ----------------------
class Supplier:
    def __init__(self, name, contact):
        self.__name = name
        self.__contact = contact

    def get_info(self):
        return f"Supplier: {self.__name}, Contact: {self.__contact}"

# ----------------------
# Item Class
# ----------------------
class Item:
    def __init__(self, name, price, quantity, supplier):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier  # Supplier object

    def __str__(self):
        return f"{self.name} | Price: ₹{self.price} | Qty: {self.quantity}"

# ----------------------
# Inventory Class
# ----------------------
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item
        print(f"Added item: {item.name}")

    def update_quantity(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name].quantity = quantity
            print(f"Updated quantity for {item_name} to {quantity}")
        else:
            print(f"Item '{item_name}' not found.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Removed item: {item_name}")
        else:
            print(f"Item '{item_name}' not found.")

    def __contains__(self, item_name):
        return item_name in self.items

    def __getitem__(self, item_name):
        return self.items.get(item_name)

    def show_inventory(self):
        for item in self.items.values():
            print(item)

# Supplier
s1 = Supplier("FreshFarms", "9876543210")

# Items
apple = Item("Apple", 50, 100, s1)
milk = Item("Milk", 30, 200, s1)

# Inventory
inv = Inventory()
inv.add_item(apple)
inv.add_item(milk)

inv.update_quantity("Apple", 120)
inv.show_inventory()

print("Milk" in inv)
print(inv["Milk"])
