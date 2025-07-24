import datetime

class OverBookingError(Exception):
    """Raised when number of guests exceeds room capacity."""
    pass

def book_hotel():
    try:
        date_str = input("Enter booking date (YYYY-MM-DD): ").strip()
        guest_count = input("Enter number of guests: ").strip()
        room_count = input("Enter number of rooms: ").strip()

        # Convert inputs
        booking_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        guests = int(guest_count)
        rooms = int(room_count)

        # Use assert to ensure date is valid (today or future)
        assert booking_date >= datetime.date.today(), "Booking date cannot be in the past."

        # Raise OverBookingError if guests exceed capacity (2 guests per room)
        if guests > rooms * 2:
            raise OverBookingError("Too many guests for the available rooms.")

    except ValueError as ve:
        print(f"❌ ValueError: {ve}")
    except AssertionError as ae:
        print(f"❌ AssertionError: {ae}")
    except OverBookingError as oe:
        print(f"❌ OverBookingError: {oe}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    else:
        print("\n✅ Booking confirmed!")
        print(f"🗓 Date: {booking_date}, 👥 Guests: {guests}, 🏨 Rooms: {rooms}")
    finally:
        print("\n📌 Booking attempt complete.")

# Run the system
if __name__ == "__main__":
    book_hotel()
