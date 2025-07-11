cart = []

while True:
    product = input("Enter product name (type 'done' to finish): ").strip()
    
    if product.lower() == "done":
        break  # Exit loop when user types 'done'
    
    if product == "":
        print("⚠️ Empty input skipped.")
        continue  # Skip empty inputs
    
    cart.append(product)
    print(f"✅ '{product}' added to cart.")
else:
    # This else will never run because of break, but included as per instructions
    print("Finished adding products.")

print("\n🧾 Your Shopping Cart:")
if cart:
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item}")
else:
    print("Your cart is empty.")
