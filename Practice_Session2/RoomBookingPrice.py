# Input: Room type and number of nights
room_type = input("Enter room type (Standard/Deluxe): ").strip().lower()
nights = int(input("Enter number of nights stayed: "))

# Set base price based on room type
if room_type == "standard":
    price_per_night = 1000
elif room_type == "deluxe":
    price_per_night = 1500
else:
    print("❌ Invalid room type. Please enter 'Standard' or 'Deluxe'.")
    exit()

# Calculate total price
total_price = price_per_night * nights

# Apply 20% discount if nights > 3
if nights > 3:
    discount = total_price * 0.20
    total_price -= discount
    print(f"💸 20% discount applied: ₹{discount:.2f}")
else:
    print("ℹ️ No discount applied.")

# Output final price
print(f"🏨 Room Type: {room_type.capitalize()}")
print(f"🛏️ Nights Stayed: {nights}")
print(f"💰 Total Price to Pay: ₹{total_price:.2f}")
