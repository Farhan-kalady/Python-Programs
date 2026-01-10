#Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance = 0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited : ${amount}. New balance : {self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw : ${amount}. New balance : {self.balance}")

account = BankAccount(11011, "Farhan", "Savings_acc", 1000)
account.deposit(10000)
account.withdraw(7000)
