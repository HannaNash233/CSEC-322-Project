# client.py
#
# Authors: Detric Brown, Evan Fannin, Hanna Nash, Victoria Seusankar
#
# Date: 10/29/25

class Client:
    
    # Attributes
    _NEXTCLIENTNUMBER = 100
    VALID_STATES = {"VA", "MD", "NJ", "PA", "DE", "NC", "WV", "DC"}
    
    # Constructs a client.
    
    # @param firstName: The first name of the client
    # @param lastName: The last name of the client
    # @param phoneNum: The client's phone number
    # @param address: A tuple containing the street, city, and state
    # @param accountType: "Checking" or "Savings"
    
    # @require: firstName and lastName contain only letters and correct length
    # @require: phoneNum is 10 digits and cannot start with 0, 1, or 2
    # @require: street and city are nonempty strings with no special characters
    # @require: state is in VALID_STATES
    # @ensure Client receives a unique client number and one account of chosen type
    
    def __init__(self, firstName, lastName, phoneNum, address, accountType):
        assert firstName.isalpha() and 1 <= len(firstName) <= 25
        assert lastName.isalpha() and 1 <= len(lastName) <= 40
        assert phoneNum.isdigit() and len(phoneNum) == 10 and phoneNum[0] not in "012"
        street, city, state = address
        assert street and len(street) <= 30 and street.replace(" ","").isalnum()
        assert city and len(city) <= 30 and city.replace(" ","").isalnum()
        assert state in Client.VALID_STATES
        assert accountType in {"Checking", "Savings"}, "Account type must be 'Checking' or 'Savings'"
        
        self._firstName = firstName
        self._lastName = lastName
        self._phoneNum = phoneNum
        self._address = address
        self._clientNum = Client._NEXTCLIENTNUMBER
        Client._NEXTCLIENTNUMBER += 1
        self.accounts = []        

    # Getters
    def getClientNumber(self):
        return self._clientNum
    
    def getFirstName(self):
        return self._firstName
    
    def getLastName(self):
        return self._lastName
        
    
    def getAddress(self):
        return self._address
        
    def getPhoneNum(self):
        return self._phoneNum
        
    def getAccountType(self):
        pass
    
    # Account management
    def openAccount(self, typeAccount):
        pass
    
    def closeAccount(self, typeAccount):
        pass

    # Sets the client's first name.
    def setFirst(self, firstName):
        self._first = firstName

    # Set the client's last name.
    def setLast(self, lastName):
        self._last = lastName

    # Set the client's address
    def setAddress(self, address):
        self._address = address

    # Set the client's phone number
    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum
    
    # Print method
    def printAccounts(self):
        pass
    



