# Task 12: Login Simulation using Python
correct_password = "mypassword123"
while True:
    user_input = input("Enter your password: ")
    
    if user_input == correct_password:
        print("✅ Access granted. Welcome!")
        break  
    else:
        print("❌ Incorrect password. Please try again.")

# Task 13: Menu-Based App Simulation
while True:
    print("\n--- Main Menu ---")
    print("1. Greet")
    print("2. Show Help")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("👋 Hello! Hope you're having a great day!")
    elif choice == "2":
        print("ℹ️ Help: Choose 1 to greet, 2 for help, or 3 to exit the app.")
    elif choice == "3":
        print("👋 Exiting... Thank you for using the app!")
        break
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 3.")

# Task 14: Ask for numbers until a negative number is entered
while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("❌ Negative number entered. Stopping the program.")
        break
    else:
        print(f"✅ You entered: {num}")

# Task 15: ATM Simulation
balance = 1000.0  # Initial balance
while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"✅ Your current balance is: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"💰 ${amount:.2f} deposited successfully.")
        else:
            print("❌ Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("❌ Invalid withdrawal amount.")
        elif amount > balance:
            print("❌ Insufficient balance.")
        else:
            balance -= amount
            print(f"💸 ${amount:.2f} withdrawn successfully.")

    elif choice == "4":
        print("👋 Thank you for using the ATM. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select from 1 to 4.")

##🔂 While with continue Statement (16–25)
# Task 16: Print odd numbers from 1 to 20 using continue.
print("Task 16:")
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print("\n")

# Task 17: Ask the user to enter 5 numbers. Skip the number if it is negative using continue.
print("Task 17:")
count = 0
while count < 5:
    num = int(input(f"Enter number {count+1}: "))
    if num < 0:
        print("Negative number skipped.")
        continue
    print(f"You entered: {num}")
    count += 1
print()

# Task 18: Print numbers from 1 to 10, but skip 5 using continue.
print("Task 18:")
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print("\n")

# Task 19: Print all numbers from 1 to 20 except those divisible by 3.
print("Task 19:")
i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print("\n")

# Task 20: Ask the user to enter 10 words. Skip if the word is less than 3 characters.
print("Task 20:")
count = 0
while count < 10:
    word = input(f"Enter word {count+1}: ")
    if len(word) < 3:
        print("Word too short, skipped.")
        continue
    print(f"Accepted: {word}")
    count += 1
print()

# Task 21: Print only vowels from the string "python programming" using while and continue.
print("Task 21:")
text = "python programming"
i = 0
while i < len(text):
    if text[i].lower() not in "aeiou":
        i += 1
        continue
    print(text[i], end=' ')
    i += 1
print("\n")

# Task 22: Count how many odd numbers exist between 1 and 100.
print("Task 22:")
count = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue
    count += 1
    i += 1
print(f"Odd numbers between 1 and 100: {count}\n")

# Task 23: Keep asking user for numbers and print only if it's a multiple of 5.
print("Task 23:")
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Stopping.")
        break
    if num % 5 != 0:
        continue
    print(f"{num} is a multiple of 5.")
print()

# Task 24: Skip printing numbers divisible by both 2 and 3 from 1 to 30.
print("Task 24:")
i = 1
while i <= 30:
    if i % 2 == 0 and i % 3 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print("\n")

# Task 25: Skip even numbers and print the cube of odd numbers between 1 and 20.
print("Task 25:")
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(f"Cube of {i} is {i**3}")
    i += 1
print()

##🛑 While with break Statement (26–35)
# Task 26: Print numbers from 1 to 10 and break if number is 6
print("Task 26:")
i = 1
while i <= 10:
    if i == 6:
        break
    print(i, end=' ')
    i += 1
print("\n")

# Task 27: Ask the user to enter numbers. Break the loop when user enters 0
print("Task 27:")
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Stopping input.")
        break
    print(f"You entered: {num}")
print()

# Task 28: Simple password checker, break loop if correct password entered
print("Task 28:")
correct_password = "pass123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password, try again.")
print()

# Task 29: Print numbers from 1 to 100. Break when a number divisible by 17 is found
print("Task 29:")
i = 1
while i <= 100:
    if i % 17 == 0:
        print(f"Number divisible by 17 found: {i}")
        break
    print(i, end=' ')
    i += 1
print("\n")

# Task 30: Keep asking for user input until they type "exit"
print("Task 30:")
while True:
    user_input = input("Type something (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting.")
        break
print()

# Task 31: Simulate a game loop: “Press q to quit”
print("Task 31:")
while True:
    command = input("Press 'q' to quit the game: ")
    if command.lower() == 'q':
        print("Game quit.")
        break
print()

# Task 32: Ask the user 10 questions, stop early if any answer is empty
print("Task 32:")
count = 0
while count < 10:
    answer = input(f"Answer question {count+1}: ")
    if answer == "":
        print("Empty answer detected. Stopping early.")
        break
    count += 1
print()

# Task 33: Simulate 3 login attempts. Break if login is successful
print("Task 33:")
correct_password = "secret"
attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Login successful.")
        break
    else:
        print("Incorrect password.")
    attempts += 1
if attempts == 3:
    print("Maximum login attempts reached.")
print()

# Task 34: Print multiplication table of 5, stop if product exceeds 30
print("Task 34:")
i = 1
while True:
    product = 5 * i
    if product > 30:
        break
    print(f"5 x {i} = {product}")
    i += 1
print()

# Task 35: Count from 1 to 10. If number is 7, break and print message
print("Task 35:")
i = 1
while i <= 10:
    if i == 7:
        print("Loop Interrupted")
        break
    print(i, end=' ')
    i += 1
print()

##📝 While with pass Statement (36–40)
# Task 36: Loop through 1 to 5 and use pass when number is 3.
print("Task 36:")
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder, no action for 3
    else:
        print(i)
print()

# Task 37: Simulate a placeholder loop for future features.
print("Task 37:")
for _ in range(5):
    pass  # Future logic will be added here
print("Placeholder loop executed.\n")

# Task 38: Create a loop where you skip logic for even numbers using pass.
print("Task 38:")
for i in range(1, 6):
    if i % 2 == 0:
        pass  # Skip logic for even numbers
    else:
        print(i)
print()

# Task 39: Use a loop that prints numbers 1 to 5 and uses pass when number is 2 or 4.
print("Task 39:")
for i in range(1, 6):
    if i == 2 or i == 4:
        pass  # Placeholder for 2 and 4
    else:
        print(i)
print()

# Task 40: Create a loop that runs without errors using pass as a placeholder for missing logic.
print("Task 40:")
for i in range(3):
    pass  # Placeholder logic, no action
print("Loop completed without errors.\n")

##🔚 While with else Statement (41–45)
# Task 41: Print numbers from 1 to 3. Use else to print "Loop Finished".
print("Task 41:")
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop Finished\n")

# Task 42: Ask the user to enter 3 numbers. Use else to say “All numbers entered successfully”.
print("Task 42:")
count = 0
while count < 3:
    num = input(f"Enter number {count + 1}: ")
    count += 1
else:
    print("All numbers entered successfully\n")

# Task 43: Run a loop to print even numbers till 10. Use break to exit early. Ensure else doesn’t run.
print("Task 43:")
for num in range(2, 11, 2):
    if num == 6:
        print("Breaking at 6")
        break
    print(num)
else:
    print("Loop completed without break")  # Won't print because of break
print()

# Task 44: Print numbers from 1 to 5. If loop finishes without break, print “Nice job!”.
print("Task 44:")
for i in range(1, 6):
    print(i)
else:
    print("Nice job!\n")

# Task 45: Create a password checker with 3 attempts. If successful, print inside else.
print("Task 45:")
correct_password = "open123"
attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password.")
    attempts += 1
else:
    # This runs only if loop was NOT broken (i.e., all attempts failed)
    print("Failed login after 3 attempts.\n")

##🔁 Logical/Practical Looping Use-Cases (46–50)
# Task 46: Ask the user to input 5 student names using while and store them in a list.
print("Task 46:")
students = []
count = 0
while count < 5:
    name = input(f"Enter student name {count + 1}: ")
    students.append(name)
    count += 1
print("Students list:", students, "\n")

# Task 47: Create a menu-driven loop for a to-do list app (add, view, remove, exit).
print("Task 47:")
todo_list = []
while True:
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
    elif choice == "2":
        if todo_list:
            print("Tasks:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks yet.")
    elif choice == "3":
        if todo_list:
            print("Tasks:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
            try:
                remove_idx = int(input("Enter task number to remove: "))
                if 1 <= remove_idx <= len(todo_list):
                    removed = todo_list.pop(remove_idx - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to remove.")
    elif choice == "4":
        print("Exiting To-Do List app.")
        break
    else:
        print("Invalid option. Please choose 1-4.")

print()

# Task 48: Ask the user to enter age of 5 people. Print how many are adults (age ≥ 18).
print("Task 48:")
count = 0
adults = 0
while count < 5:
    age = int(input(f"Enter age of person {count + 1}: "))
    if age >= 18:
        adults += 1
    count += 1
print(f"Number of adults (18 or older): {adults}\n")

# Task 49: Create a quiz loop: keep asking until the user gets the correct answer.
print("Task 49:")
correct_answer = "Python"
while True:
    answer = input("What programming language is this? ")
    if answer.strip().lower() == correct_answer.lower():
        print("Correct! 🎉")
        break
    else:
        print("Try again.")

print()

# Task 50: Build a basic number guessing game. User keeps guessing until the correct number is entered.
print("Task 50:")
import random

secret_number = random.randint(1, 20)
print("Guess the number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right! 🎉")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
