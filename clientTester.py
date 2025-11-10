# clientTester.py
# 
# Author(s): William Wian, 
# 
# Date: 10/29/25

import unittest 
from checkingAccount import CheckingAccount
from client import Client

# got prints just to see what everything is doing currently 
class TestClient(unittest.TestCase):    
    def setUp(self):
        address1 = ("168 Pelham Place", "Norfolk", "VA")
        address2 = ("167 Main St", "Richmond", "VA") 
        self.client1 = Client("joe", "smith", "7576767679", address1, "Checking")
        self.client2 = Client("Jake", "Johnson", "7575551234", address2, "Savings")
        
    def test_constructor(self):
        self.assertIsNotNone(self.client1)
        print(self.client1.printAccounts())
        # This prints 100 for client number
        # print(self.client1.getClientNumber())
        
    # Prints 110 and 111, 
    def test_get_client_number(self):
        self.assertEqual(self.client2.getClientNumber(), self.client1.getClientNumber() + 1)
        print(f"\nClient number: {self.client1.getClientNumber()}")
        print(f"Client number: {self.client2.getClientNumber()}")

    def test_get_first_name(self):
        self.assertEqual(self.client1.getFirstName(), "joe")
        print(f"\nFirst name: {self.client1.getFirstName()}")
        
    def test_get_last_name(self):
        self.assertEqual(self.client1.getLastName(), "smith")
        print(f"\nLast name: {self.client1.getLastName()}")
    
    def test_get_address(self):
        self.assertEqual(self.client1.getAddress(), ("168 Pelham Place", "Norfolk", "VA"))
        print(f"\nAddress: {self.client1.getAddress()}")
        
    def test_get_phone_num(self):
        self.assertEqual(self.client1.getPhoneNum(), "7576767679")
        print(f"\nPhone number: {self.client1.getPhoneNum()}")
        
    def test_get_account_type_checking(self):
        self.assertEqual(self.client1.getAccountType(), "Checking")
        print("\nTesting Account type Checking")
        print(f"Account type: {self.client1.getAccountType()}") 
        
    def test_get_account_type_savings(self):
        self.assertEqual(self.client2.getAccountType(), "Savings")
        print("\nTesting Account type Savings")
        print(f"Account type: {self.client2.getAccountType()}") 
    
    """
    def test_get_account_type_wrong(self):
        address3 = ("123 nowhere", "Richmond", "VA")
        with self.assertRaises(AssertionError):
            Client("John", "Johnson", "1234567890", address3, "Wrong")
    """
           
if __name__ == '__main__':
    unittest.main()