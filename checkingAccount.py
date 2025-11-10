# checkingAccount.py
#
# authors: Will Wian, Detric Brown, Evan Fannin
#
# date: 10/29/25

from bankAccount import BankAccount
from transaction import Transaction
from random import randint

# Import for encryption/decryption
from AES_CBC import *

DEBUG = False 
MESSAGE_EXTENDERS = ["ab", "cd", "12", "34", "QWERTY", "WASDX", "dogs", "cats", "\t"]
EXTENDER_LENGTH = len(MESSAGE_EXTENDERS) - 1

# Key and IV placeholders from AES Encrypt Example
KEY = b'MySuperSecretKey1222222222222222'  
IV = b'MySuperSecretIV0'

class CheckingAccount(BankAccount):
    
    # Attributes
    INTEREST_RATE = 0.015
    ACCOUNT_TYPE = "Checking"
    
    def __init__(self, firstName, lastName, initBalance=0.0): 
        super().__init__(firstName, lastName, initBalance)
        #Initialize the account with an initial balance and empty transaction list
        assert isinstance(initBalance, (int, float))
        self.balance = float(initBalance)
        self.transactions = []

        self.transactions.append(self.balance)
    
    def displayDetails(self): 
        details = ("First Name: %s \n Last Name: %s \n Balance: %0.2f\n Type: %s" % (self.firstName, self.lastName, self.balance, ACCOUNT_TYPE))
        return details        
        
    def deposit(self, amount): 
        #Deposit has to be positive
        assert isinstance(amount, (int, float))
        assert amount >= 0
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")
        print(f"${amount:.2f} deposited successfully.")
    
    
    # @override: Apply 1.5% interest rate
    # @require: balance > 0 to earn interest
    # @return True of the interest is successfully calculated, and False otherwise
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
        assert isinstance(amount, (int, float))
        assert amount > 0, "Withdrawal amount must be positive."
        
        if amount > self.balance:
            print("Withdrawal denied: insufficient funds.")
            return False
        
        self.balance -= amount
        self.transactions.append(Transaction(self.transactionNumber, "withdrawal", amount))
        self.transactionNumber += 1
        print("Transaction Complete")
        return True

    # @override: Print all checking account transactions
    # @ensure: all transactions are printed
    def printTransactions(self):
        print("\n Transactions for Checking Account %d" % (self.accountNumber))
    
        # Check if the list of transactions is empty
        if not self.transactions:
            print("No transactions recorded.")
            return
    
        # Iterate through the list of transactions and print them
        for transaction in self.transactions:
            print(transaction)
    
        # Write all checking account transactions to "checking.txt"
        # The data must be encrypted
        # @ensure: all transactions are written and encrypted to "checking.txt"
        def writeTransactions(self):
            filename = "checking.txt"
            
            if not self.transactions:
                print(f"No transactions to write for Account {self.accountNumber}.")
                return
                
            try:
                with open(filename, "wb") as outFile:
                    for transaction in self.transactions:
                        # Get the string representation of the transaction
                        message = str(transaction)
                        
                        # Encrypt the data
                        result = encrypt_AES_CBC(message, KEY, IV)
    
                        # Write the length of the encrypted message
                        outFile.write(str(len(result)).encode())
                        outFile.write(b"\n")
                        
                        # Write the encrypted message
                        outFile.write(result)
                        outFile.write(b"\n")
                        
                        # Append a randomly selected extender
                        index = randint(0, EXTENDER_LENGTH)
                        extender = MESSAGE_EXTENDERS[index]
                        outFile.write(extender.encode('utf-8'))
                        outFile.write(b"\n")
                
                if DEBUG:
                    print(f"Successfully encrypted and wrote {len(self.transactions)} transactions to {filename}")
            except Exception as e:
                print(f"An error occurred while writing transactions: {e}")
    
    
        # Read all checking account transactions from "checking.txt"
        # The data must be decrypted before it is printed
        # @ensure: all transactions from "checking.txt" are read and printed
        def readTransactions(self):
            filename = "checking.txt"
            
            try:
                # Open the file for reading bytes
                inFile = open(filename, "rb")
                print(f"\n--- Reading and Decrypting Transactions from {filename} ---")
                
                # Read the length line
                line = inFile.readline()
                line = line.rstrip()
                line = line.decode()
                
                # Loop while the length line is not empty
                while line != "":
                    # Convert the length string to an integer
                    length = int(line)
                    
                    # Read the encrypted data
                    data = inFile.read(length)
                    
                    # Read the newline after encrypted data (discard)
                    inFile.readline()
                    
                    # Decrypt the data
                    result = decrypt_AES_CBC(data, KEY, IV)
                    
                    # Print the decrypted transaction
                    print(result)
    
                    # Read and discard the extender line
                    inFile.readline()
                    
                    # Read the length of the next message to continue/end the loop
                    line = inFile.readline()
                    line = line.rstrip()
                    line = line.decode()
                
                # Close the input file
                inFile.close()
    
            except FileNotFoundError:
                print(f"File '{filename}' not found.")

        



