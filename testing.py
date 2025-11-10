
import unittest 
from checkingAccount import CheckingAccount
from client import*
from savingsAccount import SavingsAccount


def setUp(self):
        address = ("168 Pelham Place", "Norfolk", "VA")
        self.client = Client("Cara", "Routh", "7576767679", address, "Checking")
         self.client2 = Client("Cara", "Routh", "7576767679", address, "Checking")
        # print(self.client.printAccount())

def test_checking_client_opened_correctly(self):

        self.assertEqual(len(self.client.versions), 1)
        
        # That account should be a CheckingAccount
        self.client.openAccount("checkings")
        self.assertEqual(len(self.client.versions), 2)


    def test_savings_client_opened_correctly(self):

        self.assertEqual(len(self.client.accounts), 1)
        
        # That account should be a SavingsAccount
        self.client.openAccount("savings")
        self.assertEqual(len(self.client.versions), 2)

    def test_fun_client_did_not_open_account(self):
        self.client.openAccount("fun")

        self.assertEqual(len(self.client3.accounts), 1)

  def test_close_checking_account(self):
        
        # 1. Check initial state (client has 1 account)
        self.assertEqual(len(self.client.accountList), 1)
        
        #
        
        # 3. Run the method
        self.client.closeAccount("Checking")
        
        self.assertEqual(len(self.client.accountList), 0, "Account list should be empty")
        self.assertEqual(account_to_close.balance, 0, "Account balance should be zeroed")

    def test_close_savings_account(self):
   
        self.assertEqual(len(self.client.accountList), 1)
        

        # 3. Run the method
        self.client.closeAccount("Savings")
        
        # 4. Check results
        self.assertEqual(len(self.client2.accountList), 0)
        self.assertEqual(account_to_close.balance, 0)

    def test_close_account_not_in_list(self):
       
        
        # 2. Check that client1's list is not empty
        self.assertEqual(len(self.client.accountList), 1)

        #
        self.client.closeAccount("fun")

        # 4. Make sure client1's list was not changed
        self.assertEqual(len(self.client.accountList), 1)

  



  def testConstructor(self):
        # Assert the initial balance is correct
        self.assertEqual(self.savingsAccount1.balance, 1000.00)
        # Assert that the initial transaction log entry was created
        self.assertGreater(len(self.checkAccount1.transactions), 0)
        
        # Display details 
        print("\n--- Test Constructor Details ---")
        self.checkAccount1.displayDetails()

import unittest
# Import the class we want to test
from bank_accounts import SpecificAccount

class TestSpecificAccount(unittest.TestCase):

    # --- Tests for the __init__ method ---
    
    def test_init_with_defaults(self):
        self.SavingsAccount()
        account = SpecificAccount("John", "Doe")
        
        # Check that all attributes are set correctly
        self.assertEqual(account.firstName, "John")
        self.assertEqual(account.lastName, "Doe")
        self.assertEqual(account.balance, 0.0)
        self.assertEqual(account.type, "Savings") # The default bType

    def test_init_with_specific_values(self):
        """
        Test Case 2: Create an account with all args specified.
        """
        # Create the account with all args
        account = SpecificAccount("Jane", "Smith", 150.75, "Checking")
        
        # Check that all attributes are set correctly
        self.assertEqual(account.firstName, "Jane")
        self.assertEqual(account.lastName, "Smith")
        self.assertEqual(account.balance, 150.75)
        self.assertEqual(account.type, "Checking") # The specified bType

    # --- Tests for the displayDetails method ---

    def test_display_details_specific(self):
        """
        Test Case 3: Check the output of displayDetails for a specific account.
        """
        account = SpecificAccount("Jane", "Smith", 150.75, "Checking")
        
        # Define the exact string we expect
        expected_string = (
            "First Name: Jane \n "
            "Last Name: Smith \n "
            "Balance: 150.75\n "  # Note the 0.2f formatting
            "Type: Checking"
        )
        
        # Check that the method's return value matches
        self.assertEqual(account.displayDetails(), expected_string)

    def test_display_details_default(self):
        """
        Test Case 4: Check the output of displayDetails for a default account.
        """
        account = SpecificAccount("John", "Doe")
        
        # Define the exact string we expect
        expected_string = (
            "First Name: John \n "
            "Last Name: Doe \n "
            "Balance: 0.00\n "  # Note the 0.2f formatting
            "Type: Savings"
        )
        
        # Check that the method's return value matches
        self.assertEqual(account.displayDetails(), expected_string)

# This is the "runner" that starts the tests
if __name__ == '__main__':
    unittest.main()
    

  





