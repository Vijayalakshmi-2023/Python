# List Search with Break

# Sample product list
products = ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard"]

# Input: Product to search
search_item = input("Enter product to search: ")

# Search using loop
for product in products:
    if product.lower() == search_item.lower():
        print("Product Found")
        break
else:
    print("Not Found")
