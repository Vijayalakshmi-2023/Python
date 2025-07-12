# Function to display poll results
def show_results(poll_question, options, votes):
    print(f"\n📊 Poll Results: {poll_question}")
    total_votes = sum(votes)
    for i in range(len(options)):
        percent = (votes[i] / total_votes * 100) if total_votes > 0 else 0
        print(f"{options[i]} - {votes[i]} votes ({percent:.1f}%)")
    print(f"🧮 Total Votes: {total_votes}\n")

# Main polling function
def polling_app():
    print("=== Dynamic Polling App ===")
    poll_question = input("Enter the poll question: ").strip()

    # Input poll options
    options = []
    while True:
        option = input("Enter an option (or type 'done' to finish): ").strip()
        if option.lower() == 'done':
            if len(options) < 2:
                print("❌ Please enter at least 2 options.")
                continue
            break
        elif option == "":
            print("❌ Option cannot be empty.")
        else:
            options.append(option)

    # Initialize votes list
    votes = [0] * len(options)

    # Voting loop
    while True:
        print(f"\n📢 {poll_question}")
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")

        try:
            choice = input("Enter option number to vote (or type 'results' or 'exit'): ").strip().lower()
            if choice == 'exit':
                print("👋 Poll ended. Final results:")
                show_results(poll_question, options, votes)
                break
            elif choice == 'results':
                show_results(poll_question, options, votes)
            else:
                index = int(choice) - 1
                if 0 <= index < len(options):
                    votes[index] += 1
                    print(f"✅ Vote recorded for '{options[index]}'")
                else:
                    print("❌ Invalid option number.")
        except ValueError:
            print("❌ Invalid input. Please enter a number or command.")

# Run the polling app
polling_app()
