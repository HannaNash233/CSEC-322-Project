# savingsAccount.py
# 
# Author(s): Hanna Nash, Victoria Seusankar, Will Wian
#
# Date: 10/29/25
# 
# This is the module that creates the savings account 

from bankAccount import BankAccount
from transaction import Transaction
from AES_CBC import *
from random import randint

DEBUG = False


class SavingsAccount (BankAccount): 
  
  # Random Encryption key (Ensure the key is 32 bytes)
  key = os.urandom(32)
  #print("The length of the key is %d bytes" % len(key))
  
  # Random Initialization Vector (Ensure the IV is 16 bytes)
  iv = os.urandom(16)
  #print("The length of the Initialization Vector is %d bytes" % len(iv))  
  
  INTEREST_RATE = 0.04
  ACCOUNT_TYPE = "Savings"
  _NEXTACCOUNTNUMBER = 1000
  OVERDRAFT_FEE = 20.00
  # creating the constructor
  def __init__(self, initBalance=0.0):
    # inheriting from BankAccount class
    super().__init__(initBalance)
    assert isinstance(initBalance, (int, float))
    assert initBalance >= 0.0, "Initial Balance Cannot be Negative"
    self.accountNumber = SavingsAccount._NEXTACCOUNTNUMBER
    SavingsAccount._NEXTACCOUNTNUMBER += 1  
    self.transactionNumber = 100
    self.balance = float(initBalance)
    self.transactions = []
    self.type = "Savings"
    #self.type = bType
    self.overdrawn = 0

    self.transactions.append(f"Account created with balance: ${self.balance:.2f}") 
        
    
  def displayDetails(self):
    print(f"Current balance: ${self.balance:.2f}")
    print("Recent transactions:")
    print("\n Transactions for Account %d" % (self.accountNumber))
    
        # Check if the list of transactions is empty
    if not self.transactions:
      print("No transactions recorded.")
      return
        
    for transaction in self.transactions:
      print(transaction)        
    
   # Calculates and applies the monthly 4.0% annual interest.
    # @return: True if the interest was calculated and applied, and False otherwise.
  def calculateInterest(self):
      # Calculate the monthly interest rate
      assert self.INTEREST_RATE > 0
      assert self.balance > 0
      #monthly_rate = self.INTEREST_RATE / 12.0
    
      # The interest earned on the balance based on the interest rate
      interestEarned = self.balance * SavingsAccount.INTEREST_RATE

      if interestEarned > 0:
            # Add the interest earned to the balance
          self.balance += interestEarned
    
            # Create an interest transaction
          interestTransaction = Transaction(self.transactionNumber, "interest", interestEarned)
        
            # Append the transaction to the transactions list
          self.transactions.append(interestTransaction)
          self.transactionNumber += 1
            
          print("Interest Applied: %.2f added to Savings Account %d." % (interestEarned, self.getAccountNumber()))
          return True
        
      else:
          print("No interest applied to Savings Account %d due to negative balance." % (self.getAccountNumber()))
          return False

    
    # Handles withdrawals, including checks for debt limits and applying tiered overdraft fees.
    # @param amount: The amount to withdraw.
    # @return: True if the withdrawal is successful, and False otherwise.
  def withdraw(self, amount):
        # Check to see if the amount requested is positive
    assert self.balance > 0 
    assert amount > 0
    assert isinstance(amount, (int, float)) and amount > 0
    # Check to see if the current balance can cover the withdrawal
    if self.balance >= amount:            
      # Create the withdrawal transaction
      withdrawalTransaction = Transaction(self.transactionNumber, "withdrawal", amount)
            
      # Append the withdrawal to the transactions list
      self.transactions.append(withdrawalTransaction)
            
      # Add to the transaction number
      self.transactionNumber += 1
            
      # Subtract the amount from the balance
      self.balance -= amount
      print("Standard withdrawal complete. New Balance: %.2f" % (self.balance))
      return True
    
    elif self.balance >= 10000:
      self.overdrawn = 0
    
    else:
      if (self.overdrawn == 1):
        penaltyTransacation = Transaction(self.transactionNumber, "penalty", SavingsAccount.OVERDRAFT_FEE)
        self.transactions.append(penaltyTransaction)
        self.overdrawn += 1
        self.balance -= SavingsAccount.OVERDRAFT_FEE        
      elif (self.overdrawn == 2):
        self.overdrawn += 1
        self.balance -= 30
        penaltyTransaction = Transaction(self.transactionNumber, "Penalty", 30)
        self.transactions.append(penaltyTransaction)
        
      elif (self.overdrawn == 3):
        self.overdrawn += 1
        self.balance -= 50
        penaltyTransaction = Transaction(self.transactionNumber, "Penalty", 50)
        self.transactions.append(penaltyTransaction)  
      
        
    
   

    
    # 
    # 
  def transfer(self, fromAccount, amount):
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
        
    

    # Create a list to store the transactions, encrypt the list, return a list.
  def writeTransactions(self, filename): #Me
        # Create a message string to encrypt
        transList = [] #the self.transactions
        # message = 
        
        # assert
        if (self.type == "checkings"):
            outFile = open("checkings.txt", "wb")
        else:
            outFile = open("savings.txt", "wb")
        
        # For each message in the list:
        for i in range(len(self.transactions)):
            # call the encrypt method, passing it the message
            # store the return value in a variable - "result"
            message = str(self.transactions[i])
            transList.append(i)
            
        result = encrypt_AES_CBC(message, SavingsAccount.key, SavingsAccount.iv)
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
        #index = randint(0, extenderLength)
        #message = message + messageExtenders[index]
            
        # close the output file
        outFile.close()        
        
    
  def readTransactions(self, filename): #Me
        # Open the input file to read the encrypted data
        if (self.type == "checkings"):
            outFile = open("checkings.txt", "rb")
        else:
            outFile = open("savings.txt", "rb")
        
        # read in the the file
        line = outFile.readline()
        line = line.rstrip()
        line= line.decode()
        """
        if DEBUG:
            print("The input length is: %s:" % (line))
        """
        while line != "" :
            length = int(line)
            data = outFile.read(length)
            outFile.readline()
            result = decrypt_AES_CBC(data, SavingsAccount.key, SavingsAccountiv)
            line = outFile.readline().rstrip().decode()
        if DEBUG:
            print("decoded data", result)
            print("Line is: %s:" % (line))
            
        # Close the input file

        outFile.close() 
        
  def __repr__(self):
    return ("SavingsAccount(balance = %d)" % self.balance)  

