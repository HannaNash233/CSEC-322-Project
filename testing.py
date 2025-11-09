
import unittest 
from checkingAccount import CheckingAccount
from client import*
from savingsAccount import SavingsAccount


def setUp(self):
        address = ("168 Pelham Place", "Norfolk", "VA")
        self.client = Client("Cara", "Routh", "7576767679", address, "Checking")
        
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

  


    

  





