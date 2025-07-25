class SkipAndPickIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 2  # skip one item
        return item
def main():
    sample_list = ['a', 'b', 'c', 'd', 'e', 'f']
    print("📦 Picked items (skipping alternate):")
    for item in SkipAndPickIterator(sample_list):
        print(item, end=" ")

main()
