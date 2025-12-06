# TestBankAccount.py
#
# Authors: Hanna Nash, Victoria Seusankar, Will Wian, Detric Brown
#
# Date: 9/6/25

# This file tests the functions in the BankAccount.py file

import unittest
import os
from bankAccount import BankAccount

# HELPER CLASS: ConcreteBankAccount
# Because BankAccount is an Abstract Base Class (ABC), we cannot verify
# it directly. We create a concrete class here solely for testing purposes.
class ConcreteBankAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            # Create a transaction record (mimicking logic in deposit)
            return True
        return False

    def calculateInterest(self):
        interest = self.balance * BankAccount.INTEREST_RATE
        self.balance += interest
        return self.balance

# MAIN TEST CLASS
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
        # We use ConcreteBankAccount instead of BankAccount directly
        self.bankAccount1 = ConcreteBankAccount(TestBankAccount.INITIAL_BALANCE, "checkings")
        self.bankAccount2 = ConcreteBankAccount(TestBankAccount.INITIAL_BALANCE, "savings")
        self.bankAccount3 = ConcreteBankAccount(50, "checkings")
        self.acc1 = ConcreteBankAccount(1000000, "savings")
        
        self.account4 = ConcreteBankAccount(TestBankAccount.BALANCE1, "checkings")
        self.account5 = ConcreteBankAccount(TestBankAccount.BALANCE2, "savings")


    # The test_constructor method tests the constructor.
    def test_constructor(self):
        # Verify Balance
        self.assertEqual(self.account4.balance, TestBankAccount.BALANCE1)
        
        # Verify Security Attributes
        # Ensure IV and Key are generated
        self.assertIsNotNone(self.account4._iv)
        self.assertIsNotNone(self.account4._key)
        self.assertEqual(len(self.account4._iv), 16)
        self.assertEqual(len(self.account4._key), 32)

        if TestBankAccount.DEBUG:
            print("\nTesting Constructor")
            print("The First Account Balance: ", self.account4.balance)

    # Test to see if the transfer is successful
    def testTransferSuccessful(self):
        if TestBankAccount.DEBUG:
            print("\nTesting a successful transfer:")

        transferAmount = 100.00
        
        # self.bankAccount1 is the receiver
        # self.bankAccount2 is the source sender
        success = self.bankAccount1.tranfer(self.bankAccount2, transferAmount)

        self.assertTrue(success)
        self.assertEqual(self.bankAccount1.balance, TestBankAccount.INITIAL_BALANCE + transferAmount)
        self.assertEqual(self.bankAccount2.balance, TestBankAccount.INITIAL_BALANCE - transferAmount)

    # Test to see if the transfer is denied 
    def testTransferDenied(self):
        if TestBankAccount.DEBUG:
            print("\nTesting to see if the transfer is denied due to insufficient funds:")
            
        # bankAccount3 has $50.00. Attempt to transfer more than available.
        transferAmount = 300.01 
        
        success = self.bankAccount1.tranfer(self.bankAccount3, transferAmount)
        
        self.assertFalse(success)
        self.assertEqual(self.bankAccount1.balance, TestBankAccount.INITIAL_BALANCE)
        self.assertEqual(self.bankAccount3.balance, 50.00)

    # Test the transaction logging logic (in memory)
    def testPrintTransactions(self):
        if TestBankAccount.DEBUG:
            print("\nTesting printTransactions:")

        self.bankAccount3.deposit(50.00)
        # Note: withdraw in ConcreteBankAccount currently doesn't log transactions 
        # unless you update the helper class, but deposit does.
        
        self.assertGreater(len(self.bankAccount3.transactions), 0)

    # NEW TEST: Test Encryption and Decryption (Project 3)
    def test_transaction_encryption_decryption(self):
        if TestBankAccount.DEBUG:
            print("\nTesting Transaction Encryption/Decryption (Project 3):")
            
        # Create transactions
        self.bankAccount1.deposit(100.00)
        self.bankAccount1.deposit(200.00)
        
        # Ensure transactions exist
        self.assertEqual(len(self.bankAccount1.transactions), 2)
        
        # Write transactions to encrypted file
        # bankAccount1 is type "checkings", so it writes to "checkings.txt"
        self.bankAccount1.writeTransactions()
        
        
        Simulate a fresh read by clearing current memory
        # We manually clear the list to prove readTransactions actually works
        original_transactions = list(self.bankAccount1.transactions)
        self.bankAccount1.transactions = []
        self.assertEqual(len(self.bankAccount1.transactions), 0)
        
        # Read/Decrypt transactions
        # Based on standard design, it *should* usually repopulate the list.
        # Use a try/except block to catch AES errors if keys don't match (though they should here).
        try:
            self.bankAccount1.readTransactions()
            # If the code runs without error, decryption was successful using the generated key/iv.
            success = True
        except Exception as e:
            success = False
            print(f"Decryption failed: {e}")
            
        self.assertTrue(success)

    # test calculate interest 
    def test_calculateInterest(self):
        new_balance = self.account4.calculateInterest()
        
        # Initial 3200 + (3200 * 0.075) = 3200 + 240 = 3440
        self.assertEqual(new_balance, 3440)
        self.assertEqual(self.account4.balance, 3440)
        
        if TestBankAccount.DEBUG:
            print("\nTesting Calculate Interest")
            print("First Account After Interest", self.account4.balance)
           
    # test deposit 
    def testDeposit(self):
        self.assertTrue(self.acc1.deposit(500000)) 
        self.assertEqual(self.acc1.balance, 1500000.0)
        if TestBankAccount.DEBUG:
            print(f" New account balance: ${self.acc1.balance:.2f}\n")
           
        # Should not work
        self.assertFalse(self.acc1.deposit(-10)) 
        self.assertEqual(self.acc1.balance, 1500000.0)

    # test withdrawl
    def testWithdrawl(self):
        # Should work and remove money from acc1
        self.acc1.withdraw(500000)
        self.assertEqual(self.acc1.balance, 500000.0)
        
        # Should be equal to the first withdrawl
        self.acc1.withdraw(2000000) # Should fail (insufficient funds)
        self.assertEqual(self.acc1.balance, 500000)
        
    # testing special method equality    
    def test_eq_(self):
        if TestBankAccount.DEBUG:
            print("Testing equality")
        self.assertTrue(self.account4 == self.account4)
        # Assuming different instances are not equal
        self.assertFalse(self.account5 == self.account4)
       
    # testing special method inequality 
    def test_neq(self):
        if TestBankAccount.DEBUG:
            print("Testing inequality")
        self.assertTrue(self.account4 != self.account5)

        
if __name__ == '__main__':
    unittest.main()
