# TestName.py

import unittest

from name import Name

class TestName(unittest.TestCase):
    DEBUG = True
    
    def setUp(self):
        self.name1 = Name("Spongebob", "Squarepants")
        self.name2 = Name("Patrick", "Star")
    
    
    # Testing first name    
    def test_setFirst(self):
        if TestName.DEBUG:
            print("\nTesting first name")
        
        self.name1.setFirst("Sandy")
        self.assertEqual(self.name1.getFirst(), "Sandy")
        
    def test_setFirstLong(self):
        if TestName.DEBUG:
            print("\nTesting too long first name")
            
        try:
            self.name1.setFirst("qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm")
        except AssertionError as e:
            print("Assertion Error:", e)
            
    def test_setFirstShort(self):
        if TestName.DEBUG:
            print("\nTesting too short first name")     
            
        try:
            self.name1.setFirst("")
        except AssertionError as e:
            print("Assertion Error:", e)     
                
    def test_setFirstNumber(self):
        if TestName.DEBUG:
            print("\nTesting invalid characters in first name")
            
            try:
                self.name1.setFirst("Wi11y")
            except AssertionError as e:
                print("Assertion Error:", e)    
                
    
    # Testing last name 
    def test_setLast(self):
        if TestName.DEBUG:
            print("\nTesting last name")
        
        self.name1.setLast("Cheeks")
        self.assertEqual(self.name1.getLast(), "Cheeks")
        
    def test_setLastLong(self):
        if TestName.DEBUG:
            print("\nTesting too long last name")
            
        try:
            self.name1.setLast("qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm")
        except AssertionError as e:
            print("Assertion Error:", e)
            
    def test_setLastShort(self):
        if TestName.DEBUG:
            print("\nTesting too short last name")     
            
        try:
            self.name1.setLast("")
        except AssertionError as e:
            print("Assertion Error:", e)     
                
    def test_setLastNumber(self):
        if TestName.DEBUG:
            print("\nTesting invalid characters in last name")
            
        try:
            self.name1.setLast("w1an4")
        except AssertionError as e:
            print("Assertion Error:", e)  
    
    # Testing special methods
    def test__str__(self):
    	if TestName.DEBUG:
    		print("\nTesting string")
    	
    	result = str(self.name1)
    	self.assertTrue(result == "Name: Spongebob Squarepants")
                
    def test__eq__(self):
        if TestName.DEBUG:
            print("\nTesting name equality")
        
        self.assertTrue(self.name1 == self.name1)
        
    def test__ne__(self):
        if TestName.DEBUG:
            print("\nTesting name inequality")
            
        self.assertTrue(self.name1 != self.name2)
        
if __name__ == '__main__':
    unittest.main()
