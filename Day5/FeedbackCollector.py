while True:
    feedback = input("Enter your feedback: ").strip()

    if feedback.lower() == "exit":
        print("Thank you for your feedback!")
        break  # Exit the loop when user types 'exit'

    if len(feedback) < 3:
        print("⚠️ Feedback too short, please enter at least 3 characters.")
        continue  # Skip feedback shorter than 3 characters

    print("✅ Feedback recorded:", feedback)
