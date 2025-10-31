import random
import datetime

class BankAccount(object):
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = random.randint(10000, 99999)
        
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        

        with open(self.filename, "w") as f:
            f.write(f"Account created on {datetime.datetime.now()}\n")
            f.write(f"Account Holder: {self.name}\n")
            f.write(f"Account Type: {self.accountType}\n")
            f.write(f"Account Number: {self.accountNumber}\n")
            f.write(f"Opening Balance: {self.balance}\n\n")

    #Deposit 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            with open(self.filename, "a") as f:
                f.write(f"[{datetime.datetime.now()}] Deposited: ${amount}\n")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    #Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            with open(self.filename, "a") as f:
                f.write(f"[{datetime.datetime.now()}] Withdrawn: ${amount}\n")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    #Get balance
    def getBalance(self):
        return self.balance

    #Get ID, name, and account type
    def getAccountNumber(self):
        return self.accountNumber

    def getAccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.accountType

    # Get transaction history
    def getTransactionHistory(self):
        print("\nTransaction History:")
        with open(self.filename, "r") as f:
            print(f.read())

