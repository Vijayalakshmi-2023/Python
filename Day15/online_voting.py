import logging

# Setup logging for unexpected errors
logging.basicConfig(filename='voting_errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class AlreadyVotedError(Exception):
    """Raised when a user attempts to vote more than once."""
    pass

def voting_system():
    voted = False  # Session-level voting flag

    try:
        print("🗳️ Welcome to the Online Voting System")
        choice = input("Do you want to vote? (yes/no): ").strip().lower()

        if choice == "yes":
            if voted:
                raise AlreadyVotedError("⚠️ You have already voted in this session.")

            candidate = input("Enter your candidate name: ").strip()
            print(f"✅ Vote cast for: {candidate}")
            voted = True

            # Simulate another voting attempt (optional for demo)
            second_try = input("Do you want to vote again? (yes/no): ").strip().lower()
            if second_try == "yes":
                if voted:
                    raise AlreadyVotedError("⚠️ You already voted once!")

        elif choice == "no":
            print("❌ Voting skipped.")
        else:
            print("⚠️ Invalid option.")

    except AlreadyVotedError as ave:
        print(ave)
    except Exception as e:
        print("❌ An unexpected error occurred.")
        logging.error(f"Unexpected Error: {e}")
    finally:
        print("🙏 Thank you for using the voting system.")

# Run the system
if __name__ == "__main__":
    voting_system()
