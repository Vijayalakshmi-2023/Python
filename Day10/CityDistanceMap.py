# Structure: {city1: {city2: distance}}
city_distances = {
    "Chennai": {"Delhi": 2800, "Madurai": 790, "Mumbai": 1300},
    "Delhi": {"Chennai": 2800, "Madurai": 2000, "Mumbai": 2700},
    "Madurai": {"Chennai": 790, "Delhi": 2000, "Mumbai": 1300},
    "Mumbai": {"Chennai": 1300, "Delhi": 2700, "Madurai": 1300}
}

# Query the distance between two cities
def get_distance(city1, city2):
    # Check if the city1 exists and the city2 is a neighbor
    if city1 in city_distances and city2 in city_distances[city1]:
        return city_distances[city1][city2]
    elif city2 in city_distances and city1 in city_distances[city2]:
        return city_distances[city2][city1]
    else:
        return f"No direct route between {city1} and {city2}."

# Update the distance between two cities
def update_distance(city1, city2, distance):
    # Ensure both cities exist
    if city1 in city_distances:
        city_distances[city1][city2] = distance
        print(f"Distance between {city1} and {city2} updated to {distance} miles.")
    else:
        print(f"{city1} does not exist in the city map.")

# Find the shortest route (minimum distance) from a given city
def find_shortest_route(city):
    if city in city_distances:
        # Get the city with the minimum distance
        min_distance_city = min(city_distances[city], key=city_distances[city].get)
        min_distance = city_distances[city][min_distance_city]
        print(f"The shortest route from {city} is to {min_distance_city} with a distance of {min_distance} miles.")
    else:
        print(f"{city} does not exist in the city map.")


print(get_distance("Chennai", "Madurai"))

update_distance("Delhi", "Madurai", 1950)

find_shortest_route("Madurai")

print(get_distance("Chennai", "Trichy"))
