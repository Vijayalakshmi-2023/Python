class DigitExtractor:
    def __init__(self, mixed_string):
        self.chars = mixed_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.chars):
            char = self.chars[self.index]
            self.index += 1
            if char.isdigit():
                return int(char)
        raise StopIteration
def main():
    mixed_input = "abc123def456"

    print("🔢 Extracted digits:")
    for digit in DigitExtractor(mixed_input):
        print(digit, end=" ")

main()
