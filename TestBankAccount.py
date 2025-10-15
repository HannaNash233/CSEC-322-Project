# TestBankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian
# 
# Date: 9/6/25

# This file tests the functions in the BankAccount.py file

import unittest
from bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    
    BALANCE1 = 3200
    WITHDRAWL1 = 500
    DEPOSIT1 = 450
    DEBUG = True
    FIRST_NAME1 = "Hank"
    LAST_NAME1 = "Hill"
    
    BALANCE2 = 1500
    WITHDRAWL2 = 1750
    DEPOSIT2 = 200
    FIRST_NAME2 = "Mickey"
    LAST_NAME2 = "Mouse"
    
    def setUp(self):
        self.account1 = BankAccount(TestBankAccount.FIRST_NAME1, TestBankAccount.LAST_NAME1, TestBankAccount.BALANCE1)
        self.account2 = BankAccount(TestBankAccount.FIRST_NAME2, TestBankAccount.LAST_NAME2, TestBankAccount.BALANCE2)
        
        
    def test_calculateInterest(self):
            
            
        interestTest1 = self.account1.calculateInterest()
        interestTest2 = self.account2.calculateInterest()
        self.assertEqual(self.account1.balance, 3440)
        self.assertEqual(self.account2.balance, 1612.50)
        
        if TestBankAccount.debug:
            print("\nTesting Calculate Interest")
            print("First Account After Interest", self.account1.balance)
            print("Second Account After Interest", self.account2.balance)
        
    def test_constructor(self):
        self.assertEqual(self.account1.firstName, "Hank")
        self.assertEqual(self.account1.lastName, "Hill")
        if TestBankAccount.debug:
            print("\nTesting Constructor")
            print("The First Account: ", self.account1)
            print("The Second Account: ", self.account2)
    
    def test_withdrawl(self):
       
        withdrawlTest1 = self.account1.withdraw(TestBankAccount.WITHDRAWL1)
        withdrawlTest2 = self.account2.withdraw(TestBankAccount.WITHDRAWL2)
        self.assertEqual(self.account1.balance, 2700)
        self.assertFalse(withdrawlTest2)
        if TestBankAccount.debug:
            print("\nTesting Withdraw")
            print("First Account Balance After Withdraw", self.account1.balance)
            print("Second Account Balance After Withdraw ", self.account2.balance)
            
            
 
            
            
        
        
        
if __name__ == '__main__':
    unittest.main()
        
    
