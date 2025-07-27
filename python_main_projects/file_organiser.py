import os
import shutil
import hashlib
import time
import schedule
from pathlib import Path

# Function to organize files by extension
def organize_by_extension(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
            ext_folder = os.path.join(directory, extension)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(ext_folder, filename))
    print("Files organized by extension.")

# Function to find and remove duplicate files
def remove_duplicates(directory):
    seen = set()
    duplicates = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_hash = hash_file(file_path)
            if file_hash in seen:
                duplicates.append(file_path)
            else:
                seen.add(file_hash)
    for duplicate in duplicates:
        os.remove(duplicate)
        print(f"Removed duplicate: {duplicate}")
    print(f"Removed {len(duplicates)} duplicates.")

# Helper function to hash file for duplicate checking
def hash_file(file_path, buffer_size=65536):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(buffer_size):
            sha1.update(chunk)
    return sha1.hexdigest()

# Function to bulk rename files with a given pattern
def bulk_rename_files(directory, pattern):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = filename.split('.')[-1] if '.' in filename else ''
            new_name = pattern.format(filename=filename, extension=extension)
            new_path = os.path.join(directory, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
    print("Bulk renaming completed.")

# Function to find largest files in a directory
def find_largest_files(directory, n=5):
    file_sizes = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            file_sizes.append((filename, size))
    sorted_files = sorted(file_sizes, key=lambda x: x[1], reverse=True)
    print(f"Largest {n} files:")
    for i in range(min(n, len(sorted_files))):
        print(f"{sorted_files[i][0]} - {sorted_files[i][1] / (1024 * 1024):.2f} MB")
    return sorted_files[:n]

# Function to schedule the file organization automatically (daily)
def schedule_organization(directory):
    # Example: schedule to run every day at 2am
    schedule.every().day.at("02:00").do(organize_by_extension, directory=directory)
    schedule.every().day.at("02:30").do(remove_duplicates, directory=directory)
    schedule.every().day.at("03:00").do(find_largest_files, directory=directory, n=5)

    while True:
        schedule.run_pending()
        time.sleep(60)

# Main function to call for organizing files
def main():
    directory = input("Enter the directory path to organize: ")
    
    while True:
        print("\nOptions:")
        print("1. Organize files by extension")
        print("2. Remove duplicate files")
        print("3. Bulk rename files")
        print("4. Find largest files")
        print("5. Schedule automatic organization")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            organize_by_extension(directory)
        elif choice == '2':
            remove_duplicates(directory)
        elif choice == '3':
            pattern = input("Enter the renaming pattern (use {filename} and {extension}): ")
            bulk_rename_files(directory, pattern)
        elif choice == '4':
            n = int(input("How many largest files do you want to find? "))
            find_largest_files(directory, n)
        elif choice == '5':
            print("Scheduling automatic file organization daily...")
            schedule_organization(directory)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
