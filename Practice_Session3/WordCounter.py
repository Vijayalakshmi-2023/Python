# Function to count total words
def count_words(text):
    words = text.split()
    return len(words), words

# Function to count specific word frequency
def count_specific_word(words_list, target):
    count = 0
    for word in words_list:
        if word.lower().strip(".,!?") == target.lower():
            count += 1
    return count

# Main function
def main():
    print("=== Word Counter Tool ===")
    paragraph = input("Enter a paragraph:\n\n")

    total_words, word_list = count_words(paragraph)
    print(f"\n📝 Total Words: {total_words}")

    # Ask for a specific word to check frequency
    target_word = input("Enter a word to check its frequency: ").strip()
    freq = count_specific_word(word_list, target_word)
    print(f"🔍 '{target_word}' appeared {freq} time(s).\n")

# Run the tool
main()
