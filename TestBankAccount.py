# TestBankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian, Detric Brown
# 
# Date: 9/6/25

# This file tests the functions in the BankAccount.py file

import unittest
from bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
  # Constants used for testing
    INITIAL_BALANCE = 1000.00
    DEPOSIT_AMOUNT = 500.00
    WITHDRAW_AMOUNT = 200.00
    OVERDRAFT_LIMIT = 250.00
    DEBUG = True

    BALANCE1 = 3200
    WITHDRAWL1 = 500
    DEPOSIT1 = 450
    FIRST_NAME1 = "Hank"
    LAST_NAME1 = "Hill"
    
    BALANCE2 = 1500
    WITHDRAWL2 = 1750
    DEPOSIT2 = 200
    FIRST_NAME2 = "Mickey"
    LAST_NAME2 = "Mouse"    

  # The setup method creates bank accounts.
    def setUp(self):
        self.bankAccount1 = BankAccount("John", "Smith", TestBankAccount.INITIAL_BALANCE)
        self.bankAccount2 = BankAccount("Nancy", "Jackson", TestBankAccount.INITIAL_BALANCE)
        self.bankAccount3 = BankAccount("Reggie", "Miller", 50)
        self.account4 = BankAccount(TestBankAccount.FIRST_NAME1, TestBankAccount.LAST_NAME1, TestBankAccount.BALANCE1)
        self.account5 = BankAccount(TestBankAccount.FIRST_NAME2, TestBankAccount.LAST_NAME2, TestBankAccount.BALANCE2)
        # checking that the asserts fail within the account creation
        try:
            self.account6 = BankAccount("D", "P", TestBankAccount.BALANCE1)
            self.account7 = BankAccount("MabelAndDipperPines", "StanfordAndStanleyPines", TestBankAccount.BALANCE1)
        except AssertionError as error:
            print(error)
                

  
  # The test_constructor method tests the constructor.
    def test_constructor(self):
        self.assertEqual(self.account4.firstName, "Hank")
        self.assertEqual(self.account4.lastName, "Hill")
        #self.assertEqual(self.account3, )
        if TestBankAccount.debug:
            print("\nTesting Constructor")
            print("The First Account: ", self.account4)
            print("The Second Account: ", self.account5)  
   


  # Test to see if the transfer is successful
    def testTransferSuccessful(self):
        # Print debug message if DEBUG is True
        if TestBankAccount.DEBUG:
            print("\nTesting a successful transfer:")

        # Define the amount being transferred
        transferAmount = 100.00
        
        # self.bankAccount1 is the receiver
        # self.bankAccount2 is the source sender
        # Attempt to transfer money from bankAccount2 to bankAccount1
        success = self.bankAccount1.tranfer(self.bankAccount2, transferAmount)

        # Assert that the transfer function is successful 
        self.assertTrue(success)

        # Assert that bankAccount1's balance increased after the transfer; it should equal the initial balance plus the transferred amount
        self.assertEqual(self.bankAccount1.balance, TestBankAccount.INITIAL_BALANCE + transferAmount)

        # Assert that bankAccount2's balance decreased after the transfer; it should equal the initial balance minus the transferred amount
        self.assertEqual(self.bankAccount2.balance, TestBankAccount.INITIAL_BALANCE - transferAmount)


   # Test to see if the transfer is denied 
    def testTransferDenied(self):
        if TestBankAccount.DEBUG:
            print("\nTesting to see if the transfer is denied due to insufficient funds:")
            
        # bankAccount3 has $50.00
        # The max withdraw is $50 + $250 = $300
        transferAmount = 300.01 
        
        # Attempt to transfer money from bankAccount3 to bankAccount1
        success = self.bankAccount1.tranfer(self.bankAccount3, transferAmount)
        
        # Assert that the transfer failed
        #print("Trannsfer denied: ", success)
        self.assertFalse(success)
        
        # Assert that bankAccount1's balance does not change
        self.assertEqual(self.bankAccount1.balance, TestBankAccount.INITIAL_BALANCE)
        
        # Assert that bankAccount3's balance does not change (aka the withdrawal failed)
        self.assertEqual(self.bankAccount3.balance, 50.00)


    # Test the printTransactions method 
    def testPrintTransactions(self):
        # Print debug message if DEBUG is True
        if TestBankAccount.DEBUG:
            print("\nTesting printTransactions:")

        # Record a deposit and a withdrawal to ensure the account has a transaction history in order to test the printTransactions method
        self.bankAccount3.deposit(50.00)
        self.bankAccount3.withdraw(20.00)

        # Call the printTransactions method for bankAccount3
        self.bankAccount3.printTransactions()

        # Assert that the transactions list actually contains the recorded transactions
        self.assertGreater(len(self.bankAccount3.transactions), 0)

    
   
    def test_calculateInterest(self):
        # creating the interest test
        interestTest1 = self.account4.calculateInterest()
        # checking that its equal to 3440 (the balance + the interest earned)
        self.assertEqual(self.account4.balance, 3440)
        
        # printing the information if debug is true 
        if TestBankAccount.debug:
            print("\nTesting Calculate Interest")
            print("First Account After Interest", self.account4.balance)
           
    
    
    def test_withdrawl(self):
        # creating three different withdrawl tests (one to pass, one to overdraw,
        # one to deny it completely) 
        withdrawlTest1 = self.account4.withdraw(TestBankAccount.WITHDRAWL1)
        withdrawlTest2 = self.account5.withdraw(TestBankAccount.WITHDRAWL2)
        withdrawlTest3 = self.account4.withdraw(5000)
        
        self.assertEqual(self.account4.balance, 2700)
        self.assertFalse(withdrawlTest2)
        self.assertFalse(withdrawlTest3)
        # printing out the balances after the tests if debug is true
        if TestBankAccount.debug:
            print("\nTesting Withdraw")
            print("First Account Balance After Withdraw", self.account4.balance)
            print("Second Account Balance After Withdraw ", self.account5.balance)
            
        
        
        
if __name__ == '__main__':
    unittest.main()
        
