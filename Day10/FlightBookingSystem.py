# Structure: {flight_id: {"route": ..., "passengers": [...]}}
flights = {}

# Add a new passenger to a flight
def add_passenger(flight_id, passenger_name, max_seats=100):
    # Use setdefault to ensure the flight exists
    flight = flights.setdefault(flight_id, {"route": "", "passengers": []})
    
    # Check if there are available seats
    if len(flight["passengers"]) < max_seats:
        if passenger_name not in flight["passengers"]:
            flight["passengers"].append(passenger_name)
            print(f"{passenger_name} has been added to flight {flight_id}.")
        else:
            print(f"{passenger_name} is already on flight {flight_id}.")
    else:
        print(f"Sorry, no available seats on flight {flight_id}.")

# Remove a passenger from a flight
def remove_passenger(flight_id, passenger_name):
    flight = flights.get(flight_id)
    
    if flight:
        if passenger_name in flight["passengers"]:
            flight["passengers"].remove(passenger_name)
            print(f"{passenger_name} has been removed from flight {flight_id}.")
        else:
            print(f"{passenger_name} is not on flight {flight_id}.")
    else:
        print(f"Flight {flight_id} does not exist.")

# Check if there are available seats on a flight
def check_seat_availability(flight_id, max_seats=100):
    flight = flights.get(flight_id)
    
    if flight:
        available_seats = max_seats - len(flight["passengers"])
        print(f"Flight {flight_id} has {available_seats} available seats.")
    else:
        print(f"Flight {flight_id} does not exist.")

# Set flight route
def set_flight_route(flight_id, route):
    flight = flights.setdefault(flight_id, {"route": "", "passengers": []})
    flight["route"] = route
    print(f"Route for flight {flight_id} set to {route}.")
# Add flight routes
set_flight_route("FL123", "New York - Los Angeles")
set_flight_route("FL456", "Chicago - Miami")

# Add passengers to flights
add_passenger("FL123", "Alice")
add_passenger("FL123", "Bob")
add_passenger("FL123", "Charlie")

# Remove a passenger
remove_passenger("FL123", "Bob")

# Check seat availability
check_seat_availability("FL123")

# Add more passengers
add_passenger("FL123", "David")
add_passenger("FL456", "Eve")

# Check seat availability for another flight
check_seat_availability("FL456")
