# Input: Initial balance and withdrawal amount
balance_input = input("Enter your current balance: ")
withdraw_input = input("Enter withdrawal amount: ")

# Validate inputs
if balance_input.replace('.', '', 1).isdigit() and withdraw_input.replace('.', '', 1).isdigit():
    balance = float(balance_input)
    withdrawal = float(withdraw_input)

    # Check if sufficient balance
    if withdrawal <= balance:
        balance -= withdrawal
        print(f"Withdrawal successful! Remaining balance: ₹{balance:.2f}")
    else:
        print("Error: Insufficient balance for this withdrawal.")
else:
    print("Invalid input. Please enter numeric values.")
