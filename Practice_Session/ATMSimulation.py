# ATM Simulation

# Step 1: Set initial balance
balance = 5000.0  # Initial balance in account

# Step 2: Loop for 3 operations
for i in range(3):
    print("\n--- ATM Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    elif choice == '3':
        print(f"Current balance: ₹{balance:.2f}")

    else:
        print("Invalid choice. Please select 1, 2 or 3.")

# Step 3: Final balance display
print("\n--- Transaction Complete ---")
print(f"Final balance: ₹{balance:.2f}")
