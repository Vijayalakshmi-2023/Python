# quiz_engine.py

import random

def pick_random_question(questions, asked_indices):
    while True:
        index = random.randint(0, len(questions) - 1)
        if index not in asked_indices:
            asked_indices.add(index)
            return questions[index]

def ask_question(q):
    print("\n" + q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    choice = input("Your answer (1-4): ")
    if choice.isdigit() and 1 <= int(choice) <= 4:
        return q["options"][int(choice) - 1] == q["answer"]
    return False

def get_unique_topics(questions):
    return set(q["topic"] for q in questions)
