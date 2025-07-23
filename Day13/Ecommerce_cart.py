class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount  # percent

    def final_price(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return f"{self.name} - ₹{self.final_price():.2f}"

class Cart:
    def __init__(self):
        self.items = []

    def __add__(self, product):
        self.items.append(product)
        return self

    def remove(self, product_name):
        self.items = [p for p in self.items if p.name != product_name]

    def __contains__(self, product_name):
        return any(p.name == product_name for p in self.items)

    def __getitem__(self, index):
        return self.items[index]

    def total_cost(self):
        return sum(p.final_price() for p in self.items)

    @staticmethod
    def calculate_tax(amount, rate=18):
        return amount * rate / 100

    def __len__(self):
        return len(self.items)

    def show_items(self):
        for p in self.items:
            print(p)

class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart + product

    def remove_from_cart(self, product_name):
        self.cart.remove(product_name)

    def view_cart(self):
        print(f"\nCart of {self.username}:")
        self.cart.show_items()
        total = self.cart.total_cost()
        tax = Cart.calculate_tax(total)
        print(f"Subtotal: ₹{total:.2f}")
        print(f"Tax (18%): ₹{tax:.2f}")
        print(f"Total: ₹{total + tax:.2f}")

class Order(Cart):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.items = user.cart.items.copy()

    def generate_invoice(self):
        print(f"\nInvoice for {self.user.username}")
        self.show_items()
        subtotal = self.total_cost()
        tax = self.calculate_tax(subtotal)
        total = subtotal + tax
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax: ₹{tax:.2f}")
        print(f"Final Amount: ₹{total:.2f}")
        print("Order placed successfully.")

# Create Products
p1 = Product("Laptop", 60000, discount=10)
p2 = Product("Mouse", 500)
p3 = Product("Keyboard", 1500, discount=5)

# User and Cart
user1 = User("vijay")
user1.add_to_cart(p1)
user1.add_to_cart(p2)
user1.add_to_cart(p3)

# View Cart
user1.view_cart()

# Check for item in cart
print("\nIs 'Mouse' in cart?", "Mouse" in user1.cart)
print("Second item in cart:", user1.cart[1])

# Remove item
user1.remove_from_cart("Mouse")
user1.view_cart()

# Place Order
order = Order(user1)
order.generate_invoice()
