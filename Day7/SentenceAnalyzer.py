# Input sentence
sentence = input("Enter a sentence: ")

# First character (index 0)
first_char = sentence[0] if sentence else ""

# Last character (index -1)
last_char = sentence[-1] if sentence else ""

# First space position using find()
first_space_pos = sentence.find(" ")

# Count vowels and spaces
vowels = "aeiouAEIOU"
vowel_count = sum(sentence.count(v) for v in vowels)
space_count = sentence.count(" ")

# Output results
print(f"First character: '{first_char}'")
print(f"Last character: '{last_char}'")
print(f"First space position: {first_space_pos}")
print(f"Total vowels: {vowel_count}")
print(f"Total spaces: {space_count}")
