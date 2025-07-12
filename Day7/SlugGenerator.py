# Input blog title
title = input("Enter blog title: ")

# Strip leading/trailing spaces
clean_title = title.strip()

# Replace multiple spaces with a single space (optional)
import re
clean_title = re.sub(r'\s+', ' ', clean_title)

# Convert to lowercase
clean_title = clean_title.lower()

# Replace spaces with hyphens
slug = clean_title.replace(" ", "-")

print("\nGenerated slug:")
print(slug)
