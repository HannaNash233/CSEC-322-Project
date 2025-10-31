# TestBankAccount.py
# 
# Authors: Hanna Nash, Victoria Seusankar, Will Wian, Detric Brown
# 
# Date: 9/6/25

# This file tests the functions in the BankAccount.py file

import unittest
from bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
  # Constants used for testing
    INITIAL_BALANCE = 1000.00
    DEPOSIT_AMOUNT = 500.00
    WITHDRAW_AMOUNT = 200.00
    OVERDRAFT_LIMIT = 250.00
    DEBUG = True

    BALANCE1 = 3200
    WITHDRAWL1 = 500
    DEPOSIT1 = 450
    FIRST_NAME1 = "Hank"
    LAST_NAME1 = "Hill"
    
    BALANCE2 = 1500
    WITHDRAWL2 = 1750
    DEPOSIT2 = 200
    FIRST_NAME2 = "Mickey"
    LAST_NAME2 = "Mouse"    

  # The setup method creates bank accounts.
    def setUp(self):
        self.bankAccount1 = BankAccount("John", "Smith", TestBankAccount.INITIAL_BALANCE)
        self.bankAccount2 = BankAccount("Nancy", "Jackson", TestBankAccount.INITIAL_BALANCE)
        self.bankAccount3 = BankAccount("Reggie", "Miller", 50)
        self.acc1 = BankAccount("William", "Wian", 1000000)
        self.account4 = BankAccount(TestBankAccount.FIRST_NAME1, TestBankAccount.LAST_NAME1, TestBankAccount.BALANCE1)
        self.account5 = BankAccount(TestBankAccount.FIRST_NAME2, TestBankAccount.LAST_NAME2, TestBankAccount.BALANCE2)
        
        # checking that the asserts fail within the account creation
        try:
            self.account6 = BankAccount("D", "P", TestBankAccount.BALANCE1)
            self.account7 = BankAccount("MabelAndDipperPines", "StanfordAndStanleyPines", TestBankAccount.BALANCE1)
        except AssertionError as error:
            print(error)
                

  
  # The test_constructor method tests the constructor.
    def test_constructor(self):
        self.assertEqual(self.account4.getFirst(), "Hank")
        self.assertEqual(self.account4.getLast(), "Hill")
        self.assertEqual(self.account4.getBalance(), TestBankAccount.BALANCE1)
        if TestBankAccount.debug:
            print("\nTesting Constructor")
            print("The First Account: ", self.account4)
            print("The Second Account: ", self.account5)  
   


  # Test to see if the transfer is successful
    def testTransferSuccessful(self):
        # Print debug message if DEBUG is True
        if TestBankAccount.DEBUG:
            print("\nTesting a successful transfer:")

        # Define the amount being transferred
        transferAmount = 100.00
        
        # self.bankAccount1 is the receiver
        # self.bankAccount2 is the source sender
        # Attempt to transfer money from bankAccount2 to bankAccount1
        success = self.bankAccount1.tranfer(self.bankAccount2, transferAmount)

        # Assert that the transfer function is successful 
        self.assertTrue(success)

        # Assert that bankAccount1's balance increased after the transfer; it should equal the initial balance plus the transferred amount
        self.assertEqual(self.bankAccount1.balance, TestBankAccount.INITIAL_BALANCE + transferAmount)

        # Assert that bankAccount2's balance decreased after the transfer; it should equal the initial balance minus the transferred amount
        self.assertEqual(self.bankAccount2.balance, TestBankAccount.INITIAL_BALANCE - transferAmount)


   # Test to see if the transfer is denied 
    def testTransferDenied(self):
        if TestBankAccount.DEBUG:
            print("\nTesting to see if the transfer is denied due to insufficient funds:")
            
        # bankAccount3 has $50.00
        # The max withdraw is $50 + $250 = $300
        transferAmount = 300.01 
        
        # Attempt to transfer money from bankAccount3 to bankAccount1
        success = self.bankAccount1.tranfer(self.bankAccount3, transferAmount)
        
        # Assert that the transfer failed
        #print("Trannsfer denied: ", success)
        self.assertFalse(success)
        
        # Assert that bankAccount1's balance does not change
        self.assertEqual(self.bankAccount1.balance, TestBankAccount.INITIAL_BALANCE)
        
        # Assert that bankAccount3's balance does not change (aka the withdrawal failed)
        self.assertEqual(self.bankAccount3.balance, 50.00)


    # Test the printTransactions method 
    def testPrintTransactions(self):
        # Print debug message if DEBUG is True
        if TestBankAccount.DEBUG:
            print("\nTesting printTransactions:")

        # Record a deposit and a withdrawal to ensure the account has a transaction history in order to test the printTransactions method
        self.bankAccount3.deposit(50.00)
        self.bankAccount3.withdraw(20.00)

        # Call the printTransactions method for bankAccount3
        self.bankAccount3.printTransactions()

        # Assert that the transactions list actually contains the recorded transactions
        self.assertGreater(len(self.bankAccount3.transactions), 0)

    
    # test calculate interest 
    def test_calculateInterest(self):
        # creating the interest test
        interestTest1 = self.account4.calculateInterest()
        # checking that its equal to 3440 (the balance + the interest earned)
        self.assertEqual(self.account4.balance, 3440)
        
        # printing the information if debug is true 
        if TestBankAccount.debug:
            print("\nTesting Calculate Interest")
            print("First Account After Interest", self.account4.balance)
           
    # test deposit 
    def testDeposit(self):
           # Should work
        print("\nTesting Deposit")
        print(f"Current balance: ${self.acc1.balance:.2f}")
        self.assertTrue(self.acc1.deposit(500000)) 
        self.assertEqual(self.acc1.balance, 1500000.0)
        print(f"New account balance after deposit: ${self.acc1.balance:.2f}\n")
           
           # Should not work
        try:
            self.assertFalse(self.acc1.deposit(-10)) 
            self.assertEqual(self.acc1.balance, 1500000.0)
        except AssertionError as error:
            print("Invalid deposit")       
            print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
    # test withdrawl
    def testWithdrawl(self):
        # Should work and remove money from acc1
        self.acc1.withdraw(500000)
        self.assertEqual(self.acc1.balance, 500000.0)
        print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
        # Should be equal to the first withdrawl
        self.acc1.withdraw(2000000)
        self.assertEqual(self.acc1.balance, 500000)
        print(f" New account balance: ${self.acc1.balance:.2f}\n")
        
    # test overdraft process 
    def testOverdraft(self):
        self.acc1.withdraw(1000001)
        self.assertEqual(self.acc1.balance, -1.0)
        if TestBankAccount.debug:
            print("Testing overdraft")
            
        overdraft = self.acc1.getOverdraft()
        balance = self.acc1.getBalance()
        print("Amount of times of overdrafted: %d" % (overdraft))
        print("New Balance: %d" % (balance))
        
    # testing special method equality    
    def test_eq_(self):
        if TestBankAccount.debug:
            print("Testing equality")
        self.assertTrue(self.account4 == self.account4)
        self.assertFalse(self.account5 == self.account4)
       
    # testing special method inequality 
    def test_neq(self):
        if TestBankAccount.debug:
            print("Testing inequality")
        self.assertTrue(self.account4 != self.account5)
        self.assertFalse(self.account5 != self.account5)
        
        
if __name__ == '__main__':
    unittest.main()
        
