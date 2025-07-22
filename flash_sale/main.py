# main.py

from sale_ops import make_sale, products
from report_ops import print_report, get_unique_buyers

def main():
    while True:
        print("\n🛒 Flash Sale Menu")
        print("1. View Products")
        print("2. Make a Sale")
        print("3. View Sales Report")
        print("4. Unique Buyers")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n📦 Available Products:")
            for code, info in products.items():
                print(f"{code}: {info['name']} - ₹{info['price']} (Stock: {info['stock']})")

        elif choice == "2":
            code = input("Enter product code: ").strip()
            buyer = input("Enter buyer name: ").strip()
            try:
                qty = int(input("Enter quantity: "))
                result = make_sale(code, buyer, qty)
                print(result)
            except ValueError:
                print("❌ Quantity must be a number.")

        elif choice == "3":
            print_report()

        elif choice == "4":
            buyers = get_unique_buyers()
            print("👥 Unique Buyers:", ", ".join(buyers))

        elif choice == "0":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
