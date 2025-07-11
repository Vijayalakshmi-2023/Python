daily_limit = 10000
total_withdrawn = 0

while True:
    user_input = input("Enter amount to withdraw or type 'stop' to exit: ").strip().lower()

    if user_input == "stop":
        print("Transaction ended by user.")
        break

    if not user_input.isdigit():
        print("Invalid input! Please enter a valid number or 'stop'.")
        break  # Exit early on error as requested

    amount = int(user_input)

    if amount <= 0:
        print("Withdrawal amount must be positive!")
        break  # Exit early on error

    if total_withdrawn + amount > daily_limit:
        print(f"Limit exceeded! You can only withdraw ₹{daily_limit - total_withdrawn} more today.")
        break  # Exit early on limit exceed

    total_withdrawn += amount
    print(f"₹{amount} withdrawn successfully. Total withdrawn today: ₹{total_withdrawn}")

    if total_withdrawn == daily_limit:
        print("You have reached your daily withdrawal limit of ₹10,000.")
        break

print("Thank you for using the ATM!")
