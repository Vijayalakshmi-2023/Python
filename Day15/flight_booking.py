class NoSeatsAvailableError(Exception):
    """Raised when no seats are left to book."""
    pass

class FrequentFlyerDiscountError(Exception):
    """Raised to indicate a frequent flyer discount has been applied."""
    pass
import logging
from datetime import datetime

logging.basicConfig(
    filename='booking_status.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def book_ticket(passenger_id, travel_date, frequent_flyer=False):
    global available_seats

    try:
        # Validate ID (should be alphanumeric)
        if not passenger_id.isalnum():
            raise ValueError("Invalid Passenger ID format.")

        # Validate date (should be in YYYY-MM-DD)
        datetime.strptime(travel_date, "%Y-%m-%d")

        # Check seat availability
        if available_seats <= 0:
            raise NoSeatsAvailableError("All seats have been booked.")

        # Simulate booking
        available_seats -= 1
        print(f"✅ Booking confirmed for {passenger_id} on {travel_date}.")

        # Raise discount info if frequent flyer
        if frequent_flyer:
            raise FrequentFlyerDiscountError(f"{passenger_id} eligible for discount.")

    except ValueError as ve:
        print(f"❌ Error: {ve}")
        logging.error(f"Booking failed for {passenger_id}: {ve}")

    except NoSeatsAvailableError as ne:
        print(f"❌ Error: {ne}")
        logging.error(f"Booking failed for {passenger_id}: {ne}")

    except FrequentFlyerDiscountError as ff:
        print(f"💸 Notice: {ff}")
        logging.info(f"Discount applied for {passenger_id}: {ff}")

    finally:
        logging.info(f"Booking attempt complete for {passenger_id}")
        print("📋 Booking status logged.\n")
if __name__ == "__main__":
    available_seats = 2  # Seat limit for the simulation

    bookings = [
        ("user123", "2025-08-01", False),
        ("vip456", "2025-08-02", True),
        ("user$", "2025-08-03", False),        # Invalid ID
        ("user789", "2025-08-04", False),
        ("late999", "2025/08/05", False),      # Invalid date
        ("user888", "2025-08-06", True),       # No seat left
    ]

    for pid, date, flyer in bookings:
        book_ticket(pid, date, flyer)
