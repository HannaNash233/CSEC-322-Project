# clientAddress.py
#
# author(s): Hanna Nash
# 
#
# Date: 11/24/25

class ClientAddress:
    
    # constructs a client's address
    
    # @param street: The Client's street i.e. 1234 Cherry Blossom Dr.
    # @param city: The Client's city i.e. Seaside Heights
    # @param state: The Client's state i.e. VA
    
    # states have to be within the valid states list 
    VALID_STATES = {"VA", "MD", "NJ", "PA", "DE", "NC", "WV", "DC"}
    
    # @require: street is a non empty string with no special characters with a
    # max length of 30
    # @require: city is a non empty string with no special characters with a 
    # max length of 30
    # @require: state is a non empty string within the the valid states list and
    # the max length must be two characters
    def __init__(self, street, city, state):
        assert isinstance(street, str)
        assert isinstance(city, str)
        assert isinstance(state, str)
        assert len(street) <= 30
        assert len(city) <= 30
        assert state in ClientAddress.VALID_STATES
        assert len(state) <= 2
        
        self._street = street
        self._city = city
        self._state = state
        
    def getStreet(self):
        return self._street
    
    def getCity(self):
        return self._city
    
    def getState(self):
        return self._state
    
    
    def __eq__(self, other):
        result = self._street == other._street and self._city == other._city and self._state == other._state
        return result
    
    def __gt__(self, other):
        result = self._street > other._street and self._city > other._city and self._state > other._state
        return result
    
    def __le__(self, other):
        result = self._street <= other._street and self._city <= other._city and self._state <= other._state
        return result
