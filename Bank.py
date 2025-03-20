class BankAccount:
    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self._balance

# Create a bank account object
account = BankAccount("123456789")

# Perform some transactions
account.deposit(1000)
account.withdraw(500)
account.deposit(200)

# Additional transactions
account.withdraw(100)
account.deposit(50)
account.withdraw(700)

# Display the balance
print(f"Account Number: {account.account_number}")
print(f"Current Balance: {account.get_balance()}")
