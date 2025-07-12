# Online Order History Manager

orders = []

def add_order():
    order = input("Enter new order details: ").strip()
    orders.append(order)
    print(f"✅ Order added: '{order}'")

def remove_order():
    order = input("Enter order to cancel/remove: ").strip()
    if order in orders:
        orders.remove(order)
        print(f"❌ Order removed: '{order}'")
    else:
        print("⚠️ Order not found.")

def show_last_five():
    print("\n🛍️ Last 5 Orders:")
    for i, order in enumerate(orders[-5:], start=1):
        print(f"{i}. {order}")

def order_count():
    print(f"\n📊 Total orders placed: {len(orders)}")

def main():
    while True:
        print("\n🛒 Order History Menu")
        print("1. Add new order")
        print("2. Remove canceled order")
        print("3. Show last 5 orders")
        print("4. Show total order count")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_order()
        elif choice == "2":
            remove_order()
        elif choice == "3":
            show_last_five()
        elif choice == "4":
            order_count()
        elif choice == "5":
            print("👋 Exiting Order History Manager. Have a great day!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
