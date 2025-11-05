def setUp(self):
  self.bankAccount1 = BankAccount(savings)
  self.bankAccount2 = BankAccount(checkings)
  self.bankAccount3 = BankAccount(forFun)

def TestOpenAccount(self):
  self.assertEqual(getAccountType(self),bankAccount1)
  self.assertEqual(getAccountType(self),bankAccount2)
  self.assertEqual(getAccountType(self),bankAccount3)



def TestCloseAccount(self):
  the







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



def TestInit(self):
  the


def TestDisplayDetails(self):
  the

def TestDeposit():
  the
  





