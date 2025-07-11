name = input("Enter your name: ")
units = float(input("Enter electricity units consumed: "))
if units <= 100:
    rate = 2
elif units <= 300:
    rate = 3
else:
    rate = 5
bill = units * rate
print("\n📄 Electricity Bill")
print("---------------------------")
print(f"Name         : {name}")
print(f"Units Used   : {units} units")
print(f"Rate Applied : ₹{rate} per unit")
print(f"Total Bill   : ₹{bill:.2f}")
