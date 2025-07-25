class ReverseStringIterator:
    def __init__(self, text):
        if not text:
            raise ValueError("Input string cannot be empty.")
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.text[self.index]
        self.index -= 1
        return char
try:
    user_input = input("Enter a string: ")
    rev_iter = ReverseStringIterator(user_input)
    
    for ch in rev_iter:
        print(ch)
except ValueError as e:
    print(f"Error: {e}")
