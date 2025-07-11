# Simple Hotel Room Booking

# Step 1: Dictionary of room types and prices per night
room_prices = {
    "standard": 1000,
    "deluxe": 2000,
    "suite": 3500
}

# Step 2: Input room type and number of nights
room_type = input("Enter room type (standard/deluxe/suite): ").lower()
nights = int(input("Enter number of nights: "))

# Step 3: Check if room type is valid
if room_type in room_prices:
    price_per_night = room_prices[room_type]
    total = price_per_night * nights

    # Step 4: Apply 10% discount if nights > 3
    discount = 0
    if nights > 3:
        discount = total * 0.10
        total -= discount

    # Step 5: Print booking summary
    print("\n----- Booking Summary -----")
    print(f"Room Type      : {room_type.capitalize()}")
    print(f"Nights         : {nights}")
    print(f"Price/Night    : ₹{price_per_night}")
    print(f"Discount       : ₹{discount:.2f}")
    print(f"Total Amount   : ₹{total:.2f}")
    print("----------------------------")
else:
    print("Invalid room type selected.")
