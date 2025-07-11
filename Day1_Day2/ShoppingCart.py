shopping_cart = {}

def add_item():
    item = input("Enter item name: ").strip().title()
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        if price < 0 or quantity <= 0:
            print("Price must be positive and quantity must be at least 1.")
            return
    except ValueError:
        print("Invalid price or quantity.")
        return
    
    if item in shopping_cart:
        shopping_cart[item]['quantity'] += quantity
        shopping_cart[item]['price'] = price  # Update price if changed
    else:
        shopping_cart[item] = {'price': price, 'quantity': quantity}
    print(f"Added {quantity} x {item} at ${price:.2f} each.")

def view_cart():
    if not shopping_cart:
        print("Your shopping cart is empty.")
        return
    print("\nShopping Cart:")
    total = 0
    for item, details in shopping_cart.items():
        item_total = details['price'] * details['quantity']
        total += item_total
        print(f"- {item}: ${details['price']:.2f} x {details['quantity']} = ${item_total:.2f}")
    print(f"Total cost: ${total:.2f}")

def remove_item():
    item = input("Enter the item name to remove: ").strip().title()
    if item in shopping_cart:
        del shopping_cart[item]
        print(f"{item} removed from the cart.")
    else:
        print(f"{item} not found in your cart.")

def update_quantity():
    item = input("Enter the item name to update quantity: ").strip().title()
    if item in shopping_cart:
        try:
            quantity = int(input("Enter the new quantity: "))
            if quantity <= 0:
                print("Quantity must be at least 1.")
                return
            shopping_cart[item]['quantity'] = quantity
            print(f"Updated {item} quantity to {quantity}.")
        except ValueError:
            print("Please enter a valid integer quantity.")
    else:
        print(f"{item} not found in your cart.")

def main():
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Update Quantity")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            update_quantity()
        elif choice == '5':
            print("Thank you for shopping! Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
