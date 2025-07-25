class LazySquareIterator:
    def __init__(self, numbers):
        if not numbers:
            raise ValueError("Input list is empty. Cannot calculate squares.")
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        num = self.numbers[self.index]
        self.index += 1
        return num ** 2
def main():
    try:
        user_input = input("Enter numbers separated by space: ").strip()
        if not user_input:
            raise ValueError("No input provided.")

        numbers = list(map(int, user_input.split()))

        print("Squares (lazily generated):")
        for square in LazySquareIterator(numbers):
            print(square)
    except ValueError as e:
        print(f"❌ Error: {e}")

main()
