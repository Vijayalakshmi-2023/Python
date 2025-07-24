import logging

# Configure logging
logging.basicConfig(filename='atm_errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception
class InsufficientFundsError(Exception):
    pass

class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        assert amount > 0, "Amount must be positive."
        self.balance += amount
        print(f"✅ ₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        assert amount > 0, "Amount must be positive."
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance for this withdrawal.")
        self.balance -= amount
        print(f"✅ ₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"💰 Current balance: ₹{self.balance:.2f}")

# Main ATM loop
def run_atm():
    atm = ATM(initial_balance=5000)  # Starting with ₹5000

    print("🏧 Welcome to the ATM Simulator!")
    while True:
        print("\nOptions: 1) Deposit  2) Withdraw  3) Balance  4) Exit")
        choice = input("Enter choice (1-4): ").strip()

        try:
            if choice == '1':
                try:
                    amt = float(input("Enter amount to deposit: "))
                    atm.deposit(amt)
                except (AssertionError, ValueError) as e:
                    logging.error("Deposit error: %s", e)
                    print(f"❌ Deposit failed: {e}")

            elif choice == '2':
                try:
                    amt = float(input("Enter amount to withdraw: "))
                    atm.withdraw(amt)
                except (AssertionError, ValueError, InsufficientFundsError) as e:
                    logging.error("Withdrawal error: %s", e)
                    print(f"❌ Withdrawal failed: {e}")

            elif choice == '3':
                atm.check_balance()

            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break

            else:
                print("❌ Invalid option. Please choose 1-4.")

        except Exception as e:
            logging.error("Unexpected error: %s", e)
            print("❌ An unexpected error occurred.")

# Run the simulator
run_atm()
