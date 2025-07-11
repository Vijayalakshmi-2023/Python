age = int(input("Enter your age: "))
has_aadhar = input("Do you have an Aadhar card? (yes/no): ").strip().lower()
if age >= 18:
    if has_aadhar is "yes":  
        print(f"✅ You are eligible to apply for a driving license.")
    elif has_aadhar is "no":
        print("❌ Aadhar card is required to apply for a driving license.")
    else:
        print("⚠️ Invalid Aadhar input. Please enter 'yes' or 'no'.")
else:
    print("❌ You are not eligible. Minimum age is 18.")
