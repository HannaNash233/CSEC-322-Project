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

  # The setup method creates three bank accounts.
  def setUp(self):
    self.bankAccount1 = BankAccount("John", "Smith", balance)
    self.bankAccount2 = BankAccount("Nancy", "Jackson", balance)
    self.bankAccount3 = BankAccount("Reggie", "Miller", balance)

  
  # The test_constructor method tests the constructor.
  def test_constructor(self):
    pass


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


if __name__ == '__main__':
  unittest.main()
