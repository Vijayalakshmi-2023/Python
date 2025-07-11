# Input: Daily fuel consumption for 7 days
fuel_consumption = []

print("Enter fuel consumption for 7 days (in liters):")
for i in range(1, 8):
    liters = float(input(f"Day {i}: "))
    fuel_consumption.append(liters)

# Calculate total fuel used
total_fuel = 0
for liters in fuel_consumption:
    total_fuel += liters

# Output total and check for alert
print(f"\n⛽ Total fuel consumed in the week: {total_fuel:.2f} liters")

if total_fuel > 50:
    print("⚠️ Alert: High fuel consumption! Consider reducing usage.")
else:
    print("✅ Fuel usage is within normal limits.")
