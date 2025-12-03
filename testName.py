# TestName.py

import unittest

from name import Name

class TestName(unittest.TestCase):
    DEBUG = True
    
    def setUp(self):
        self.name1 = Name("William", "Wian")
        self.name2 = Name("Cara", "Routh")
        
    def TestConstructor(self):
        if  TestName.DEBUG:
            print("\nTesting Constructor")
            
        self.assertEqual(self.name1.getFirst(), "William")
        self.assertEqual(self.name2.getFirst(), "Cara")   
    
    # Testing first name    
    def test_setFirst(self):
        if TestName.DEBUG:
            print("\nTesting first name")
        
        self.name1.setFirst("Jordan")
        self.assertEqual(self.name1.getFirst(), "Jordan")
        
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
        
        self.name1.setLast("Casey")
        self.assertEqual(self.name1.getLast(), "Casey")
        
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
            self.name1.setFirst("w1an4")
        except AssertionError as e:
            print("Assertion Error:", e)  
    
                
    def test_eq(self):
        if TestName.DEBUG:
            print("\nTesting name equality")
        
        self.assertTrue(self.name1 == self.name1)
        
    def test_ne(self):
        if TestName.DEBUG:
            print("\nTesting name inequality")
            
        self.assertFalse(self.name1 == self.name2)
        
        
if __name__ == '__main__':
    unittest.main()
        
    
        