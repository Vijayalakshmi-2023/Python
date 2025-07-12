# Function to count character frequencies
def count_characters(text):
    freq = {}  # Dictionary to store frequencies

    for char in text:
        if char != " ":  # Ignore spaces
            char = char.lower()  # Optional: case-insensitive
            freq[char] = freq.get(char, 0) + 1

    return freq

# Function to display frequency in a formatted way
def display_frequencies(freq_dict):
    print("\n=== Character Frequencies ===")
    for char, count in sorted(freq_dict.items()):
        print(f"'{char}': {count}")
    print()

# Main program
def main():
    sentence = input("Enter a sentence: ")
    frequencies = count_characters(sentence)
    display_frequencies(frequencies)

# Run the counter
main()
