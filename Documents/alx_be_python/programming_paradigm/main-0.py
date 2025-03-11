# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')

    if command == "deposit" and params:
        amount = float(params[0])
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")

    elif command == "withdraw" and params:
        amount = float(params[0])
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command. Please use 'deposit', 'withdraw', or 'display'.")

if __name__ == "__main__":
    main()
