# checkingAccount.py
#
# authors: Will Wian, Detric Brown, Evan Fannin
#
# date: 10/29/25


from AES_CBC import *
from random import randint

DEBUG = False
messageExtenders = ["ab", "cd", "12", "34", "QWERTY", "WASDX", "dogs", "cats",
"\t"]
extenderLength = len(messageExtenders)-1
._iv = b'MySuperSecretIV0'
._key = b'MySuperSecretKey1222222222222222'

class CheckingAccount:
    
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
    
    def printTransactions(self):
        print("Transaction # %d, amount $%.2f, date %s type: %s" % (self._tNumber, self._amount, self._date, self._tType))
        pass
    
    def writeTransactions(self, filename):
    transList = []
    
    if (self._accountType == "checkings"):
        outFile = open("checkings.txt", "wb")
    else:
        outFile = open("savings.txt", "wb")
# For each message in the list:
   for i in range (len(self._transactions)):
       message = str(self._transactions[i])
       translist.append(i)
       
    result = encrypt_AES_CBC(message, key, iv)

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


        
        pass
    
    def readTransactions(self, filename):

    key = b'MySuperSecretKey1222222222222222'
    print("The length of the key is %d bytes" % len(key))
# Initialization vector (Ensure the IV is 16 bytes)
    iv = b'MySuperSecretIV0'
    print("The length of the Initialization Vector is %d bytes" % len(iv))
# Open the input file to read the encrypted data
    inFile = open("testOutput.txt", "rb")
# read in the the file
    line = inFile.readline()
    line = line.rstrip()
    line= line.decode()
    
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

        
        pass
    
    
