def word_stats(paragraph, show_longest=False):
    # Clean and split the paragraph into words
    words = paragraph.lower().split()
    words = [word.strip(".,!?;:()[]{}\"'") for word in words]

    total_words = len(words)
    unique_words = len(set(words))
    longest_word = max(words, key=len) if show_longest and words else None

    if show_longest:
        return total_words, unique_words, longest_word
    else:
        return total_words, unique_words

# --- Example Usage ---
text = input("Enter a paragraph: ")
include_longest = input("Show longest word? (yes/no): ").strip().lower() == "yes"

result = word_stats(text, show_longest=include_longest)

print(f"\n🧾 Total words: {result[0]}")
print(f"🔑 Unique words: {result[1]}")

if include_longest:
    print(f"📏 Longest word: {result[2]}")
