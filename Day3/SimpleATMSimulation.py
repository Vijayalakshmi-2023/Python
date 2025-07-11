balance = float(input("Enter initial balance: "))
transaction = input("Do you want to deposit or withdraw? ").strip().lower()
if transaction == "deposit":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"✅ ₹{amount} deposited successfully.")
    print(f"💰 Updated Balance: ₹{balance:.2f}")
elif transaction == "withdraw":
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        print(f"✅ ₹{amount} withdrawn successfully.")
        print(f"💰 Updated Balance: ₹{balance:.2f}")
    else:
        print("❌ Insufficient balance.")
        print(f"💰 Available Balance: ₹{balance:.2f}")

else:
    print("❌ Invalid transaction type. Please choose 'deposit' or 'withdraw'.")
