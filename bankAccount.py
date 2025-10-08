# BankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian
# 
# Date: 9/6/25

# This module defines the BankAccount class

class BankAccount:
  # Attributes (overdraft fee, interest rate, next available account number)
  OVERDRAFT_FEE = 20.00
  INTEREST_RATE = 0.075
  _NEXTACCOUNTNUMBER = 1000

  
  # Constructs a bank account.
  @param firstName: The first name of the account holder
  @param lastName: The last name of the account holder
  @param initBalance: The initial bank account balance (float)
  def __init__(firstName, lastName, initBalance = 0.0):
    self.firstName = firstName
    self.lastName = lastName
    self.balance = float(initBalance)
    self.accountNumber = BankAccount._NEXTACCOUNTNUMBER
    BankAccount._NEXTACCOUNTNUMBER += 1
    self.transactions = []


  # Returns a string that contains the account details (first & last name, account number, balance, overdrawn counter)
  @return A human readable string containing the account details
  def __str__(self):
    return (f"Account Holder: {self.firstName} {self.lastName}\n"
                f"Account Number: {self.accountNumber}\n"
                f"Balance: ${self.balance:.2f}\n")


  # Deposit an amount into the account
  @param amount: The amount being deposited (float)
  @return True if the deposit is successful, and False otherwise
  def deposit(self, amount):
    if amount <= 0:
      return False
    else:
      self.balance = self.balance + amount
      self.transactions.append(f"Deposited ${amount:.2f}")
      return True


  # Calculate the interest and add the interest amount to the account
  @return True of the interest is successfully calculated, and False otherwise
  def calculateInterest(self):
    pass


  # Withdraw an amount from the account
  @param amount: The amount being withdrawn (float)
  @return True if the withdrawl is successful, and False otherwise
  def withdraw(self, amount):
    pass


  # Transfer an amount to this account from the account passed as a parameter
  @param fromAccount: The BankAccount object to transfer the money from
  @param amount: The amount being transfered
  @return True if the transfer is successful, and False otherwise
  def tranfer(self, fromAccount, amount):
    pass


  # Print the list of transactions for an account
  def printTransactions(self):
    pass



