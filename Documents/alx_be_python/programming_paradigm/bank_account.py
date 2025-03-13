# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account if funds are sufficient."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
