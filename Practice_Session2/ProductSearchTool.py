# Predefined list of products
products = ["laptop", "mouse", "keyboard", "monitor", "printer"]

# Input: Product to search
search_item = input("Enter the product to search: ").strip().lower()

# Flag to track if found
found = False

# Search using for loop and if
for item in products:
    if item == search_item:
        found = True
        break

# Output result
if found:
    print(f"✅ '{search_item}' is Available in stock.")
else:
    print(f"❌ '{search_item}' is Out of stock.")
