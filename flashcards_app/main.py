# main.py

from card_ops import add_flashcard, delete_flashcard, review_flashcards, quiz_mode
from stats import display_stats, reset_stats

flashcards = []
categories = {}
stats = {"correct": 0, "incorrect": 0}

def main():
    while True:
        print("\n📚 Language Flashcards Menu")
        print("1. Add Flashcard")
        print("2. Delete Flashcard")
        print("3. Review Flashcards")
        print("4. Start Quiz")
        print("5. View Stats")
        print("6. Reset Stats")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            word = input("Enter word: ")
            translation = input("Enter translation: ")
            category = input("Enter category: ")
            print(add_flashcard(flashcards, categories, word, translation, category))

        elif choice == "2":
            word = input("Enter word to delete: ")
            print(delete_flashcard(flashcards, categories, word))

        elif choice == "3":
            print("\n".join(review_flashcards(flashcards)))

        elif choice == "4":
            quiz_mode(flashcards, stats)

        elif choice == "5":
            print(display_stats(stats))

        elif choice == "6":
            print(reset_stats(stats))

        elif choice == "7":
            print("👋 Exiting. Bye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
