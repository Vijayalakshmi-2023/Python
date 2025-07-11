age = int(input("Enter your age: "))
income = float(input("Enter your monthly income (in ₹): "))
if age < 21:
    print(f"❌ Not eligible for loan. Reason: Age {age} is less than 21.")
elif income < 20000:
    print(f"❌ Not eligible for loan. Reason: Income ₹{income:.2f} is less than ₹20,000.")
else:
    print(f"✅ Eligible for loan. Age: {age}, Income: ₹{income:.2f}")
