# Sample flight data: Each flight is represented by a tuple
# (flight_id, source, destination, passenger_list)
flights = [
    (101, "New York", "London", [("Alice", 35), ("Bob", 42), ("Charlie", 29)]),  # Passenger info (name, age)
    (102, "Los Angeles", "Tokyo", [("David", 25), ("Eva", 38)]),
    (103, "Paris", "Berlin", [("Frank", 30), ("Grace", 27), ("Hannah", 33), ("Ian", 40)]),
    (104, "Sydney", "Auckland", [("John", 28)])
]

# 1. Show all passengers for each flight using nested loops and unpacking
def show_passengers():
    for flight in flights:
        flight_id, source, destination, passenger_list = flight  # Unpacking flight tuple
        print(f"Flight ID: {flight_id}, Source: {source}, Destination: {destination}")
        print("Passengers:")
        for passenger in passenger_list:  # Nested loop for passengers
            name, age = passenger  # Unpacking passenger tuple
            print(f"  Name: {name}, Age: {age}")
        print("-" * 30)

# 2. Count the number of passengers per flight
def count_passengers():
    for flight in flights:
        flight_id, _, _, passenger_list = flight  # Unpacking and ignoring source and destination
        num_passengers = len(passenger_list)
        print(f"Flight ID {flight_id} has {num_passengers} passenger(s).")

# 3. Update flight information by replacing old tuple with a new one
def update_flight(flight_id, new_details):
    for i, flight in enumerate(flights):
        if flight[0] == flight_id:  # Find the flight by its ID
            flights[i] = new_details  # Replace the old flight tuple with the new one
            print(f"Flight ID {flight_id} updated successfully!")
            return
    print(f"Flight ID {flight_id} not found.")

# Testing the functions
show_passengers()  # Show all passengers for each flight
count_passengers()  # Count number of passengers per flight

# Example of updating a flight (ID: 102)
new_flight_details = (102, "Los Angeles", "Tokyo", [("David", 25), ("Eva", 38), ("Alice", 30)])
update_flight(102, new_flight_details)  # Update flight 102

# Show updated flight details
print("\nUpdated Flight Information:")
show_passengers()
