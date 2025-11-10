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
    
    BALANCE1 = 1000
    BALANCE2 = 1500
    BALANCE3 = 80000
    DEBUG = True
    
    def setUp(self):
        self.savingsAccount1 = SavingsAccount(TestSavingsAccount.BALANCE1)
        self.savingsAccount2 = SavingsAccount(TestSavingsAccount.BALANCE2)
        self.savingsAccount3 = SavingsAccount(TestSavingsAccount.BALANCE3)
        
    
    def test_constructor(self):
        self.assertEqual(self.savingsAccount1.getBalance(), TestSavingsAccount.BALANCE1)
        self.assertEqual(self.savingsAccount1.getType(), "Savings")
        self.assertEqual(self.savingsAccount2.getBalance(), TestSavingsAccount.BALANCE2)
        self.assertEqual(self.savingsAccount2.getType(), "Savings")
        if TestSavingsAccount.DEBUG:
            print("\nTesting the Constructor")
            print(repr(self.savingsAccount1))
            print(repr(self.savingsAccount2))
            
            
    def test_withdraw(self):
        self.savingsAccount1.withdraw(100)
        try:
            self.savingsAccount2.withdraw(-100)
        except AssertionError:
            print("\nTesting Bad Withdraw (negative)")
            
        self.savingsAccount2.withdraw(1500)
        try:
            self.savingsAccount2.withdraw(200)
        except AssertionError:
            print("\nTesting Bad Withdraw (account balance < 0)")
        
        self.savingsAccount2.deposit(1500)
        self.savingsAccount2.withdraw(1600)
        self.savingsAccount2.withdraw(1700)
        self.savingsAccount3.withdraw(81000)
        self.savingsAccount3.deposit(30000)
            
            
        if TestSavingsAccount.DEBUG:
            print("\nTesting Withdraw")
            print("Account 1 Balance: ", self.savingsAccount1.getBalance())
            print("Account 1 Overdraw Counter: ", self.savingsAccount1.getOverdraft())
            print("\nAccount 2 Balance: ", self.savingsAccount2.getBalance())
            print("Account 2 Overdraw Counter: ", self.savingsAccount2.getOverdraft())
            print("\nAccount 3 Balance: ", self.savingsAccount3.getBalance())
            print("Account 3 Overdraw Counter: ", self.savingsAccount3.getOverdraft())
            
    
    def test_CalculateInterest(self):
        interest1 = self.savingsAccount1.calculateInterest()
        self.savingsAccount2.withdraw(1500)
        self.assertEqual(self.savingsAccount1.getBalance(), 1040.0)
        self.assertTrue(interest1)
        try:
            interest2 = self.savingsAccount2.calculateInterest()
        except AssertionError:
            print("\nTesting negative account interest")
        if TestSavingsAccount.DEBUG:
            print("\nTesting Calculate Interest")
            print("Account 1 Balance: ", self.savingsAccount1.getBalance())
            
    def test_transfer(self):
        transfer1 = self.savingsAccount1.transfer(self.savingsAccount2, 100)
        try:
            transfer2 = self.savingsAccount3.transfer(self.savingsAccount3, 500)
        except AssertionError:
            print("\nTesting Transfer to Self")
            
        self.savingsAccount2.withdraw(1400)
        try:
            transfer3 = self.savingsAccount3.transfer(self.savingsAccount2, 150)
        except AssertionError:
            print("\nTesting Transfer with negative account balance")
            
        try:
            transfer4 = self.savingsAccount2.transfer(self.savingsAccount1, -200)
        except AssertionError:
            print("\nTesting transfer with negative amount")
        
        
        if TestSavingsAccount.DEBUG:
            print("\nTesting Transfer")
            print("Account 1 Balance: ", self.savingsAccount1.getBalance())
    
    def test_displayDetails(self):
        pass
    
    def testWriteTransactions(self):
        # Print debug message if DEBUG is True
        if TestSavingsAccount.DEBUG:
            print("\nTesting writeTransactions:")

        # Record transactions to ensure the account has a history
        # self._record_transactions (self.savingsAccount3)
        
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