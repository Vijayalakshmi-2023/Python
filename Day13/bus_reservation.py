# Seat class
class Seat:
    def __init__(self, number):
        self.number = number
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Seat {self.number} - {status}"

# Passenger class
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} yrs)"

# Booking class
class Booking:
    def __init__(self, passenger, seat):
        self.passenger = passenger
        self.seat = seat

    def __eq__(self, other):
        return isinstance(other, Booking) and self.passenger.name == other.passenger.name and self.seat.number == other.seat.number

    def __str__(self):
        return f"🎫 Ticket: {self.passenger} - Seat No: {self.seat.number}"

# Bus class
class Bus:
    def __init__(self, total_seats):
        self.seats = [Seat(i+1) for i in range(total_seats)]
        self.bookings = []

    def check_availability(self):
        return [seat for seat in self.seats if not seat.is_booked]

    def book_seat(self, passenger, seat_number):
        if 1 <= seat_number <= len(self.seats):
            seat = self.seats[seat_number - 1]
            if not seat.is_booked:
                seat.is_booked = True
                booking = Booking(passenger, seat)
                self.bookings.append(booking)
                return booking
            else:
                print(f"❌ Seat {seat_number} is already booked.")
        else:
            print("❌ Invalid seat number.")
        return None

    def display_available_seats(self):
        print("\n🪑 Available Seats:")
        for seat in self.check_availability():
            print(seat)

# Create bus with 5 seats
bus = Bus(total_seats=5)

# Create passengers
p1 = Passenger("Alice", 28)
p2 = Passenger("Bob", 35)

# Book seats
ticket1 = bus.book_seat(p1, 2)
ticket2 = bus.book_seat(p2, 4)

# Display available seats
bus.display_available_seats()

# Print tickets
if ticket1:
    print("\n", ticket1)
if ticket2:
    print(ticket2)

# Compare bookings
print("\n🎯 Are the bookings same?", ticket1 == ticket2)
