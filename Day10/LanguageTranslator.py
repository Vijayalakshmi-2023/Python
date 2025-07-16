# Format: {english_word: tamil_word}
english_to_tamil = {
    "hello": "வணக்கம்",
    "goodbye": "பிரியாவிடை",
    "please": "தயவு செய்து",
    "thank you": "நன்றி",
    "yes": "ஆம்",
    "no": "இல்லை"
}
# Add a new translation
def add_translation(english_word, tamil_word):
    if english_word in english_to_tamil:
        print(f"'{english_word}' already exists in the dictionary.")
    else:
        english_to_tamil[english_word] = tamil_word
        print(f"Added translation: {english_word} -> {tamil_word}")

# Update an existing translation
def update_translation(english_word, new_tamil_word):
    if english_word in english_to_tamil:
        english_to_tamil[english_word] = new_tamil_word
        print(f"Updated translation: {english_word} -> {new_tamil_word}")
    else:
        print(f"'{english_word}' not found in the dictionary.")

# Delete a translation
def delete_translation(english_word):
    if english_word in english_to_tamil:
        del english_to_tamil[english_word]
        print(f"Deleted translation for '{english_word}'.")
    else:
        print(f"'{english_word}' not found in the dictionary.")

# Search and return Tamil translation using .get()
def search_translation(english_word):
    tamil_translation = english_to_tamil.get(english_word, "Translation not found.")
    return tamil_translation

# Reverse translation (Tamil to English)
def reverse_translation(tamil_word):
    # Swapping the dictionary to reverse the translation
    tamil_to_english = {v: k for k, v in english_to_tamil.items()}
    return tamil_to_english.get(tamil_word, "Translation not found.")

# Check if a word exists using 'in'
def check_word_exists(english_word):
    if english_word in english_to_tamil:
        print(f"'{english_word}' is available in the dictionary.")
    else:
        print(f"'{english_word}' is not found in the dictionary.")
# Add new translations
add_translation("love", "காதல்")
add_translation("good morning", "காலை வணக்கம்")

# Update existing translation
update_translation("hello", "வணக்கம் (updated)")

# Delete a translation
delete_translation("goodbye")

# Search for Tamil translation
print("\nSearch for 'please':", search_translation("please"))
print("Search for 'goodbye':", search_translation("goodbye"))

# Reverse translation (Tamil → English)
print("\nReverse translation of 'காதல்':", reverse_translation("காதல்"))

# Check if a word exists in the dictionary
check_word_exists("thank you")
check_word_exists("goodbye")
