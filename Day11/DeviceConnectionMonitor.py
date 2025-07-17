# Device Connection Monitor

# Current devices connected to Server A
server_a_connections = {"device1", "device2", "device3"}

# Current devices connected to Server B
server_b_connections = {"device3", "device4", "device5"}

# New device connects to Server A
server_a_connections.add("device6")
print("Server A connections after adding device6:", server_a_connections)

# Device disconnects from Server A (using pop to remove an arbitrary device)
disconnected_device = server_a_connections.pop()
print(f"Device disconnected from Server A: {disconnected_device}")
print("Server A connections now:", server_a_connections)

# Merge connections from both servers to get all connected devices
all_connected_devices = server_a_connections.union(server_b_connections)
print("All devices connected across servers:", all_connected_devices)
