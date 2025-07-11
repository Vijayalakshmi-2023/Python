# Input: Word to check
word = input("Enter a word: ").strip().lower()

# Reverse the word using a for loop
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word  # Prepend character to build reversed string

# Check if palindrome
if word == reversed_word:
    print(f"✅ '{word}' is a palindrome.")
else:
    print(f"❌ '{word}' is not a palindrome.")
