# clientTester.py
# 
# Author(s): William Wian
# 
# Date: 10/29/25

import unittest 
from checkingAccount import CheckingAccount
from client import Client

# got prints just to see what everything is doing currently 
class testClient(unittest.TestCase):    

    def setUp(self):
        address1 = ("168 Pelham Place", "Norfolk", "VA")
        address2 = ("167 Main St", "Richmond", "VA") 
        self.client1 = Client("joe", "smith", "7576767679", address1, "Checking")
        self.client2 = Client("John", "Johnson", "7571234567", address2, "Savings")
            
        # Client number here is 100 101
        # goes up at each test
        print(self.client1.getClientNumber())
        print(self.client2.getClientNumber())
        
    def test_constructor(self):
        self.assertIsNotNone(self.client1)
        self.assertIsNotNone(self.client2)
        print("\nClient Accounts: ")
        print(self.client1.printAccounts())
        print(self.client2.printAccounts())
        
    
    # Prints 110 and 111
    # incriments correctly
    def test_client_number(self):
        self.assertEqual(self.client2.getClientNumber(), self.client1.getClientNumber() + 1)
        print(f"\nClient number: {self.client1.getClientNumber()}")
        print(f"Client number: {self.client2.getClientNumber()}")
    
    
    # Fully Tested
    def test_first_name(self):
        print("\nTesting setters and getters for firstName")
        self.client1.setFirst("Will")
        self.assertEqual(self.client1.getFirstName(), "Will")
        
        try: 
            self.client1.setFirst("")
        except(AssertionError):
            print("\nTesting < 0 characters")
        
        try:
            self.client1.setFirst("qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewqwertyuiopasdfghjklmnbzxbv")
        except(AssertionError):
            print("\nTesting > 40 characters")
        
        
    def test_get_last_name(self):
        self.assertEqual(self.client1.getLastName(), "smith")
        print(f"\nLast name: {self.client1.getLastName()}")
    
    def test_address(self):
        self.assertEqual(self.client1.getAddress(), ("168 Pelham Place", "Norfolk", "VA"))
        print(f"\nAddress: {self.client1.getAddress()}")
        
    def test_phone_num(self):
        self.assertEqual(self.client1.getPhoneNum(), "7576767679")
        print(f"\nPhone number: {self.client1.getPhoneNum()}")
    
    # Type is fully covered and tested
    def test_get_account_type_checking(self):
        self.assertEqual(self.client1.getAccountType(), "Checking")
        print("\nTesting Account type Checking")
        print(f"Account type: {self.client1.getAccountType()}") 
        
    def test_get_account_type_savings(self):
        self.assertEqual(self.client2.getAccountType(), "Savings")
        print("\nTesting Account type Savings")
        print(f"Account type: {self.client2.getAccountType()}") 
    
    def test_get_account_type_wrong(self):
        address3 = ("123 nowhere", "Richmond", "WY")
        print("\nTest wrong type")
        with self.assertRaises(AssertionError):
            Client("John", "Johnson", "1234567890", address3, "Wrong")

    def test_eq(self):
        if testClient.DEBUG:
            print("\nTesting __eq__ method")
    
        # Assign account numbers for controlled comparison
        self.client1 = self.client2
        
        # Equal
        result = (self.client1 == self.client2)
        self.assertTrue(result)
    
        # Not equal
        result = (self.client1 == self.client3)
        self.assertFalse(result)
    
    
    def test_lt(self):
        if testClient.DEBUG:
            print("\nTesting __lt__ method")
    
        result = (self.client1 < self.client2)
        self.assertTrue(result)
    
        result = (self.client2 < self.client1)
        self.assertFalse(result)
    
    
    def test_gt(self):
        if testClient.DEBUG:
            print("\nTesting __gt__ method")
    
        result = (self.client1 > self.client2)
        self.assertFalse(result)
    
        result = (self.client2 > self.client1)
        self.assertTrue(result)
    
    
    def test_le(self):
        if testClient.DEBUG:
            print("\nTesting __le__ method")
    
        result = (self.client1 <= self.client2)
        self.assertTrue(result)
           
        result = (self.client3 <= self.client2)
        self.assertFalse(result)
           
        result = (self.client2 <= self.client1)
        self.assertFalse(result)
        
           
if __name__ == '__main__':
    unittest.main()
