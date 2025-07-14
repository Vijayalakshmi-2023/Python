from collections import Counter

# Sample list of pixels (RGB values)
image_pixels = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (0, 255, 255), # Cyan
    (255, 0, 0),   # Red
    (255, 255, 255),# White
    (0, 0, 0),     # Black
    (255, 255, 0), # Yellow
    (0, 0, 255)    # Blue
]

# 1. Count how many pixels match a specific color (e.g., Red color)
red_color = (255, 0, 0)
red_count = image_pixels.count(red_color)

print(f"Number of Red Pixels: {red_count}")

# 2. Slice the pixel list to analyze a subregion (e.g., first 5 pixels)
subregion = image_pixels[:5]
print("Subregion (First 5 Pixels):")
print(subregion)

# 3. Return dominant colors using tuple frequency
# Use Counter to count the frequency of each RGB value in the image pixels
color_counts = Counter(image_pixels)
dominant_color = color_counts.most_common(1)

print(f"Dominant Color: {dominant_color[0][0]} with {dominant_color[0][1]} occurrences")

# 4. Display all colors with their frequencies
print("\nAll Colors with Frequencies:")
for color, count in color_counts.items():
    print(f"Color {color} occurs {count} times.")
