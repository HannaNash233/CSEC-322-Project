# checkingAccount.py
#
# authors: Will Wian, Detric Brown, Evan Fannin
#
# date: 10/29/25

from bankAccount import BankAccount
from transaction import Transaction

class CheckingAccount(BankAccount):
    
    # Attributes
    INTEREST_RATE = 0.015
    
    def __init__(self, initBalance=0.0):
        pass
    
    # @override: Apply 1.5% interest rate
    # @require: balance > 0 to earn interest
    def calculateInterest(self):
        if self.balance <= 0:
            return False
        
        assert self.balance > 0, "Interest cannot be applied to negative or zero balance."
        
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
    
    def printTransactions(self):
        pass
    
    def writeTransactions(self, filename):
        pass
    
    def readTransactions(self, filename):
        pass

    
