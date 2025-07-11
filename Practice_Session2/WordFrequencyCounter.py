# Input: a word
word = input("Enter a word: ").strip().lower()

# Dictionary to store frequency
freq = {}

# Count frequency of each character
for char in word:
    if char in freq:
        freq[char] += 1  # Update existing count
    else:
        freq[char] = 1   # Add new character with count 1

# Print frequency of each character
print("\nCharacter frequency:")
for char, count in freq.items():
    print(f"'{char}': {count}")
