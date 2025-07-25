# Mocked database with dictionaries
products = [
    {"id": 1, "name": "Laptop", "stock": 5},
    {"id": 2, "name": "Keyboard", "stock": 0},
    {"id": 3, "name": "Monitor", "stock": 3},
    {"id": 4, "name": "Mouse", "stock": 0},
    {"id": 5, "name": "Headphones", "stock": 4},
    {"id": 6, "name": "Webcam", "stock": 2},
    {"id": 7, "name": "Microphone", "stock": 0},
    {"id": 8, "name": "Speaker", "stock": 6},
    {"id": 9, "name": "Charger", "stock": 1},
    {"id": 10, "name": "USB Cable", "stock": 0}
]
# Generator expression to keep only products in stock
in_stock_products = (p for p in products if p["stock"] > 0)
def product_viewer(product_iterable, page_size=5):
    page = []
    for product in product_iterable:
        page.append(product)
        if len(page) == page_size:
            yield page
            page = []
    if page:
        yield page  # Yield the last page
    return "End of product list"
viewer = product_viewer(in_stock_products, page_size=5)

try:
    while True:
        page = next(viewer)
        print("\n--- Product Page ---")
        for product in page:
            print(f"{product['name']} (Stock: {product['stock']})")
except StopIteration as e:
    print("\nNo more products.")
    print("Message:", e.value)
