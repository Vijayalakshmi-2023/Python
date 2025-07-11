# Input from user
name = input("Enter Your Name: ")

# Initialize vowel count
vowel_count = 0

# Define vowels
vowels = "aeiou"

# Loop through each character in the name
for char in name:
    if char.lower() in vowels:
        vowel_count += 1

# Display the result
print("Total number of vowels:", vowel_count)
