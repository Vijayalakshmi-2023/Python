# Initial seat arrangement in the theater (0 = empty, 1 = booked)
seats = (
    (0, 0, 0, 0, 0),  # Row 1
    (0, 1, 0, 0, 0),  # Row 2 (one seat booked)
    (0, 0, 1, 0, 0),  # Row 3 (one seat booked)
    (0, 0, 0, 0, 0),  # Row 4
    (0, 0, 0, 0, 0),  # Row 5
)

# 1. Access specific seat using row and column
def access_seat(row, col):
    if 0 <= row < len(seats) and 0 <= col < len(seats[0]):
        if seats[row][col] == 0:
            print(f"Seat ({row + 1}, {col + 1}) is available.")
        else:
            print(f"Seat ({row + 1}, {col + 1}) is already booked.")
    else:
        print(f"Invalid seat ({row + 1}, {col + 1}).")
    print("-" * 30)

# 2. Show all empty seats in the theater
def show_empty_seats():
    print("Empty seats in the theater:")
    for row_index, row in enumerate(seats):
        for col_index, seat in enumerate(row):
            if seat == 0:
                print(f"Seat ({row_index + 1}, {col_index + 1}) is empty.")
    print("-" * 30)

# 3. Prevent changes to booked seats (immutability of tuples)
def book_seat(row, col):
    # This function simulates attempting to book a seat
    global seats
    if 0 <= row < len(seats) and 0 <= col < len(seats[0]):
        if seats[row][col] == 0:
            print(f"Booking seat ({row + 1}, {col + 1})...")
            # Seat booking would change the original tuple, but tuples are immutable
            # so we have to create a new modified version of the original tuple.
            seats = tuple(
                tuple(1 if (r == row and c == col) else seat for c, seat in enumerate(rw))
                for r, rw in enumerate(seats)
            )
            print(f"Seat ({row + 1}, {col + 1}) successfully booked.")
        else:
            print(f"Seat ({row + 1}, {col + 1}) is already booked.")
    else:
        print(f"Invalid seat ({row + 1}, {col + 1}).")
    print("-" * 30)

# Testing the functions
show_empty_seats()  # Show all empty seats
access_seat(1, 2)  # Check the status of seat (2, 3)
book_seat(1, 2)  # Book seat (2, 3)
show_empty_seats()  # Show updated empty seats after booking
access_seat(1, 2)  # Check the status of seat (2, 3) again after booking
