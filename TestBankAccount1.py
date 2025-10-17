# TestBankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian
# 
# Date: 9/6/25

# This file tests the functions in the BankAccount.py file

import unittest
from bankAccount import BankAccount
from transaction import Transaction

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.acc1 = BankAccount("William", "Wian", 1000000)
        
        print(f"Account Balance: ${self.acc1.balance:.2f}\n")
        
    def testDeposit(self):
        # Should work
        self.assertTrue(self.acc1.deposit(500000)) 
        self.assertEqual(self.acc1.balance, 1500000.0)
        print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
        # Should not work
        self.assertFalse(self.acc1.deposit(-10)) 
        self.assertEqual(self.acc1.balance, 1500000.0)
        print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
    def testWithdrawl(self):
        # Should work and remove money from acc1
        self.acc1.withdraw(500000)
        self.assertEqual(self.acc1.balance, 500000.0)
        print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
        # Should be equal to the first withdrawl
        self.acc1.withdraw(2000000)
        self.assertEqual(self.acc1.balance, 500000)
        print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
    def testOverdraft(self):
        # Should not work
        self.acc1.withdraw(1000001)
        self.assertEqual(self.acc1.balance, -1.0)
        print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
    
if __name__ == '__main__':
    unittest.main()    