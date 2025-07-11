# Alphabet Counter

# Input: Get a string from the user
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special_chars = 0

# Define vowel characters
vowel_chars = "aeiouAEIOU"

# Loop through each character in the string
for char in text:
    if char.isalpha():
        if char in vowel_chars:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1

# Display the results
print(f"\nVowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special Characters: {special_chars}")
