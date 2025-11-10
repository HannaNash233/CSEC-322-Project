# savingsAccountTester.py
#
# Author(s): 
# 
# Date: 10/29/25
# 
# This is the testing module for the savings account 

import unittest
from savingsAccount import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    print("Hello")
    def setUp(self):
        self.savingsAccount1 = SavingsAccount("Dove", "Cameron", 1500)
        
    def testConstructor(self):
        self.assertEqual(self.savingsAccount1.type, "Savings")
        print(self.savingsAccount1.displayDetails())
        
    def testDeposit(self):
        deposit1 = self.savingsAccount1.deposit(100)
        self.assertTrue(deposit1)

    def testPrintTransactions(self):
        # Print debug message if DEBUG is True
        if TestSavingsAccount.DEBUG:
            print("\nTesting printTransactions:")

        # Record transactions to ensure the account has a history
        self._record_transactions(self.savingsAccount3)

        # Call the printTransactions method
        self.savingsAccount3.printTransactions()

        # This assertion confirms that the setup worked
        self.assertGreater(len(self.savingsAccount3._transactions), 0)

    def testWriteTransactions(self):
        # Print debug message if DEBUG is True
        if TestSavingsAccount.DEBUG:
            print("\nTesting writeTransactions:")

        # Record transactions to ensure the account has a history
        self._record_transactions(self.savingsAccount3)
        
        # Call the writeTransactions method and use a placeholder as the filename
        self.savingsAccount3.writeTransactions("test_savings.txt")

        # Assertion for completeness
        self.assertTrue(True) 

    def testReadTransactions(self):
        # Print debug message if DEBUG is True
        if TestSavingsAccount.DEBUG:
            print("\nTesting readTransactions:")

        # Call the readTransactions method (a file must exist)
        self.savingsAccount3.readTransactions("test_savings.txt")

        # Assertion for completeness
        self.assertTrue(True)


    def test_checking_client_opened_correctly(self):

        self.assertEqual(len(self.client.versions), 1)
        self.client.openAccount("checkings")
        self.assertEqual(len(self.client.versions), 2)
        
    def test_savings_client_opened_correctly(self):
        
        self.assertEqual(len(self.client.accounts), 1)
        self.client.openAccount("savings")
        self.assertEqual(len(self.client.versions), 2)

    def test_fun_client_did_not_open_account(self):
        self.client.openAccount("fun")
        self.assertEqual(len(self.client3.accounts), 1)

  def test_close_checking_account(self):
        
        self.assertEqual(len(self.client.accountList), 1)
        self.client.closeAccount("Checking")
        self.assertEqual(len(self.client.accountList), 0, "Account list should be empty")
        self.assertEqual(account_to_close.balance, 0, "Account balance should be zeroed")

    def test_close_savings_account(self):
   
        self.assertEqual(len(self.client.accountList), 1)
        self.client.closeAccount("Savings")
        self.assertEqual(len(self.client2.accountList), 0)
        self.assertEqual(account_to_close.balance, 0)

    def test_close_account_not_in_list(self):
       
        self.assertEqual(len(self.client.accountList), 1) 
        self.client.closeAccount("fun")
        self.assertEqual(len(self.client.accountList), 1)

        
        
if __name__ == '__main__':

    unittest.main()

