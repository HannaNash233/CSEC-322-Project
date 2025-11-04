# checkingAccount.py
#
# authors: Will Wian, Detric Brown, Evan Fannin
#
# date: 10/29/25

class CheckingAccount:
    
    def __init__(self, initBalance=0.0): #Me
        #Initialize the account with an initial balance and empty transaction list
        assert isinstance(initBalance, (int, float))
        self.balance = float(initBalance)
        self.transactions = []
        self.transactions.append(f"Account created with balance: ${self.balance:.2f}")
    
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
        
    def deposit(self, amount): #Me
        #Deposit has to be positive
        assert isinstance(initBalance, (int, float))
        assert amount >= 0
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")
        print(f"${amount:.2f} deposited successfully.")
    
    def calculateInterest(self): #TEST
        pass
    
    def withdraw(self, amount): #TEST
        pass
    
    def transfer(self, fromAccount, amount): #TEST
        pass
    
    def printTransactions(self):
        pass
    
    def writeTransactions(self, filename):
        pass
    
    def readTransactions(self, filename):
        pass
    
    