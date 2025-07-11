fuel_limit = 50  # Maximum capacity in liters
total_fuel = 0

while total_fuel < fuel_limit:
    try:
        amount = float(input("Enter fuel to add (in liters): "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        continue

    if amount <= 0:
        print("⚠️ Enter a positive amount.")
        continue  # Skip zero or negative values

    if total_fuel + amount > fuel_limit:
        available = fuel_limit - total_fuel
        print(f"⚠️ Can't exceed 50L. You can only add up to {available}L.")
        continue

    total_fuel += amount
    print(f"✅ Added {amount}L. Total fuel: {total_fuel}L")

print("✅ Tank full! 50L reached.")
