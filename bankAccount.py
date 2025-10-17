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
  #@require firstName to be 1-25 characters with no special characters
  #@require lastName to be 1-40 characters with no special characters
  #@require accountNumber is greater than or equal to 1000
  def __init__(self, firstName, lastName, initBalance = 0.0, accountNumber = 1000):

    # Assertions
    assert firstName.isalpha and len(firstName) >= 1 and len(firstName) <= 25
    assert lastName.isalpha and len(lastName) >= 1 and len(lastName) <= 40
    assert accountNumber >= 1000
    
    self.firstName = firstName
    self.lastName = lastName
    self.balance = float(initBalance)
    self.accountNumber = BankAccount._NEXTACCOUNTNUMBER
    BankAccount._NEXTACCOUNTNUMBER += 1
    self.transactionNumber = 100
    self.transactions = []
    self.overdrawn = 0


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
    interestEarned = self.balance * self.INTEREST_RATE
    self.balance += interestEarned
    # add the transacation number
    interestTransaction = Transaction(self.transactionNumber, "interest", interestEarned)
    self.transactions.append(interestTransaction)
    self.transactionNumber += 1
    
    if interestEarned:
      return True
    else:
      return False


  # Withdraw an amount from the account
  #@param amount: The amount being withdrawn (float)
  #@return True if the withdrawl is successful, and False otherwise
  def withdraw(self, amount):
    withdrawCheck = self.balance + 250 
    if (amount > withdrawCheck):
      print("Transaction denied\n")
      return False
    elif (self.balance > 0):
      withdrawTransaction = Transaction(self.transactionNumber, "withdrawal", amount)
      self.transactions.append(withdrawTransaction)
      self.overdrawn += 1
      self.balance = self.balance - amount
      print("Transaction Complete")
      return True
    elif (self.balance < 0):
      self.overdrawn += 1
      penaltyTransaction = Transaction("penalty", amount)
      self.transactionNumber += 1
      overdrawnDeduct = self.balance - OVERDRAFT_FEE
      print("Account has been overdrawn\n")
      self.transacations.append(penaltyTransaction)
      return False
    else:
      print("Transaction has been denied\n")
      return False
      


  # Transfer an amount to this account from the account passed as a parameter
  #@param fromAccount: The BankAccount object to transfer the money from
  #@param amount: The amount being transfered
  #@return True if the transfer is successful, and False otherwise
  def tranfer(self, fromAccount, amount):
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



