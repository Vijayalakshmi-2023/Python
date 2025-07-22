# main.py

from voting import vote, candidates
from tally import tally_results, announce_winner

def main():
    while True:
        print("\n🗳 Simple Voting System")
        print("1. View Candidates")
        print("2. Cast Vote")
        print("3. View Results")
        print("4. Announce Winner")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n👤 Candidates:")
            for c in candidates:
                print(f"- {c}")

        elif choice == "2":
            voter_id = input("Enter your voter ID: ").strip()
            candidate = input("Enter candidate name: ").strip()
            result = vote(voter_id, candidate)
            print(result)

        elif choice == "3":
            tally_results()

        elif choice == "4":
            announce_winner()

        elif choice == "0":
            print("👋 Exiting voting system.")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
