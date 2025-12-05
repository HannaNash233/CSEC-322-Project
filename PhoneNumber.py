

class PhoneNumber:
	def __init__(self, phoneNum):
		assert phoneNum.isdigit() and len(phoneNum) == 10 and phoneNum[0] not in "012"
		self.phoneNum = phoneNum
		
	def __str__(self):
		return ("Phone Number: %s" % (self.phoneNum))
		
	def __eq__(self, other):
		result = (self.phoneNum == other.phoneNum)
		return result
		
	def __gt__(self, other):
		result =  (self.phoneNum > other.phoneNum)
		return result
		
	def __ge__(self, other):
		result = (self.phoneNum >= other.phoneNum)
		return result
		
	def getPhoneNum(self):
		return self.phoneNum
		
	def _setPhoneNum(self, phoneNum):
		self.phoneNum = phoneNum
		
