# main.py

from trip_ops import add_trip, remove_trip, edit_trip, list_unique_destinations, calculate_total_cost
from suggestion_engine import suggest_activities

trips = []

# Add trips
print(add_trip(trips, "Paris", ("2025-08-10", "2025-08-20"), {"Alice", "Bob"}, ["Eiffel Tower"], 2400))
print(add_trip(trips, "Tokyo", ("2025-09-01", "2025-09-12"), {"Charlie"}, ["Akihabara", "Skytree"], 3000))

# Edit trip
print(edit_trip(trips, "Paris", itinerary=["Louvre", "Seine Cruise"], cost=2600))

# Unique destinations
print("🌍 Unique Destinations:", list_unique_destinations(trips))

# Suggestions
print("🧭 Suggestions for Tokyo:", suggest_activities("Tokyo"))

# Cost calculation
print("💰 Total Estimated Cost:", calculate_total_cost(trips))

# Remove trip
print(remove_trip(trips, "Tokyo"))
