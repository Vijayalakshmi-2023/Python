class CartIterator:
    def __init__(self, cart_items):
        if not cart_items:
            raise ValueError("🛒 Your cart is empty!")
        self.cart = cart_items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cart):
            raise StopIteration
        item = self.cart[self.index]
        self.index += 1
        return item
def main():
    # Simulating user cart
    user_cart = ["Laptop", "Mouse", "Keyboard", "Charger"]

    try:
        cart_iter = CartIterator(user_cart)
        print("🛍️ Items in your cart:")

        for item in cart_iter:
            print(f" - {item}")

    except ValueError as e:
        print(f"❌ {e}")

main()

