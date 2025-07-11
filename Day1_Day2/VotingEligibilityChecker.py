def check_voting_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative!")
        elif age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are NOT eligible to vote yet.")
    except ValueError:
        print("Please enter a valid integer for age.")

if __name__ == "__main__":
    check_voting_eligibility()
