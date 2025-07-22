# card_ops.py
import random

def add_flashcard(flashcards, categories, word, translation, category):
    flashcards.append((word, translation))
    categories[word] = category
    return f"✅ Flashcard '{word}' added."

def delete_flashcard(flashcards, categories, word):
    for i, (w, _) in enumerate(flashcards):
        if w == word:
            flashcards.pop(i)
            categories.pop(word, None)
            return f"🗑️ Flashcard '{word}' deleted."
    return f"❌ Word '{word}' not found."

def review_flashcards(flashcards):
    return [f"{word} → {translation}" for word, translation in flashcards]

def quiz_mode(flashcards, stats):
    if not flashcards:
        return "⚠️ No flashcards available."
    random.shuffle(flashcards)
    for word, translation in flashcards:
        answer = input(f"What is the meaning of '{word}'? ")
        if answer.strip().lower() == translation.lower():
            print("✅ Correct!")
            stats["correct"] += 1
        else:
            print(f"❌ Incorrect. Correct answer: {translation}")
            stats["incorrect"] += 1
