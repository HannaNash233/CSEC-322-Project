# BankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian
# 
# Date: 9/6/25

# This module defines the BankAccount class


from transaction import Transaction
from abc import ABC, abstractmethod

class BankAccount:
  # Attributes (overdraft fee, interest rate, next available account number)
  OVERDRAFT_FEE = 20.00
  INTEREST_RATE = 0.075
  _NEXTACCOUNTNUMBER = 1000
  
  

  
  # Constructs a bank account.
  #@param firstName: The first name of the account holder
  #@param lastName: The last name of the account holder
  #@param initBalance: The initial bank account balance (float)
  # @require: The length of the first name has to be in between 1 and 25
  # @require: The length of the last name has to be in between 1 and 40
  def __init__(self, initBalance=0.0, bType = " "):
    self.balance = float(initBalance)
    self.accountNumber = BankAccount._NEXTACCOUNTNUMBER
    BankAccount._NEXTACCOUNTNUMBER += 1
    self.transactionNumber = 100
    self.transactions = []
    self.overdrawn = 0
    self.type = bType


  # Returns a string that contains the account details (first & last name, account number, balance, overdrawn counter)
  #@return A human readable string containing the account details
  def __str__(self):
    return (f"Account Number: {self.accountNumber}\n"
                f"Balance: ${self.balance:.2f}\n")


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
  @abstractmethod
  def tranfer(self, fromAccount, amount):
    pass



  # Print the list of transactions for an account
  def printTransactions(self):
    print("\n Transactions for Account %d" % (self.accountNumber))

    # Check if the list of transactions is empty
    if not self.transactions:
      print("No transactions recorded.")
      return

    # Iterate through the list of transactions and print them
    for transaction in self.transactions:
      print(transaction)
      
  # initializing the getters 
  def getAccountNumber(self):
      return self.accountNumber  
   
  def getBalance(self):
      return self.balance 
      
  def getTransactions(self):
      return self.transactions 
      
  def getBalance(self):
      return self.balance   
  
  def getOverdraft(self):
      return self.overdrawn
    
  def getType(self):
      return self.type
    
 
  # creating the string representation 
  def __str__(self):
    return ("Account Number: %d Balance: %0.2f" % (self.accountNumber, self.balance))
  
  # creating the machine representation
  def __repr__(self):
    return ("BankAccount(balance = %d)" % self.balance)
  
  # creating the special methods (equality and non-equality)
  def __eq__(self, other):
    result = (self.balance == other.balance) and (self.accountNumber == other.accountNumber) and (self.transactions == other.transactions)
    return result
  
  def __ne__(self, other):
    result = (self.balance != other.balance) or (self.accountNumber != other.accountNumber) or (self.transactions != other.transactions)
    return result
  
  def __gt__(self, other):
    result =  (self.balance > other.balance) or (self.accountNumber > other.accountNumber)
    return result   
  
  


