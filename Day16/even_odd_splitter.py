class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration
class OddIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 != 0:
                return num
        raise StopIteration
nums = [10, 21, 32, 43, 54, 65, 76, 87, 98]

print("Even numbers:")
for even in EvenIterator(nums):
    print(even)

print("\nOdd numbers:")
for odd in OddIterator(nums):
    print(odd)
