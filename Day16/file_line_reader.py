

def read_non_empty_lines(filename):
    try:
        with open(filename, 'r') as file:
            file_iterator = iter(file)
            while True:
                try:
                    line = next(file).strip()
                    if line:  # Only print non-empty lines
                        print(line)
                except StopIteration:
                    break
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")

# Example usage:
read_non_empty_lines("sample.txt")
