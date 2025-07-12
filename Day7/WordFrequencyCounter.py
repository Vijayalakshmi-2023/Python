# Input paragraph from the user
paragraph = input("Enter a paragraph:\n").strip()

# Convert to lowercase for case-insensitive comparison
paragraph = paragraph.lower()

# Split paragraph into words
words = paragraph.split()

# Create a set to get unique words
unique_words = set(words)

print("\nWord Frequencies:")
for word in unique_words:
    count = words.count(word)
    print(f"{word}: {count}")

# Print total number of words
print("\nTotal number of words:", len(words))
