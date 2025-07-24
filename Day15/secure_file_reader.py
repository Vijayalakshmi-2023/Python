import logging
import os

# Setup logging
logging.basicConfig(filename="file_reader_errors.log",
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def secure_file_reader():
    file = None
    try:
        filepath = input("Enter file path to read: ")

        # Outer try block to catch open-related errors
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"The file '{filepath}' does not exist.")
            if not os.access(filepath, os.R_OK):
                raise PermissionError(f"Permission denied for file '{filepath}'.")

            # Try opening and reading the file
            file = open(filepath, 'r')
            try:
                content = file.read()
                print("\n📄 File Content:\n")
                print(content)
            except Exception as read_error:
                logging.error("Error while reading file: %s", read_error)
                print("❌ Error reading the file content.")
        except (FileNotFoundError, PermissionError) as e:
            logging.error("File access error: %s", e)
            print("❌", e)
        except Exception as e:
            logging.error("Unexpected error during file access: %s", e)
            print("❌ Unexpected error:", e)
    finally:
        if file:
            file.close()
            print("\n✅ File closed successfully.")
        else:
            print("\nℹ️ File was not opened.")

# Run the reader
secure_file_reader()
