# ---------------------------
# Class: MenuItem
# ---------------------------
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

# ---------------------------
# Class: Order
# ---------------------------
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def total_price(self):
        return sum(item.price for item in self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

# ---------------------------
# Class: Bill
# ---------------------------
class Bill:
    tax_rate = 0.18  # 18% GST

    def __init__(self, order: Order):
        self.order = order

    def generate(self):
        subtotal = self.order.total_price()
        tax = Bill.calculate_tax(subtotal)
        total = subtotal + tax
        return subtotal, tax, total

    @staticmethod
    def calculate_tax(amount):
        return round(amount * Bill.tax_rate, 2)

# ---------------------------
# Class: Customer
# ---------------------------
class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, menu: dict, item_names: list):
        for name in item_names:
            if name in menu:
                self.order.add_item(menu[name])

    def show_bill(self):
        bill = Bill(self.order)
        subtotal, tax, total = bill.generate()
        print(f"\nBill for {self.name}")
        print("-" * 30)
        for item in self.order.items:
            print(f"{item.name:<15} ₹{item.price}")
        print("-" * 30)
        print(f"{'Subtotal':<15} ₹{subtotal}")
        print(f"{'Tax (18%)':<15} ₹{tax}")
        print(f"{'Total':<15} ₹{total}")

# Define Menu
menu = {
    "Burger": MenuItem("Burger", 120),
    "Pizza": MenuItem("Pizza", 250),
    "Coffee": MenuItem("Coffee", 90),
    "Pasta": MenuItem("Pasta", 180)
}

# Create Customer
c1 = Customer("Anjali")

# Place Order
c1.place_order(menu, ["Pizza", "Coffee", "Burger"])

# Remove an item
c1.order.remove_item("Coffee")

# Show Bill
c1.show_bill()
