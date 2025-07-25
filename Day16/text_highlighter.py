class TextHighlighter:
    def __init__(self, text):
        words = text.replace('\n', ' ').split()
        self.capitalized_words = [w for w in words if w[0].isupper()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.capitalized_words):
            raise StopIteration
        word = self.capitalized_words[self.index]
        self.index += 1
        return word
paragraph = """Hi! Everyone, Welcome You All. I am Vijayalakshmi."""

print("✨ Highlighted (Capitalized) Words:")
for word in TextHighlighter(paragraph):
    print(word)
