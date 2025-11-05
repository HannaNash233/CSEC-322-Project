# savingsAccount.py
# 
# Author(s): Hanna Nash, Victoria Seusankar, Will Wian
#
# Date: 10/29/25
# 
# This is the module that creates the savings account 

from bankAccount import BankAccount


class SavingsAccount (BankAccount): 
  
  INTEREST_RATE = 0.04
  # creating the constructor
  def __init__(self, firstName, lastName, initBalance=0.0, bType="Savings"):
    # inheriting from BankAccount class
    super().__init__(firstName, lastName, initBalance)
    self.type = bType  
        
    
  def displayDetails(self):
    details = ("First Name: %s \n Last Name: %s \n Balance: %0.2f\n Type: %s" % (self.firstName, self.lastName, self.balance, self.type))
    return details  
    
  def calculateInterest(self):
    pass
    
  def withdraw(self, amount):
    pass
    
  def transfer(self, fromAccount, amount):
    pass
    
  def writeTransactions(self, filename):
    pass
    
  def readTransactions(self, filename):
    pass    