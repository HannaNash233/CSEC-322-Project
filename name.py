# @param firstName: The first name of the client
# @param lastName: The last name of the client
    
# @require: firstName and lastName contain only letters and correct length
class Name:
	
	def __init__(self, firstName, lastName):
		assert firstName.isalpha()
		assert 1 <= len(firstName) <= 25
		
		assert lastName.isalpha()
		assert 1 <= len(lastName) <= 40
		
		self._firstName = firstName
		
        self._lastName = lastName
    
    # Get the client's last name.
    def getFirstName(self):
		return self._firstName
    
    # Get the client's last name.
    def getLastName(self):
		return self._lastName
    
    # Set the client's first name.
    def setFirst(self, firstName):
		self._first = firstName

    # Set the client's last name.
    def setLast(self, lastName):
		self._last = lastName
