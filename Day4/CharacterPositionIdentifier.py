# Character Position Identifier

# Input: Get a name from the user
name = input("Enter your name: ")

# Use enumerate to print index and character
for index, char in enumerate(name):
    print(f"{index} - {char}")
