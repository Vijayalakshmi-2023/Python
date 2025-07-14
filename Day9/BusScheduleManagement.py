# Sample bus schedule data as a list of tuples (bus_no, departure_time, arrival_time, stops)
bus_schedule = [
    (101, "08:00 AM", "09:30 AM", ("Station A", "Station B", "Station C")),
    (102, "09:00 AM", "10:15 AM", ("Station D", "Station E", "Station F")),
    (103, "10:00 AM", "11:00 AM", ("Station G", "Station H")),
    (104, "12:00 PM", "01:30 PM", ("Station A", "Station I", "Station J")),
    (105, "02:00 PM", "03:00 PM", ("Station B", "Station C", "Station K"))
]

# 1. Display entire bus schedule using tuple unpacking
def display_bus_schedule():
    print("Bus Schedule Report:")
    for route in bus_schedule:
        bus_no, departure_time, arrival_time, stops = route  # Unpacking the tuple
        print(f"Bus No: {bus_no}, Departure: {departure_time}, Arrival: {arrival_time}")
        print("Stops: " + " -> ".join(stops))  # Joining the stops with arrows
        print("-" * 30)

# 2. Extract specific details using slicing and indexing
def get_route_details(bus_no):
    for route in bus_schedule:
        if route[0] == bus_no:  # Check if bus_no matches
            _, departure_time, arrival_time, stops = route  # Unpacking (ignoring bus_no with _)
            print(f"Bus {bus_no} Schedule:")
            print(f"Departure Time: {departure_time}")
            print(f"Arrival Time: {arrival_time}")
            print(f"Stops: {', '.join(stops)}")
            break
    else:
        print(f"Bus No {bus_no} not found.")

# 3. Simulate update of a bus route (replace old tuple with a new one)
def update_route(bus_no, new_route):
    for i, route in enumerate(bus_schedule):
        if route[0] == bus_no:  # Find the route with matching bus_no
            bus_schedule[i] = new_route  # Replace old route with the new one
            print(f"Route for Bus {bus_no} updated.")
            break
    else:
        print(f"Bus No {bus_no} not found.")

# Testing the functions
display_bus_schedule()  # Display all routes

# Get details of a specific bus route (e.g., Bus No 102)
get_route_details(102)

# Simulate an update for Bus 103 (change the arrival time and stops)
update_route(103, (103, "10:15 AM", "11:30 AM", ("Station G", "Station H", "Station X", "Station Y")))

# Display the updated schedule
print("\nUpdated Bus Schedule:")
display_bus_schedule()
