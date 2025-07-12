# Input sentence
sentence = input("Enter a sentence: ").lower()

# Vowels to check
vowels = "aeiou"

# Count and print frequency of each vowel
print("\nVowel Frequencies:")
for vowel in vowels:
    count = sentence.count(vowel)
    print(f"{vowel}: {count}")
