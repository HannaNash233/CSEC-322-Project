# clientTester.py
# 
# Author(s): William Wian, 
# 
# Date: 10/29/25

import unittest 
from checkingAccount import CheckingAccount
from client import Client

class TestClient(unittest.TestCase):
    print("hello")
    
    def setUp(self):
        address = ("168 Pelham Place", "Norfolk", "VA")
        self.client = Client("Cara", "Routh", "7576767679", address, "Checking")
        # print(self.client.printAccount())

    def test_get_first_name(self):
        self.assertEqual(self.client.getFirstName(), "Cara")

    def test_client_number_increments(self):
        address = ("167 Main St", "Richmond", "VA")
        another_client = Client("Jacob", "Ambrose", "7575551234", address, "Savings")
        self.assertEqual(another_client.getClientNumber(), self.client.getClientNumber() + 1)

    def test_invalid_state(self):
        address = ("167 Main St", "Wyoming", "WY")
        with self.assertRaises(AssertionError):
            Client("William", "Wian", "7579876543", address, "Checking")  
        
    
if __name__ == '__main__':
    unittest.main()