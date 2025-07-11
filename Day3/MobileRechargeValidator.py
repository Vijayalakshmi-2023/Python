mobile = input("Enter your 10-digit mobile number: ")
amount = float(input("Enter recharge amount (₹): "))

if len(mobile) == 10 and mobile.isdigit():
    if amount > 10:
        print(f"✅ Recharge of ₹{amount:.2f} successful for {mobile}.")
    else:
        print("❌ Recharge amount must be greater than ₹10.")
else:
    print("❌ Invalid mobile number. It must be exactly 10 digits.")
