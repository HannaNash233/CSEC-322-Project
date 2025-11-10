# checkingAccount.py
#
# authors: Will Wian, Detric Brown, Evan Fannin
#
# date: 10/29/25

from bankAccount import BankAccount
from transaction import Transaction
from AES_CBC import *
from random import randint

DEBUG = False
messageExtenders = ["ab", "cd", "12", "34", "QWERTY", "WASDX", "dogs", "cats",
"\t"]
extenderLength = len(messageExtenders) - 1

# Encryption key (Ensure the key is 16, 24, or 32 bytes for AES-128, AES-192, or AES-256)
key = b'MySuperSecretKey1222222222222222'
#print("The length of the key is %d bytes" % len(key))

# Initialization vector (Ensure the IV is 16 bytes)
iv = b'MySuperSecretIV7'
#print("The length of the Initialization Vector is %d bytes" % len(iv))

class CheckingAccount(BankAccount):
    
     INTEREST_RATE = 0.015
    
     def __init__(self, initBalance=0.0): #Me
        #Initialize the account with an initial balance and empty transaction list
          super().__init__(initBalance)
          assert isinstance(initBalance, (int, float))
          self.balance = float(initBalance)
          self.transactions = []
          self.transactions.append(f"Account created with balance: ${self.balance:.2f}")
          self.type = "Checkings"
    
     def displayDetails(self): #Me
        #Display current account details
          print(f"Current balance: ${self.balance:.2f}")
          print("Recent transactions:")
          print("\n Transactions for Account %d" % (self.accountNumber))
    
        # Check if the list of transactions is empty
          if not self.transactions:
               print("No transactions recorded.")
               return
        
          for transaction in self.transactions:
               print(transaction)        
        
     
    
    # @override: Apply 1.5% interest rate
    # @require: balance > 0 to earn interest
     def calculateInterest(self):
          assert self.balance > 0, "Interest cannot be applied to negative or zero balance."
          if self.balance <= 0:
               return False
        
          interestEarned = self.balance * CheckingAccount.INTEREST_RATE
          self.balance += interestEarned
          self.transactions.append(Transaction(self.transactionNumber, "interest", interestEarned))
          self.transactionNumber += 1
          return True        
    
    # @override: Cannot withdrawal more funds than are in the checking account (no overdraft fee)
    # @param amount: the amount being withdrawn (float)
    # @require: amount > 0
    # @return True if the withdrawl is successful, and False otherwise
     def withdraw(self, amount):
          assert amount > 0, "Withdrawal amount must be positive."
        
          if amount > self.balance:
               print("Withdrawal denied: insufficient dunds.")
               return False
        
          self.balance -= amount
          self.transactions.append(Transaction(self.transactionNumber, "withdrawal", amount))
          self.transactionNumber += 1
          return True
    
     '''def printTransactions(self):
          print("Transaction # %d, amount $%.2f, date %s type: %s" % (self.transactionNumber, self._amount, self._date, self._tType))'''
    
   