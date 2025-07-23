# -----------------------
# Class: Seat
# -----------------------
class Seat:
    def __init__(self, seat_no):
        self.seat_no = seat_no
        self._is_booked = False

    def book(self):
        if not self._is_booked:
            self._is_booked = True
            return True
        return False

    def cancel(self):
        if self._is_booked:
            self._is_booked = False
            return True
        return False

    def is_available(self):
        return not self._is_booked

    def __str__(self):
        return f"Seat {self.seat_no} - {'Available' if not self._is_booked else 'Booked'}"

# -----------------------
# Class: Movie
# -----------------------
class Movie:
    def __init__(self, title, show_time, total_seats=10):
        self.title = title
        self.show_time = show_time
        self.seats = [Seat(i+1) for i in range(total_seats)]

    @staticmethod
    def check_availability(seat):
        return seat.is_available()

    def get_available_seats(self):
        return [seat for seat in self.seats if seat.is_available()]

    def __str__(self):
        return f"Movie: {self.title}, Show Time: {self.show_time}"

# -----------------------
# Class: Ticket
# -----------------------
class Ticket:
    def __init__(self, user, movie, seat):
        self.user = user
        self.movie = movie
        self.seat = seat

    def __str__(self):
        return f"🎟️ Ticket\nUser: {self.user.name}\nMovie: {self.movie.title}\nSeat: {self.seat.seat_no}\nTime: {self.movie.show_time}"

# -----------------------
# Class: User
# -----------------------
class User:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def book_ticket(self, movie, seat_no):
        if 1 <= seat_no <= len(movie.seats):
            seat = movie.seats[seat_no - 1]
            if Movie.check_availability(seat):
                if seat.book():
                    ticket = Ticket(self, movie, seat)
                    self.tickets.append(ticket)
                    print(f"[✓] Ticket Booked: {ticket}")
                else:
                    print("[!] Seat already booked.")
            else:
                print("[!] Seat not available.")
        else:
            print("[!] Invalid seat number.")

    def cancel_ticket(self, movie, seat_no):
        for ticket in self.tickets:
            if ticket.movie == movie and ticket.seat.seat_no == seat_no:
                if ticket.seat.cancel():
                    self.tickets.remove(ticket)
                    print(f"[✓] Ticket Cancelled for Seat {seat_no}")
                    return
        print("[!] No such ticket found.")

    def show_tickets(self):
        if self.tickets:
            for ticket in self.tickets:
                print(ticket)
        else:
            print("[ℹ] No tickets booked.")

# Create movie
movie1 = Movie("Interstellar", "7:00 PM")

# Create user
user1 = User("Alice")

# Show available seats
print("\nAvailable Seats:")
for seat in movie1.get_available_seats():
    print(seat)

# Book seat 3 and 5
user1.book_ticket(movie1, 3)
user1.book_ticket(movie1, 5)

# Attempt to book already booked seat
user1.book_ticket(movie1, 3)

# Show all user tickets
print("\nUser Tickets:")
user1.show_tickets()

# Cancel a ticket
user1.cancel_ticket(movie1, 3)

# Show tickets after cancellation
print("\nAfter Cancellation:")
user1.show_tickets()
