import random

secret_number = random.randint(1, 100)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}: Guess the number (1-100): "))
    if guess == secret_number:
        print("🎉 Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    attempts += 1
else:
    # This else runs only if loop finishes without a break (no correct guess)
    print(f"Sorry! You didn't guess it. The number was {secret_number}.")
