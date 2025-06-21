"""
Objective

Design a basic banking system using object-oriented programming principles. 
The system should support multiple types of bank accounts and standard operations like deposit, withdrawal, and balance checking.
"""

class Account(self, owner, balance):
    self.owner = owner
    self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance():
        pass

class SavingsAccount(Account, interest_rate):
    self.interest_rate = interest_rate
    

class CheckingAccount(Account, overdraft_limit):
    self.overdraft_limit = overdraft_limit


