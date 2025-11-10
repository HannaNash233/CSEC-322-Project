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
class SavingsAccount (BankAccount):
    INTEREST_RATE = 0.04
    
    def __init__(self, firstName, lastName, initBalance=0.0):
        super().__init__(firstName, lastName, initBalance)
        self.type = "Saving"  
    
    def displayDetails(self):
        details = ("First Name: %s \n Last Name: %s \n Balance: %0.2f\n Type: %s" % (self.firstName, self.lastName, self.balance, self.type))
        return details 
    
    # Calculates and applies the monthly 4.0% annual interest.
    # @return: True if the interest was calculated and applied, and False otherwise.
    def calculateInterest(self):
        assert self.INTEREST_RATE > 0, "Interest rate must be positive for calculation."

        # Store the initial state for assertion
        initial_balance = self._balance
        initial_transaction_count = len(self._transactions)
        
        # Calculate the monthly interest rate
        monthly_rate = self.INTEREST_RATE / 12.0
    
        # The interest earned on the balance based on the interest rate
        interestEarned = self._balance * monthly_rate

        if interestEarned > 0:
            # Add the interest earned to the balance
            self._balance += interestEarned
    
            # Create an interest transaction
            interestTransaction = Transaction(BankAccount._nextTransactionNumber, "interest", interestEarned)
        
            # Append the transaction to the transactions list
            self._transactions.append(interestTransaction)
            BankAccount._nextTransactionNumber += 1
            
            print("Interest Applied: %.2f added to Savings Account %d." % (interestEarned, self.getAccountNumber()))

            # ASSERTIONS FOR SUCCESS
            # ASSERTION: The new balance must be the initial balance plus the interest earned.
            assert self._balance == initial_balance + interestEarned, "The interest calculation failed to update the balance."
            # ASSERTION: A new transaction must be added.
            assert len(self._transactions) == initial_transaction_count + 1, "Failed to record the interest transaction."
            
            return True
        
        else:
            # ASSERTIONS FOR FAILURE
            # ASSERTION: The balance must not change.
            assert self._balance == initial_balance, "Balance changed despite no interest being applied."
            # ASSERTION: The transaction count must not change.
            assert len(self._transactions) == initial_transaction_count, "Transaction recorded despite no interest being applied."
            
            return False

    
    # Handles withdrawals, including checks for debt limits and applying tiered overdraft fees.
    # @param amount: The amount to withdraw.
    # @return: True if the withdrawal is successful, and False otherwise.
    def withdraw(self, amount):
        assert isinstance(amount, (int, float)) and amount > 0, "Withdrawal amount must be a positive number."

        # Store the initial state for assertion
        initial_balance = self._balance
        initial_transaction_count = len(self._transactions)
        
        # Check to see if the amount requested is positive
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False

        # Check to see if the current balance can cover the withdrawal
        if self._balance >= amount:            
            # Create the withdrawal transaction
            withdrawalTransaction = Transaction(BankAccount._nextTransactionNumber, "withdrawal", -amount)
            
            # Append the withdrawal to the transactions list
            self._transactions.append(withdrawalTransaction)
            
            # Add to the transaction number
            BankAccount._nextTransactionNumber += 1
            
            # Subtract the amount from the balance
            self._balance -= amount
            
            print("Standard withdrawal complete. New Balance: %.2f" % (self._balance))

            # ASSERTIONS FOR SUCCESS
            assert self._balance == initial_balance - amount, "The withdrawal failed to update the balance correctly."
            assert len(self._transactions) == initial_transaction_count + 1, "Failed to record the withdrawal transaction."
            
            return True

        else:
            # ASSERTIONS FOR FAILURE
            assert self._balance == initial_balance, "The balance changed despite the insufficient funds."
            assert len(self._transactions) == initial_transaction_count, "The transaction recorded despite the insufficient funds."
            
            return False

    
    # Transfers a specified amount from one account (source) to the current account (destination).
    # @param fromAccount: The BankAccount object to withdraw the funds from (the source).
    # @param amount: The amount to transfer.
    # @return: True if the transfer is successful, and False otherwise.
    def transfer(self, fromAccount, amount):
        assert fromAccount is not None, "Source account cannot be None."
        assert isinstance(amount, (int, float)) and amount > 0, "Transfer amount must be a positive number."

        # Store the initial state of the destination account for assertion
        initial_self_balance = self._balance
        initial_self_transactions = len(self._transactions)
        
        # If fromAccount tries to make a transfer to itself, deny the transfer and return false
        if fromAccount is self:
            print("Transfer denied: Cannot transfer to the same account.")
            # ASSERTIONS FOR FAILURE
            assert self._balance == initial_self_balance, "Destination balance changed on self-transfer attempt."
            assert len(self._transactions) == initial_self_transactions, "Destination transaction recorded on self-transfer attempt."
            
            return False
    
        # If the amount being transfered is negative or equal to 0, print a message to let the user know
        # that the amount being transferred needs to be positive, and return false
        if amount <= 0:
            print("Transfer denied: Amount must be positive.")
            # ASSERTIONS FOR FAILURE
            assert self._balance == initial_self_balance, "Destination balance changed on non-positive amount transfer attempt."
            assert len(self._transactions) == initial_self_transactions, "Destination transaction recorded on non-positive amount transfer attempt."
            
            return False
    
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
            # ASSERTIONS FOR FAILURE
            assert self._balance == initial_self_balance, "Destination balance changed when source withdrawal failed."
            assert len(self._transactions) == initial_self_transactions, "Destination transaction recorded when source withdrawal failed."
            
            return False
        

    
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






