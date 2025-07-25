import string

def word_by_word_speaker(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove punctuation and split words lazily
            clean_line = line.translate(str.maketrans('', '', string.punctuation))
            for word in clean_line.strip().split():
                yield word
# Simulate audio playback (word-by-word)
for word in word_by_word_speaker("paragraph.txt"):
    print("Speaking:", word)
