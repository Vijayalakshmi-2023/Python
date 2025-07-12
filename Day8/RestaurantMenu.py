# Restaurant Menu System
menu = [
    ["Pizza", 299],
    ["Burger", 149],
    ["Pasta", 199]
]

def show_menu():
    print("\n🍽️  Current Menu:")
    if not menu:
        print("Menu is currently empty.")
    else:
        for item in menu:
            print(f"- {item[0]}: ₹{item[1]}")

def add_dish():
    name = input("Enter dish name: ").strip().title()
    try:
        price = float(input("Enter price (₹): "))
        menu.append([name, price])
        print(f"✅ '{name}' added to the menu for ₹{price}.")
    except ValueError:
        print("❌ Invalid price entered.")

def remove_dish():
    name = input("Enter the name of the dish to remove: ").strip().title()
    for item in menu:
        if item[0] == name:
            menu.remove(item)
            print(f"🗑️ '{name}' has been removed from the menu.")
            return
    print(f"❌ '{name}' not found on the menu.")

def main_menu():
    while True:
        print("\n📋 Menu Manager Options")
        print("1. Show Menu")
        print("2. Add Dish")
        print("3. Remove Dish")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            remove_dish()
        elif choice == "4":
            print("Exiting Menu Manager. Bon appétit! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the system
main_menu()
