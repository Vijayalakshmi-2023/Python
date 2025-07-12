# Input paragraph and keyword
paragraph = input("Enter a paragraph:\n")
keyword = input("Enter the keyword to highlight: ")

# Count occurrences (case-insensitive)
count = paragraph.lower().count(keyword.lower())

# Replace all occurrences with uppercase keyword (case-insensitive)
# Using a simple approach with replace after normalizing case:
import re
pattern = re.compile(re.escape(keyword), re.IGNORECASE)
highlighted_paragraph = pattern.sub(keyword.upper(), paragraph)

print("\nHighlighted Paragraph:")
print(highlighted_paragraph)
print(f"\nThe keyword '{keyword}' appeared {count} times.")
