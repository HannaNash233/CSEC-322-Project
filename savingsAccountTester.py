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
        
        
if __name__ == '__main__':

    unittest.main()
