class EmailParser:
    def __init__(self, lines):
        import re
        self.lines = lines
        self.index = 0
        self.pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.lines):
            line = self.lines[self.index].strip()
            self.index += 1
            if self.pattern.match(line):
                return line
        raise StopIteration

lines = [
    "banu@example.com",
    "invalid-email",
    "anbu@mail.co.in",
    "not-an-email@",
    "diya@domain.org"
]

print("📧 Valid Emails:")
for email in EmailParser(lines):
    print(email)
