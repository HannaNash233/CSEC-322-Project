# checkingAccountTester.py
#
# Authors:
#
# Date: 11/5/25
#
# This is the testing module for the checking account class.

import unittest
from checkingAccount import CheckingAccount

class testCheckingAccount(unittest.TestCase):
    print("Hello")
    
    # Structural flag for debug messages
    DEBUG = False
    
    def setUp(self):
        # Setup an account for testing
        self.checkAccount1 = CheckingAccount(1000.00)
        
    def testConstructor(self):
        # Assert the initial balance is correct
        self.assertEqual(self.checkAccount1.balance, 1000.00)
        # Assert that the initial transaction log entry was created
        self.assertGreater(len(self.checkAccount1.transactions), 0)
        
        # Display details 
        print("\n--- Test Constructor Details ---")
        self.checkAccount1.displayDetails()
        
    def testDisplayDetails(self):
        # Print debug message if DEBUG is True
        if TestCheckingAccount.DEBUG:
            print("\nTesting displayDetails:")

        # Record a transaction to ensure there is history to display
        self.checkAccount1.deposit(50.00)
        
        # Call the displayDetails method
        self.checkAccount1.displayDetails()

        # Assertion that confirms there is data to display.
        self.assertGreater(len(self.checkAccount1.transactions), 1)

    def testDeposit(self):
        # Record the initial transaction count
        initial_transaction_count = len(self.checkAccount1.transactions)
        
        # Perform the deposit
        self.checkAccount1.deposit(200.00)
        
        # Assert the balance updated correctly (1000 + 200 = 1200)
        self.assertEqual(self.checkAccount1.balance, 1200.00)
        
        # Assert a new transaction was recorded
        self.assertEqual(len(self.checkAccount1.transactions), initial_transaction_count + 1)


if __name__ == '__main__':
    unittest.main()
