class MultiListIterator:
    def __init__(self, list1, list2):
        self.combined = list1 + list2
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.combined):
            raise StopIteration
        item = self.combined[self.index]
        self.index += 1
        return item
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']

print("🔁 Combined Iteration:")
for item in MultiListIterator(list_a, list_b):
    print(item)
