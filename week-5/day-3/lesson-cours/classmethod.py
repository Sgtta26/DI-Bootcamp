import random

class BankAccount:

    available_account = 100000

    def __init__(self, holder, address):
        self.__holder = holder
        self.__address = address
        self.__account = BankAccount.available_account
        self.__balance = 0.0

        BankAccount.available_account += 1

    def deposit(self, amount):
        self.__balance += amount

    def __iadd__(self, amount):
        self.__balance += amount
        return self # __iadd__ (or any dunder method with 'i') need to return self
    
    @property # REMOVES brackets. makes a function act like an attribute
    def balance(self):
        return self.__balance
    
    @property
    def holder(self):
        return self.__holder

    @property
    def account(self):
        return self.__account

    @property # Get method. @property is GET by default
    def address(self):
        return self.__address

    @address.setter # Set method
    def address(self, new_address):
        self.__address = new_address



account1 = BankAccount('Yossi', 'Tel Aviv')
account2 = BankAccount('Lea', 'Herzlia')

print(account1.address)
print(account2.address)

account1.address = 'Afula'
# print(account1.__dict__) # __dict__ = dictionary with all object attributes and values

account1.deposit(100)
account1 += 100
print(account1.balance)
