# Inventory System
inventory = [["apple", 10], ["banana", 20], ["milk", 15]]

def show_menu():
    print("\n=== Shop Inventory Menu ===")
    print("1. View inventory")
    print("2. Add new product")
    print("3. Update product quantity")
    print("4. Delete a product")
    print("5. Exit")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\n📦 Current Inventory:")
        for item in inventory:
            print(f"- {item[0].capitalize()}: {item[1]} units")

def add_product():
    name = input("Enter product name: ").lower()
    if any(name == product[0] for product in inventory):
        print(f"⚠️ '{name}' already exists. Use option 3 to update quantity.")
        return
    try:
        qty = int(input("Enter quantity: "))
        inventory.append([name, qty])
        print(f"✅ Added '{name}' with quantity {qty}.")
    except ValueError:
        print("❌ Please enter a valid number.")

def update_quantity():
    name = input("Enter product name to update: ").lower()
    for product in inventory:
        if product[0] == name:
            try:
                qty = int(input(f"Enter new quantity for {name}: "))
                product[1] = qty
                print(f"🔄 Updated '{name}' to {qty} units.")
                return
            except ValueError:
                print("❌ Quantity must be a number.")
                return
    print(f"❌ '{name}' not found in inventory.")

def delete_product():
    name = input("Enter product name to delete: ").lower()
    for product in inventory:
        if product[0] == name:
            inventory.remove(product)
            print(f"🗑️ '{name}' removed from inventory.")
            return
    print(f"❌ '{name}' not found.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–5): ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_quantity()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        print("Exiting... Thank you! 🛒")
        break
    else:
        print("Invalid option. Try again.")
