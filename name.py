

# @param firstName: The first name of the client
# @param lastName: The last name of the client
# @require: firstName and lastName contain only letters and correct length
class Name:
  def __init__(self, firstName, lastName):
      assert isinstance(firstName, str)
      assert firstName.isalpha()
      assert 1 <= len(firstName) <= 25
		
      assert isinstance(lastName, str)
      assert lastName.isalpha()
      assert 1 <= len(lastName) <= 40
		
      self._first = firstName
      self._last = lastName
	
	
  # Get the client's first name.
  # @ensure: self._firstName is a valid string.
  # @require: returns self._firstName unchanged
  
  def getFirst(self):
      return self._first
    
    
  # Get the client's last name.  
  # @ensure: self._lastName is a valid string.
  # @require: returns self._lastName unchanged
  
  def getLast(self):
      return self._last
    
    
  # Set the client's first name
  # @require: firstName is a string of letters only
  # @require: 1 <= len(firstName) <= 25
  # @ensure: self._firstName == firstName 
  
  def setFirst(self, firstName):
      assert isinstance(firstName, str)
      assert firstName.isalpha(), "first name can only include characters from alphabet"
      assert 1 <= len(firstName) <= 25, "Length must be between 1 and 25"    
      self._first = firstName
      

  # Set the client's last name.
  # @ensure: lastName is a string of letters only
  # @ensure: 1 <= len(lastName) <= 40
  # @require: self._lastName == lastName
  
  def setLast(self, lastName):
      assert isinstance(lastName, str)
      assert lastName.isalpha(), "last name can only include characters from alphabet"
      assert 1 <= len(lastName) <= 40, "Length must be between 1 and 40"    
      self._last = lastName
   
   
  # Print the full name   
  # @ensure: self._firstName and self._lastName are valid strings
  # @require: returns a string formatted with the current names
  
  def __str__(self):
    name = ("Name: %s %s" % (self._first, self._last))
    return name
  
  
  # Returns true if equal
  # @ensure: other is a Name instance
  # @require: returns True if both first and last names match exactly 
  
  def __eq__(self, other):
    result = ((self._first == other._first) and (self._last == other._last))
    return result
  
  # Returns true if not equal 
  # @ensure: other is a Name instance
  # @require: returns True if one name differs
  
  def __ne__(self, other):
    result = ((self._first != other._first) or (self._last != other._last))
    return result