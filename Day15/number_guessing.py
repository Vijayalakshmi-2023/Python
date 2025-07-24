import random

class GameOverError(Exception):
    """Raised when user fails to guess in given attempts."""
    pass

def number_guessing_game():
    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    success = False

    print("🎯 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 20. You have 5 attempts.\n")

    while attempts < max_attempts:
        try:
            guess = input(f"Attempt {attempts + 1}: Enter your guess: ").strip()
            if not guess.isdigit():
                raise ValueError("Input must be a number.")

            guess = int(guess)
            attempts += 1

            if guess == secret:
                print("✅ Correct! You guessed it!")
                success = True
                break
            elif guess < secret:
                print("📉 Too low!")
            else:
                print("📈 Too high!")

            if attempts == max_attempts:
                raise GameOverError("❌ Game Over! You've used all your attempts.")

        except ValueError as ve:
            print(f"⚠️ Invalid input: {ve}")
        except GameOverError as go:
            print(go)
            break
        finally:
            print(f"🔄 Attempts used: {attempts}/{max_attempts}\n")

    if not success:
        print(f"🔒 The number was: {secret}")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
