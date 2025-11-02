# client.py
#
# Authors: Detric Brown, Evan Fannin, Hanna Nash, Victoria Seusankar
#
# Date: 10/29/25

class Client:
    
    def __init__(self, firstName, lastName, phoneNum, address):
        pass
    
    def getClientNumber(self):
        pass
    
    def getFirstName(self):
        pass
    
    def getLastName(self):
        return self.lastName
        
    
    def getAddress(self):
        return self.address
        
    
    def getPhoneNum(self):
        return self.PhoneNum
        
    
    def getAccountType(self):
        pass
    
    def openAccount(self, typeAccount):
        pass
    
    def closeAccount(self, typeAccount):
        pass

    # Sets the client's first name.
    def setFirst(self, firstName):
        self.first = firstName

    # Set the client's last name.
    def setLast(self, lastName):
        self._last = lastName

    # Set the client's address
    def setAddress(self, address):
        self._address = address

    # Set the client's phone number
    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum

    

