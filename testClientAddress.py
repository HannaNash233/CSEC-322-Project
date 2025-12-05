# testClientAddress.py
# 
# author(s): Hanna Nash
#
# date: 11/24/25

import unittest
from clientAddress import ClientAddress

class TestClientAddress(unittest.TestCase):
    
    def setUp(self):
        self.clientAddress1 = ClientAddress("1209 Ocean Terrace", "Seaside Heights", "NJ")
        self.clientAddress2 = ClientAddress("1024 Cherry Street", "Langley Falls", "VA")
        
    def testGetStreet(self):
        street1 = self.clientAddress1.getStreet()
        print(street1)
        
    def testGetCity(self):
        city1 = self.clientAddress2.getCity()
        print(city1)
        
    def testGetState(self):
        state1 = self.clientAddress1.getState()
        print(state1)
        
    def testInvalidLength(self):
        try:
            self.clientAddress3 = ClientAddress("First Street and East Capitol Street East Front Plaza US Capitol", "Washington", "DC")
        except AssertionError:
            print(">= 30 street length")
            
        try:
            self.clientAddress3 = ClientAddress("3200 Mount Vernon", "George Washington Ave Revolutionary War Way With Thomas Jefferson", "VA")
        except AssertionError: 
            print(">= 30 city length")
            
        try:
            self.clientAddress3 = ClientAddress("123 Family Guy Way", "Stoolbend", "VAA")
        except AssertionError:
            print(">= 2 state length")
            
    def testWrongStateList(self):
        try:
            self.clientAddress3 = ClientAddress("123 McKinley Way", "Lima", "OH")
        except AssertionError:
            print("Not in states list")

    
    def testStr(self):
    	address = str(self.clientAddress1)
    	self.assertTrue(address == "Street: 1209 Ocean Terrace, City: Seaside Heights, State: NJ")
    	print(self.clientAddress1)
    
    def testEq(self):
        self.clientAddress3 = ClientAddress("1209 Ocean Terrace", "Seaside Heights", "NJ")
        equality = self.clientAddress1 == self.clientAddress3
        print(equality)
        
    def testGt(self):
        print(self.clientAddress2 > self.clientAddress1)
        
    def testLe(self):
        print(self.clientAddress1 <= self.clientAddress2)
        