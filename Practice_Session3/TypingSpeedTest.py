import time
import requests

# Function to get a random sentence from an API
def get_sentence_from_api():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            return data["content"]
        else:
            return "Practice makes perfect."
    except:
        return "Practice makes perfect."

# Function to calculate typing speed and errors
def typing_test():
    sentence = get_sentence_from_api()
    print("\n=== Typing Speed Test ===")
    print("Type the following sentence:\n")
    print("📋", sentence)
    
    input("\nPress Enter when you're ready to start...")

    start_time = time.time()
    typed = input("\nStart typing: ")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)
    word_count = len(sentence.split())
    speed = round((word_count / time_taken) * 60, 2)

    # Count word-level errors
    original_words = sentence.strip().split()
    typed_words = typed.strip().split()
    errors = sum(1 for o, t in zip(original_words, typed_words) if o != t)
    errors += abs(len(original_words) - len(typed_words))

    # Results
    print("\n=== Results ===")
    print(f"⏱ Time taken: {time_taken} seconds")
    print(f"💨 Typing Speed: {speed} WPM")
    print(f"❌ Errors: {errors}\n")

# Main loop
def main():
    while True:
        typing_test()
        again = input("Try again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for practicing!")
            break

# Run the typing test
main()
