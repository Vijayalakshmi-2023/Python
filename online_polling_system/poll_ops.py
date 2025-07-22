# poll_ops.py

def create_poll(polls, question, options):
    polls[question] = {
        "options": options,
        "votes": {option: 0 for option in options}
    }
    return f"✅ Poll created: '{question}' with options {options}"

def vote(polls, question, selected_option):
    if question not in polls:
        return "❌ Poll not found."

    if selected_option not in polls[question]["votes"]:
        return "❌ Invalid option."

    polls[question]["votes"][selected_option] += 1
    return f"🗳️ Vote cast for '{selected_option}'"

def display_results(polls, question):
    if question not in polls:
        return "❌ Poll not found."

    result = f"\n📊 Poll Results: {question}\n"
    for option, count in polls[question]["votes"].items():
        result += f" - {option}: {count} votes\n"
    return result.strip()
