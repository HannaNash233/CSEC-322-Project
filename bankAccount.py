# BankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian
# 
# Date: 9/6/25

# This module defines the BankAccount class

from transaction import Transaction

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
  def __init__(self, initBalance=0.0):
    assert isinstance(initBalance, (int, float))
    assert initBalance >= 0.0, "Initial balance cannot be negative."
    self.balance = float(initBalance)
    self.accountNumber = BankAccount._NEXTACCOUNTNUMBER
    BankAccount._NEXTACCOUNTNUMBER += 1
    self.transactionNumber = 100
    self.transactions = []
    self.overdrawn = 0
    
    self.accountType = "Base" # Placeholder, will be overriden by Checking/Savings


  # Returns a string that contains the account details (first & last name, account number, balance, overdrawn counter)
  #@return A human readable string containing the account details
  def __str__(self):
    return (f"Account Holder: {self.firstName} {self.lastName}\n"
                f"Account Number: {self.accountNumber}\n"
                f"Balance: ${self.balance:.2f}\n")


  # Deposit an amount into the account
  #@param amount: The amount being deposited (float)
  #@return True if the deposit is successful, and False otherwise
  def deposit(self, amount):
    assert isinstance(amount,(int, float))
    assert amount > 0, "Deposit amount must be positive."
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
  def calculateInterest(self):
    # the interest earned on the balance based on the interest rate
    interestEarned = self.balance * BankAccount.INTEREST_RATE
    # adding the interest earned to the balance 
    self.balance += interestEarned
    # creating an interest transaction 
    interestTransaction = Transaction(self.transactionNumber, "interest", interestEarned)
    # appending the transaction to the transactions list
    self.transactions.append(interestTransaction)
    self.transactionNumber += 1
    
    return True

  # Withdraw an amount from the account
  #@param amount: The amount being withdrawn (float)
  #@return True if the withdrawl is successful, and False otherwise
  def withdraw(self, amount):
    assert isinstance(amount, (int, float))
    assert amount > 0, "Withdrawal amount must be positive."
    # creating a variable to check the balance + 250
    withdrawCheck = self.balance + 250 
    # checking if the amount is less than the withdraw check
    if (amount > withdrawCheck):
      print("Transaction denied\n")
      return False
    
    # checking if that the balance is greater than zero
    elif (self.balance > 0):
      # creating the withdraw transaction 
      withdrawTransacation = Transaction(self.transactionNumber, "withdrawal", amount)
      # appending the withdraw to the transactions list 
      self.transactions.append(withdrawTransacation)
      
      # adding to the transaction number
      self.transactionNumber += 1
      # subtracting the amount from the balance 
      self.balance = self.balance - amount
      
      # checking if the balance is less than 0 
      if (self.balance < 0):
        # adding to the overdrawn counter
        self.overdrawn += 1
        
        # creating a penalty transaction 
        penaltyTransaction = Transaction(self.transactionNumber, "penalty", amount)
        
        # adding to the transaction number
        self.transactionNumber += 1
        # subtract from the balance with the overdraft fee
        overdrawnDeduct = self.balance - BankAccount.OVERDRAFT_FEE
        
        print("Account has been overdrawn\n")
        return False
      
      else: 
        print("Transaction Complete")
        return True

    else:
      print("Transaction has been denied\n")
      return False
      


  # Transfer an amount to this account from the account passed as a parameter
  #@param fromAccount: The BankAccount object to transfer the money from
  #@param amount: The amount being transfered
  #@return True if the transfer is successful, and False otherwise
  def tranfer(self, fromAccount, amount):
    assert isinstance(amount, (int, float))
    assert amount > 0, "Transfer amount must be positive."
    # If fromAccount tries to make a transfer to itself, deny the transfer and return false
    if fromAccount is self:
      print("Transfer denied: Cannot transfer to the same account.")
      return False

    # If the amount being transfered is negative or equal to 0, print a message to let the user know
    # that the amount being transferred needs to be positive, and return false
    if amount <= 0:
      print("Transfer denied: Amount must be positive.")
      return False

    # Create a variable to store the successful withdrawal
    successfulWithdrawal = fromAccount.withdraw(amount)

    # If the withdrawal is successful, deposit the specified amount, and return true
    if successfulWithdrawal:
      self.deposit(amount) 
      return True

    # If the withdrawal does not meet the proper conditions, print a message to let the user know
    # that the transfer failed, and return false
    else:
      print("Transfer failed: Withdrawal from the source account was denied.")
      return False



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
      
  # initializing the getters (removed getFirst and getLast)
      
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
    
  # removed setters - setFirst and setLast
      
  # creating the string representation 
  def __str__(self):
    return ("Account Holder: %s %s Account Number: %d Balance: %0.2f" % (self.firstName, self.lastName, self.accountNumber, self.balance))
  
  # creating the machine representation
  def __repr__(self):
    return ("BankAccount(firstName = %s, lastName = %s, balance = %d)" % self.firstName, self.lastName, self.balance)
  
  # creating the special methods (equality and non-equality)
  def __eq__(self, other):
    result = (self.firstName == other.firstName) and (self.lastName == other.lastName) and (self.balance == other.balance)
    return result
  
  def __ne__(self, other):
    result = (self.firstName != other.firstName) or (self.lastName != other.lastName) or (self.balance != other.balance)
    return result
  
  

