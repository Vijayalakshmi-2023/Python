def reverse_lines(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()[::-1]

for reversed_line in reverse_lines('sample.txt'):
    print(reversed_line)
