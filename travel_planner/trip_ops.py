# trip_ops.py

def add_trip(trips, destination, dates, participants, itinerary, cost):
    trip = {
        "destination": destination,
        "dates": tuple(dates),
        "participants": set(participants),
        "itinerary": list(itinerary),
        "cost": cost
    }
    trips.append(trip)
    return f"✅ Trip to {destination} added."

def remove_trip(trips, destination):
    for trip in trips:
        if trip["destination"] == destination:
            trips.remove(trip)
            return f"🗑️ Trip to {destination} removed."
    return f"❌ No trip to {destination} found."

def edit_trip(trips, destination, **updates):
    for trip in trips:
        if trip["destination"] == destination:
            for key, value in updates.items():
                if key in trip:
                    if key == "participants":
                        trip[key].update(value)
                    elif key == "dates":
                        trip[key] = tuple(value)
                    else:
                        trip[key] = value
            return f"🔄 Trip to {destination} updated."
    return f"❌ No trip to {destination} found."

def list_unique_destinations(trips):
    return {trip["destination"] for trip in trips}

def calculate_total_cost(trips):
    return sum(trip["cost"] for trip in trips)
