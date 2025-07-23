# Account class
class Account:
    def __init__(self, account_number, name, pin, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.__pin = pin
        self.__balance = balance  # Private balance

    def verify_pin(self, input_pin):
        return self.__pin == input_pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

# Transaction class
class Transaction:
    @staticmethod
    def deposit(account, amount):
        if account.deposit(amount):
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Invalid deposit amount.")

    @staticmethod
    def withdraw(account, *args):
        # Overloaded withdraw using *args
        for amount in args:
            if account.withdraw(amount):
                print(f"✅ Withdrawn ₹{amount}")
            else:
                print(f"❌ Insufficient balance or invalid amount: ₹{amount}")

# ATM class
class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def authenticate(self, acc_num, pin):
        account = self.accounts.get(acc_num)
        if account and account.verify_pin(pin):
            return account
        print("❌ Authentication failed.")
        return None

    def balance_enquiry(self, account):
        print(f"💰 Available Balance: ₹{account.get_balance()}")

# Create ATM and account
atm = ATM()
acc1 = Account("1001", "Alice", "1234", 5000)
atm.add_account(acc1)

# Authenticate user
user = atm.authenticate("1001", "1234")

if user:
    # Balance Enquiry
    atm.balance_enquiry(user)

    # Deposit ₹2000
    Transaction.deposit(user, 2000)
    atm.balance_enquiry(user)

    # Withdraw ₹1000 and ₹500 using overloaded method
    Transaction.withdraw(user, 1000, 500)
    atm.balance_enquiry(user)

    # Invalid Withdraw attempt
    Transaction.withdraw(user, 100000)
