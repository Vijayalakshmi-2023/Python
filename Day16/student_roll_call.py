class StudentRollCall:
    def __init__(self, student_dict):
        self.students = list(student_dict.items())  # convert to list of tuples
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        result = self.students[self.index]
        self.index += 1
        return result

def main():
    student_data = {
        101: "Alice",
        102: "Bob",
        103: "Charlie",
        104: "Diana"
    }

    print("📋 Student Roll-Call:")
    for roll, name in StudentRollCall(student_data):
        print(f"Roll No: {roll}, Name: {name}")

main()
