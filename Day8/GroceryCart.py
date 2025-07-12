# Grocery Cart System
cart = []

def show_menu():
    print("\n=== Grocery Cart Menu ===")
    print("1. Add single item")
    print("2. Add multiple items")
    print("3. View cart items")
    print("4. Remove item")
    print("5. Pop last item")
    print("6. Show total count")
    print("7. Check for duplicates")
    print("8. Show first 3 items")
    print("9. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-9): ")

    if choice == "1":
        item = input("Enter item to add: ").strip()
        cart.append(item)
        print(f"'{item}' added to cart.")

    elif choice == "2":
        items = input("Enter multiple items separated by commas: ")
        item_list = [i.strip() for i in items.split(",")]
        cart.extend(item_list)
        print("Items added:", item_list)

    elif choice == "3":
        if cart:
            print("\n🛒 Cart Items:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item}")
        else:
            print("Cart is empty.")

    elif choice == "4":
        item = input("Enter item to remove: ").strip()
        if item in cart:
            cart.remove(item)
            print(f"'{item}' removed from cart.")
        else:
            print(f"'{item}' not found in cart.")

    elif choice == "5":
        if cart:
            removed = cart.pop()
            print(f"Popped item: {removed}")
        else:
            print("Cart is empty.")

    elif choice == "6":
        print(f"Total items in cart: {len(cart)}")

    elif choice == "7":
        print("\nDuplicate check:")
        seen = set()
        duplicates = set()
        for item in cart:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        if duplicates:
            print("Duplicate items found:", list(duplicates))
        else:
            print("No duplicates found.")

    elif choice == "8":
        print("First 3 items in the cart:", cart[:3])

    elif choice == "9":
        print("Thank you for using Grocery Cart System!")
        break

    else:
        print("Invalid choice. Please try again.")
