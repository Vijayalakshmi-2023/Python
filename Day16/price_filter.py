class PriceFilter:
    def __init__(self, products):
        self.items = iter(products.items())

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            product, price = next(self.items)  # may raise StopIteration
            if price > 1000:
                return (product, price)
products = {
    "Keyboard": 999,
    "Monitor": 4500,
    "Mouse": 550,
    "Laptop": 55000,
    "Headphones": 1200
}

print("🛒 Products above ₹1000:")
for item in PriceFilter(products):
    print(f"{item[0]} - ₹{item[1]}")
