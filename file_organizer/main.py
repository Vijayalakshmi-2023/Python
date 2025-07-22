# main.py

import os
from scanner import scan_directory
from mover import move_files_by_type

def main():
    source = input("Enter the path to organize: ").strip()

    if not os.path.isdir(source):
        print("❌ Invalid directory.")
        return

    file_dict, file_types = scan_directory(source)

    print("\n📂 Found File Types:", file_types)
    print("📋 Organizing files...\n")

    move_files_by_type(file_dict, source)

    print("\n✅ File organization complete.")

if __name__ == "__main__":
    main()
