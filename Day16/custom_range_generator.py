class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.start, self.end)

class MyRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val
r = MyRange(3, 7)

# First use
for num in r:
    print(num)  # 3, 4, 5, 6

print("---")

# Reused again
for num in r:
    print(num)  # 3, 4, 5, 6
