# Input title text
title = input("Enter the banner title: ").strip()

# Define total width of banner
total_width = 40

# Create stars on sides
stars_count = (total_width - len(title) - 2) // 2  # subtract 2 for spaces around title
stars = "*" * stars_count

# Combine stars + space + title + space + stars
banner = stars + " " + title + " " + stars

# If odd width leftover, add one more star at the end
if len(banner) < total_width:
    banner += "*"

print("\n" + banner)
