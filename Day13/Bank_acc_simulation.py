class Account:
    def __init__(self, account_no, holder_name, initial_balance=0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = initial_balance  # Encapsulated

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.__balance:.2f}")
        else:
            print("Invalid or insufficient funds.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.holder_name} (A/C: {self.account_no}) - Balance: ₹{self.__balance:.2f}"

class SavingsAccount(Account):
    def __init__(self, account_no, holder_name, initial_balance=0):
        super().__init__(account_no, holder_name, initial_balance)
        self.withdraw_limit = 20000

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Cannot withdraw more than ₹{self.withdraw_limit} in a single transaction.")
        else:
            super().withdraw(amount)

class CurrentAccount(Account):
    def __init__(self, account_no, holder_name, initial_balance=0):
        super().__init__(account_no, holder_name, initial_balance)
        self.withdraw_limit = 50000

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Cannot withdraw more than ₹{self.withdraw_limit} in a single transaction.")
        else:
            super().withdraw(amount)

class Transaction:
    @staticmethod
    def transfer(from_acc, to_acc, amount):
        if amount <= from_acc.get_balance():
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print(f"₹{amount} transferred from {from_acc.holder_name} to {to_acc.holder_name}")
        else:
            print("Transfer failed: insufficient funds.")

# Create accounts
savings = SavingsAccount("S1001", "Alice", 30000)
current = CurrentAccount("C2001", "Bob", 80000)

# Deposit
savings.deposit(5000)
current.deposit(10000)

# Withdraw
savings.withdraw(15000)     # Within limit
current.withdraw(60000)     # Above limit, should fail

# Transfer
Transaction.transfer(current, savings, 10000)

# Check balances
print("\nFinal Balances:")
print(savings)
print(current)
