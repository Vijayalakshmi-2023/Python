class CountdownTimer:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
start = int(input("Enter countdown start number: "))

print("⏳ Countdown:")
for number in CountdownTimer(start):
    print(number)
