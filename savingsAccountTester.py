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
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()