def validate_pin(user_pin):
    """Validate the entered PIN"""
    correct_pin = "1234"
    return user_pin == correct_pin

def atm():
    balance = 1000  # Starting balance

    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
        else:
            print("Invalid deposit amount.")

    def withdrawal(amount):
        nonlocal balance
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrew ${amount}. New balance: ${balance}")
        else:
            print("Invalid or insufficient funds.")

    def change_pin():
        # Placeholder function using `pass`
        pass

    # Simulate some operations
    deposit(200)
    withdrawal(150)
    change_pin()

    print(f"\nFinal balance: ${balance}")

# --- Main Program ---
entered_pin = input("Enter your 4-digit PIN: ")

if validate_pin(entered_pin):
    print("PIN validated successfully.\n")
    atm()
else:
    print("Invalid PIN. Access denied.")
