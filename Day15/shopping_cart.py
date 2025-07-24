import logging

# Configure logging
logging.basicConfig(filename='cart_errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception
class ProductExistsError(Exception):
    pass

def shopping_cart_calculator():
    cart = {}
    total = 0.0

    print("🛒 Welcome to the Shopping Cart!\n(Type 'done' to finish)\n")

    while True:
        try:
            product = input("Enter product name: ").strip()
            if product.lower() == 'done':
                break

            if product in cart:
                raise ProductExistsError(f"'{product}' already exists in the cart.")

            price_input = input(f"Enter price for {product}: ").strip()

            # Validate price
            price = float(price_input)
            if price < 0:
                raise ValueError("Price cannot be negative.")

            # Add to cart
            cart[product] = price

        except ValueError as ve:
            logging.error("Invalid price entry: %s", ve)
            print("❌ Invalid price. Please enter a numeric value.")
        except ProductExistsError as pe:
            logging.error("Duplicate product: %s", pe)
            print(f"❌ {pe}")
        except Exception as e:
            logging.error("Unexpected error: %s", e)
            print("❌ Unexpected error occurred.")
        finally:
            print(f"🧾 Current cart total: ₹{sum(cart.values()):.2f} | Items: {len(cart)}\n")

    # Final cart summary
    print("\n🛍️ Final Cart Summary:")
    for item, price in cart.items():
        print(f"- {item}: ₹{price:.2f}")
    print(f"✅ Total amount: ₹{sum(cart.values()):.2f}")
    print(f"📦 Total items: {len(cart)}")

# Run the cart
shopping_cart_calculator()
