import csv
import logging
import os

# Logging setup
logging.basicConfig(filename='csv_upload_errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception
class InvalidCSVFormatError(Exception):
    pass

def validate_row(row):
    """
    Custom validation logic.
    Example: Expecting [name (str), age (int), email (str)]
    """
    if len(row) != 3:
        raise InvalidCSVFormatError("Row must contain exactly 3 columns.")

    name, age, email = row
    if not name or not email:
        raise ValueError("Name and email cannot be empty.")

    if not age.isdigit() or int(age) < 0:
        raise ValueError("Age must be a non-negative integer.")

    return name, int(age), email


def upload_csv(filepath):
    file = None
    try:
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File '{filepath}' not found.")

        file = open(filepath, newline='', encoding='utf-8')
        reader = csv.reader(file)

        print("📄 Valid Rows:")
        for i, row in enumerate(reader, start=1):
            try:
                validated = validate_row(row)
                print(f"{i}: {validated}")
            except Exception as e:
                logging.error("Invalid row %d: %s | Error: %s", i, row, e)
                print(f"❌ Skipping invalid row {i}: {row} -> {e}")

    except FileNotFoundError as fe:
        logging.error("File error: %s", fe)
        print(f"❌ File not found: {fe}")

    except Exception as e:
        logging.error("Parsing error: %s", e)
        print(f"❌ Unexpected parsing error: {e}")

    else:
        print("\n✅ File parsed successfully.")

    finally:
        if file:
            file.close()
            print("📦 File closed (cleanup complete).")


# Example usage:
if __name__ == "__main__":
    file_path = input("Enter path to CSV file: ").strip()
    upload_csv(file_path)
