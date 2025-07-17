# Vocabulary Builder from Articles

# Let's assume we have two article files: 'article1.txt' and 'article2.txt'
# For demonstration, I'll simulate the file contents as strings.

article1_text = """
Python is a powerful programming language.
It is widely used for web development, data analysis, and automation.
"""

article2_text = """
Learning Python can boost your career.
Automation and data science are popular fields.
"""

# User's known words
known_words = {"python", "is", "a", "and", "for", "your", "it"}

# Function to extract words from text (simulate reading from files)
def extract_words(text):
    # Split on whitespace and punctuation, convert to lowercase
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# Extract words from both articles
words_article1 = extract_words(article1_text)
words_article2 = extract_words(article2_text)

# Build unique vocabulary set using set comprehension
unique_vocab = {word for word in words_article1 + words_article2}

# Find words not in user's known words
new_words = unique_vocab.difference(known_words)

print("Unique vocabulary found in articles:", unique_vocab)
print("\nNew words for the user to learn:", new_words)
