



import unittest
from PhoneNumber import PhoneNumber


class TestPhoneNumber(unittest.TestCase):
	
	def setUp(self):
		self.phoneNum1 = PhoneNumber("5678907645")
		self.phoneNum2 = PhoneNumber("4609871234")
		
	def testGetPhoneNum(self):
		print("\nTesting getters for phone number")
		self.assertEqual(self.phoneNum1.getPhoneNum(),"5678907645")
	
	
	def testSetPhoneNum(self):
		print("\nTesting setters for phone number")
		self.phoneNum2._setPhoneNum("9086574567")
		self.assertEqual(self.phoneNum2.getPhoneNum(), "9086574567")
		
	def testInvalidPhoneLength(self):
		print("\nTesting invalid phone length")
		try:
			self.phoneNum3 =  PhoneNumber("46098712346343234352")
		except AssertionError:
			print("> 10 digit phone number")
            
    
	def testInvalidPhoneStart(self):
		print("\nTesting invalid phone starting digit")
		try:
			self.phoneNum4 =  PhoneNumber("2347689087")
		except AssertionError:
			print("invalid starting digit 0 1 or 2")
            
            
	def testInvalidPhoneDigit(self):
		print("\nTesting invalid phone digit")
		try:
			self.phoneNum3 =  PhoneNumber("54!6970695")
		except AssertionError:
			print("Non number in phone number")
            
            
	def testEq(self):
		print("\nTesting equal")
		self.assertTrue(self.phoneNum1 == self.phoneNum1)
    	
	def testNe(self):
		print("\nTesting not equal")
		self.assertFalse(self.phoneNum1 == self.phoneNum2)
    	
	def testGt(self):
		print("\nTesting greater then")
		self.assertTrue(self.phoneNum1 > self.phoneNum2)
    	
	def testLt(self):
		print("\nTesting less then")
		self.assertFalse(self.phoneNum1 < self.phoneNum2)
    	
	def testGe(self):
		print("\nTesting greater then or equal")
		self.assertTrue(self.phoneNum1 >= self.phoneNum2)
    	
	def testLe(self):
		print("\nTesting less then or equal")
		self.assertFalse(self.phoneNum1 <= self.phoneNum2)
            
            
