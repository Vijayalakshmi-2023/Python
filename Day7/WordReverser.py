# Input sentence from user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Reverse each word using slicing [::-1]
reversed_words = [word[::-1] for word in words]

# Join reversed words back into a sentence
reversed_sentence = " ".join(reversed_words)

print("Reversed words sentence:")
print(reversed_sentence)
