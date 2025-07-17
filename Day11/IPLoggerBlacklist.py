# IP Logger with Blacklist

# Set of visitor IPs logged so far
visitor_ips = {"192.168.1.10", "10.0.0.5"}

# Blacklisted IPs that should never be logged
blacklist = {"192.168.1.100", "10.0.0.5", "123.45.67.89"}

# New IPs visiting the website
new_ips = ["192.168.1.15", "10.0.0.5", "172.16.0.1", "123.45.67.89"]

for ip in new_ips:
    # Check if the IP is blacklisted
    if not {ip}.isdisjoint(blacklist):
        print(f"IP {ip} is blacklisted, skipping.")
        # If already in visitor_ips, discard it (optional)
        visitor_ips.discard(ip)
    else:
        # Safe to add to visitor log
        visitor_ips.add(ip)
        print(f"IP {ip} added to visitor log.")

print("\nCurrent visitor IPs:", visitor_ips)
