# Function to count file types
def count_file_types(filenames):
    file_types = {}
    
    # Loop through each filename in the list
    for filename in filenames:
        # Extract the file extension by splitting the filename at the last dot
        extension = filename.split('.')[-1]
        
        # Update the dictionary using .get() to handle missing extensions
        file_types[extension] = file_types.get(extension, 0) + 1
    
    return file_types
# Example list of filenames
filenames = ["file1.txt", "image.jpg", "file2.txt", "photo.png", "image.jpg"]

# Count file types
file_type_counts = count_file_types(filenames)

# Output the result
print("File type counts:", file_type_counts)
