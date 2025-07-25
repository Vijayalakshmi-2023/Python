def csv_row_reader(filepath):
    with open(filepath, 'r') as file:
        next(file)  # Skip header row
        for line in file:
            line = line.strip()  # Clean whitespace and newline
            if "END" in line:
                print("END keyword found. Stopping reader.")
                break
            yield line.split(',')  # Return row as a list of values
for row in csv_row_reader("products.csv"):
    print("Row:", row)
