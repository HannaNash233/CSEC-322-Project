# savingsAccount.py
# 
# authors: Hanna Nash, Victoria Seusankar, Will Wian
#
# Date: 10/29/25

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

class SavingsAccount:
    
    def __init__(self, initBalance=0.0): 
        pass
    
    def displayDetails(self):
        pass
    
    def deposit(self, amount):
        pass
    
    def calculateInterest(self):
        pass
    
    def withdraw(self, amount):
        pass
    
    def transfer(self, fromAccount, amount):
        pass
    
    def printTransactions(self): #Me
        #Print all transactions.
        print("Transaction History:")
        for i in range(len(self.transactions)):
            print(self.transactions[i])    
    
    # Create a list to store the transactions, encrypt the list, return a list.
    def writeTransactions(self, filename): #Me
        # Create a message string to encrypt
        transList = [] #the self.transactions
        # message = 
        
        # assert
        if (self._accountType == "checkings"):
            outFile = open("checkings.txt", "wb")
        else:
            outFile = open("savings.txt", "wb")
        
        # For each message in the list:
        for i in range(len(self.transactions[i])):
            # call the encrypt method, passing it the message
            # store the return value in a variable - "result"
            message = str(self.transactions[i])
            transList.append(i)
            
        result = encrypt_AES_CBC(message, key, iv)
        """
        if DEBUG:
            print(len(result), result)
        """        
        
        # Write the length of the message to the file.
        outFile.write(str(len(result)).encode())
        outFile.write(b"\n")
            
        # Write the encrypted message and newline to the file
        outFile.write(result)
        outFile.write(b"\n")
            
        # Append a randomly selected extender to the message
        index = randint(0, extenderLength)
        message = message + messageExtenders[index]
            
        # close the output file
        outFile.close()        
        
    
    def readTransactions(self, filename): #Me
        # Open the input file to read the encrypted data
        if (self._accountType == "checkings"):
            outFile = open("checkings.txt", "wb")
        else:
            outFile = open("savings.txt", "wb")
        
        # read in the the file
        line = inFile.readline()
        line = line.rstrip()
        line= line.decode()
        """
        if DEBUG:
            print("The input length is: %s:" % (line))
        """
        while line != "" :
            length = int(line)
            data = inFile.read(length)
            inFile.readline()
            result = decrypt_AES_CBC(data, key, iv)
            line = inFile.readline().rstrip().decode()
        if DEBUG:
            print("decoded data", result)
            print("Line is: %s:" % (line))
            
        # Close the input file
        inFile.close()