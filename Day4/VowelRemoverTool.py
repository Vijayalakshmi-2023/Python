# Vowel Remover Tool

# Input: Get a sentence from the user
sentence = input("Enter a sentence: ")

# Define vowels
vowels = "aeiouAEIOU"

# New string to collect non-vowel characters
no_vowels = ""

# Use for loop to process each character
for char in sentence:
    if char in vowels:
        continue  # Skip vowels
    no_vowels += char  # Add non-vowel characters

# Display the filtered sentence
print("Filtered sentence without vowels:", no_vowels)
