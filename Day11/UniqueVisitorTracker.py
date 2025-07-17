# Unique Visitor Tracker

# Initialize an empty set for visitor IPs
visitor_ips = set()

# Example blacklisted IPs
blacklist = {"192.168.1.100", "10.0.0.5"}

# Function to add new visitor IPs, ignoring blacklisted IPs
def add_visitor(ip):
    if ip in blacklist:
        print(f"Blocked IP ignored: {ip}")
    else:
        visitor_ips.add(ip)
        print(f"Added visitor IP: {ip}")

# Simulated visitor IPs
new_visitors = [
    "192.168.1.10",
    "10.0.0.5",          # blacklisted
    "172.16.0.1",
    "192.168.1.10",      # duplicate
    "192.168.1.100",     # blacklisted
    "10.0.0.8"
]

# Add visitors
for ip in new_visitors:
    add_visitor(ip)

# Total unique visitors
print(f"\nTotal unique visitors: {len(visitor_ips)}")

# Remove blacklisted IPs if accidentally added
for bad_ip in blacklist:
    visitor_ips.discard(bad_ip)

# Backup visitor IP set
backup_visitor_ips = visitor_ips.copy()

print("\nCurrent visitor IPs:", visitor_ips)
print("Backup of visitor IPs:", backup_visitor_ips)
