# BankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian
# 
# Date: 9/6/25

# This module defines the BankAccount class


from transaction import Transaction
from abc import ABC, abstractmethod
from AES_CBC import *
from random import randint
import os


class BankAccount(ABC):
    # Attributes (overdraft fee, interest rate, next available account number)
    OVERDRAFT_FEE = 20.00
    INTEREST_RATE = 0.075
    _NEXTACCOUNTNUMBER = 1000

    # Constructs a bank account.
    #@param initBalance: The initial bank account balance (float)
    #@param bType: The type of the bank account (string)
    def __init__(self, initBalance=0.0, bType=" "):
        # Preconditions
        assert isinstance(initBalance, (int, float)), "initBalance must be numeric"
        self.balance = float(initBalance)
        # NOTE: accountNumber will be set by Client (still needs fixed)
        self.accountNumber = None
        # Transaction numbering starts at 100 for each account
        self.transactionNumber = 100
        self.transactions = []
        self.overdrawn = 0
        self.type = bType
        self._iv = os.urandom(16)
        self._key = os.urandom(32)

    # Returns a string that contains the account details
    #@return A human readable string containing the account details
    def __str__(self):
        return (f"Account Number: {self.accountNumber}\n" f"Balance: ${self.balance:.2f}\n")

    # Deposit an amount into the account
    #@param amount: The amount being deposited (float)
    #@return True if the deposit is successful, and False otherwise
    def deposit(self, amount):
        assert isinstance(amount, (int, float))
        assert amount >= 0
        if amount <= 0:
            return False
        else:
            self.balance = self.balance + amount
            balanceTransaction = Transaction(self.transactionNumber, "deposit", amount)
            #self.transactions.append(f"Deposited ${amount:.2f}")
            self.transactions.append(balanceTransaction)
            self.transactionNumber += 1
            return True

    # Calculate the interest and add the interest amount to the account
    #@return True of the interest is successfully calculated, and False otherwise
    @abstractmethod
    def calculateInterest(self):
        pass
        
    # Withdraw an amount from the account
    #@param amount: The amount being withdrawn (float)
    #@return True if the withdrawl is successful, and False otherwise
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Transfer an amount to this account from the account passed as a parameter
    #@param fromAccount: The BankAccount object to transfer the money from
    #@param amount: The amount being transfered
    #@return True if the transfer is successful, and False otherwise
    def tranfer(self, fromAccount, amount):
        assert self.balance > 0
        assert amount > 0
        assert self != fromAccount

        # Create a variable to store the successful withdrawal
        successfulWithdrawal = fromAccount.withdraw(amount)
    
        # If the withdrawal is successful, deposit the specified amount and return true
        if successfulWithdrawal:
            self.deposit(amount)
            return True
    
        # If the withdrawal does not meet the proper conditions, print a message to let the user know
        # that the transfer failed, and return false
        else:
            print("Transfer failed: Withdrawal from the source account was denied.")
            return False 

    def writeTransactions(self):
        assert len(self.transactions) > 0

        # Determine file name based on account type
        if (self.type == "checkings"):
            outFile = open("checkings.txt", "wb")
        else:
            outFile = open("savings.txt", "wb")
        
        transList = [] #the self.transactions
        message = ""
        
        # For each message in the list:
        for i in range(len(self.transactions)):
            message = message + str(self.transactions[i]) + "\n"
            transList.append(i)
            # NOTE: I am assuming CheckingAccount.key/iv should be self._key/self._iv here
            result = encrypt_AES_CBC(message, self._key, self._iv) 
            
            # Write the length of the message to the file.
            outFile.write(str(len(result)).encode())
            outFile.write(b"\n")
            # Write the encrypted message and newline to the file
            outFile.write(result)
            outFile.write(b"\n")
            
            # Append a randomly selected extender to the message (commented out in original)
            # index = randint(0, extenderLength)
            # message = message + messageExtenders[index]
            
        # close the output file
        outFile.close()
            
    def readTransactions(self):
        # NOTE: If this is meant to read all past transactions, it shouldn't assert the list is NOT empty
        # assert len(self.transactions) > 0 
        
        if (self.type == "checkings"):
            inFile = open("checkings.txt", "rb") # Changed outFile to inFile
        else:
            inFile = open("savings.txt", "rb") # Changed outFile to inFile
    
        
        line = inFile.readline() # Changed infile to inFile
        line = line.rstrip()
        line = line.decode()
        
        while line != "" :
            length = int(line)
            data = inFile.read(length) # Changed infile to inFile
            inFile.readline() # Changed infile to inFile
            # NOTE: I am assuming CheckingAccount.key/iv should be self._key/self._iv here
            result = decrypt_AES_CBC(data, self._key, self._iv) 
            
            # The original code had logic to read another line and print debug info.
            # I've streamlined the loop structure. You may need to adjust the next line 
            # if your file format is complex (e.g. including the random extender)
            line = inFile.readline().rstrip().decode()
            
            # The original code used a hardcoded CheckingAccount.DEBUG, I'll remove it 
            # as it should likely be self.DEBUG or a global flag if needed.
            # print("decoded data", result)
  
  


