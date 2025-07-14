# Each GPS coordinate is stored as a tuple: (latitude, longitude)

# Simulated GPS movement (immutable data)
gps_log = [
    (40.7128, -74.0060),   # New York
    (41.8781, -87.6298),   # Chicago
    (34.0522, -118.2437),  # Los Angeles
    (29.7604, -95.3698),   # Houston
    (39.9526, -75.1652),   # Philadelphia
    (33.4484, -112.0740),  # Phoenix
    (37.7749, -122.4194),  # San Francisco
    (47.6062, -122.3321),  # Seattle
    (25.7617, -80.1918),   # Miami
    (38.9072, -77.0369)    # Washington, D.C.
]

# Displaying the last 5 GPS locations using slicing
recent_locations = gps_log[-5:]

print("Last 5 GPS Locations:")
print("----------------------")
for coord in recent_locations:
    latitude, longitude = coord  # Unpacking tuple
    print(f"Latitude: {latitude:.4f}, Longitude: {longitude:.4f}")
