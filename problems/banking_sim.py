"""
Objective

Design a basic banking system using object-oriented programming principles. 
The system should support multiple types of bank accounts and standard operations like deposit, withdrawal, and balance checking.

1. Base Class: Account
    Represents a generic bank account.

    Properties:
        owner: Name of the account holder
        balance: Current amount of money in the account

    Methods:
        deposit(amount)
        withdraw(amount)
        check_balance()

2. Derived Class: SavingsAccount
    Inherits from Account
    Additional Properties:
        interest_rate (e.g., 2% = 0.02)

    Additional Methods:
        apply_interest() — adds interest to the current balance

3. Derived Class: CheckingAccount
    Inherits from Account
    Additional Properties:

        overdraft_limit — allows withdrawing beyond the balance up to this limit
    Override withdraw() to allow withdrawals beyond balance (within limit)

Test Cases / Scenarios to Cover
    Create one savings and one checking account.
    Deposit and withdraw various amounts in both.
    Try to overdraw from a checking account (within and beyond limit).
    Apply interest to the savings account.
    Print account balances at various stages.

Optional Challenges (Extra Credit)
    Add method transfer(to_account, amount) to move funds between accounts.
    Add a Bank class to manage multiple Account instances.
    Persist data to a file (e.g. JSON) and load it back.
    Create a CLI interface using input() to interact with the system.

"""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} has been withdrawn")
        else:
            print("You're trying to withdraw more than you can afford")

    def check_balance(self):
        print(f"This account's balance is: {self.balance}")
        

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance = self.balance*(1+self.interest_rate)
        print(f"{self.interest_rate} has been applied")
    

class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} has been withdrawn")
        elif (amount<=self.balance+self.overdraft_limit):
            self.balance -= amount
            print("You're cooked, bro, you're overdrafting")
        elif (amount>self.balance+self.overdraft_limit):
            print("Not even overdrafting can save you")
    
    

account_1 = Account("John", 100)
account_1.check_balance()

account_1.deposit(10)
account_1.check_balance()

account_1.withdraw(10)
account_1.check_balance()

account_1.withdraw(1011)
account_1.check_balance()