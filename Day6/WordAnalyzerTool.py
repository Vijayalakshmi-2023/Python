from collections import Counter

def word_analyzer(*words):
    # Print word lengths using map()
    lengths = list(map(len, words))
    print("Word lengths:", lengths)
    
    # Convert words to uppercase using lambda and map
    uppercase_words = list(map(lambda w: w.upper(), words))
    print("Uppercase words:", uppercase_words)
    
    # Function to find most frequent character in a word
    def most_frequent_char(word):
        if not word:
            return None
        count = Counter(word)
        # Return the char with max frequency; if tie, first one
        return max(count, key=count.get)
    
    # Get most frequent char for each word
    frequent_chars = [most_frequent_char(word) for word in words]
    
    return frequent_chars

# Example usage:
result = word_analyzer("hello", "world", "test", "mississippi")
print("Most frequent characters:", result)
