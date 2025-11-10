# checkingsAccountTester.py
# 
# Author(s): 
#
# Date: 10/29/25


    # checkingAccountTester.py
#
# Authors:
#
# Date: 11/5/25
#
# This is the testing module for the checking account class.


from checkingAccount import CheckingAccount
import unittest
import os

class testCheckingAccount(unittest.TestCase):
    
    # Constants
    INITIAL_BALANCE = 1000.00
    DEPOSIT_AMOUNT = 500.00
    WITHDRAW_AMOUNT = 200.00
    # Structural flag for debug messages
    DEBUG = False    
    
    print("Hello")
    
    
    def setUp(self):
        # Setup an account for testing
        self.checkAccount1 = CheckingAccount(1000.00)
        self.checkAccount2 = CheckingAccount(testCheckingAccount.INITIAL_BALANCE)
        
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
        if testCheckingAccount.DEBUG:
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
        
    
    # Test printing when transactions exist
    def test_printTransactions_success(self):
        # Arrange
        self.checkAccount2.deposit(10.00)
            
        # Act/Assert: Verify method runs without error
        self.checkAccount2.printTransactions()
        self.assertGreater(len(self.checkAccount2.transactions), 0)
            
    # Test printing when no transactions exist
    def test_printTransactions_failure(self):
        # Arrange: Create a temporary account and clear the initial transaction
        tempAccount = CheckingAccount(0.0)
        tempAccount.transactions = [] 
        
        # Act/Assert: Verify method runs without error on empty list
        tempAccount.printTransactions()
        self.assertEqual(len(tempAccount.transactions), 0)
    
    
    # Test writing when transactions exist
    def test_file_write_success(self):
        # Arrange
        self.checkAccount2.deposit(50.00)
        
        # Act
        self.checkAccount2.writeTransactions("checking.txt")
        
        # Assert
        self.assertTrue(os.path.exists("checking.txt"))
    
    # Test writing when no transactions exists
    def test_file_write_no_transactions(self):
        # Arrange: Create a temporary account and clear the initial transaction
        tempAccount = CheckingAccount(0.0)
        tempAccount.transactions = [] 
        
        # Act
        tempAccount.writeTransactions("checking.txt")
        
        # Assert
        self.assertFalse(os.path.exists("checking.txt"))
    
    # Test reading a successful file
    def test_file_read_success(self):
        # Arrange: Ensure a file exists
        self.checkAccount2.deposit(50.00)
        self.checkAccount2.writeTransactions("checking.txt")
        
        # Act: Verify method runs without error
        self.checkAccount2.readTransactions("checking.txt")
        
    # Test reading when file not found
    def test_file_read_file_not_found(self):
        # Arrange: Ensure the file is deleted
        if os.path.exists("checking.txt"):
            os.remove("checking.txt")
            
        # Act: Verify method runs without error
        self.checkAccount2.readTransactions("checking.txt")    



if __name__ == '__main__':
    unittest.main()
