# main.py

from poll_ops import create_poll, vote, display_results
from user_ops import has_voted, mark_voted

polls = {}
voted_users = set()

# Create a sample poll
create_poll(polls, "Your favorite programming language?", ["Python", "Java", "C++", "JavaScript"])

while True:
    print("\n📌 Current Poll: Your favorite programming language?")
    user = input("👤 Enter your username (or 'exit' to quit): ")
    if user.lower() == "exit":
        break

    question = "Your favorite programming language?"
    if has_voted(voted_users, user, question):
        print("⚠️ You have already voted in this poll.")
        continue

    print("Options:")
    for opt in polls[question]["options"]:
        print(f" - {opt}")

    selected = input("👉 Enter your choice: ")
    result = vote(polls, question, selected)
    print(result)

    if "🗳️" in result:
        mark_voted(voted_users, user, question)

# Show final results
print(display_results(polls, "Your favorite programming language?"))
