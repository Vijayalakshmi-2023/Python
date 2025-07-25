dictionary = {
    "hello": "வணக்கம்",
    "world": "உலகம்",
    "apple": "ஆப்பிள்",
    "book": "புத்தகம்",
    "computer": "கணினி"
}
words = ["hello", "world", "python", "book", "mouse", "apple"]
# Generator expression with filtering
lazy_translator = (
    (word, dictionary[word]) 
    for word in words 
    if word in dictionary
)
def chained_translator(word_pairs):
    for eng, tam in word_pairs:
        yield f"Original: {eng}"
        yield f"Translated: {tam}"
for line in chained_translator(lazy_translator):
    print(line)
