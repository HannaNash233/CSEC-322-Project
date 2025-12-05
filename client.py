# client.py
#
# Authors: Detric Brown, Evan Fannin, Hanna Nash, Victoria Seusankar
#
# Date: 10/29/25

from bankAccount import BankAccount
from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount

class Client:
    
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
    
    def __init__(self, name, phoneNum,address):
    	assert(isinstance(name,Name)), "Invalid Name"
    	assert(isinstance(phoneNum,PhoneNumber)), "Invalid Phone Number"
    	assert(isinstance(address,ClientAddress)), "Invalid Address"
        
        #self._firstName = firstName
        #self._lastName = lastName
        self._name = name
        self._phoneNum = phoneNum
        self._address = address
        self._clientNum = Client._NEXTCLIENTNUMBER
        Client._NEXTCLIENTNUMBER += 1
        self.accounts = []        

    # Getters
    def getClientNumber(self):
        return self._clientNum
    
    #def getFirstName(self):
    #    return self._firstName
    #def getLastName(self):
    #    return self._lastName

    def getName(self):
        return self._name
    
    def getAddress(self):
        return self._address
    
    def getPhoneNum(self):
        return self._phoneNum
    
    def getAccountType(self):
        return self._accountType
    
    def getAccounts(self):
        return self.accounts
    
    def printAccounts(self):
        for account in self.accounts:
            print(account)
        
    
    def displayDetails(self):
        print("Current Client: %s %s\n" % (self._firstName, self._lastName))
        print("Client Number: #%d\n" % (self._clientNum))
        print("Current Count of Accounts: %d\n" % (len(self.accounts)))
        self.printAccounts()
        
    def openAccount(self, account, balance):
        assert account in {"Checking", "Savings"}, "Not a valid account"
        assert balance > 0, "Balance must over zero"
        #assert isinstance(account, BankAccount)
        #acctType = typeAccount.getType()
        if account == "Savings":
            account = SavingsAccount(balance)
            self.accounts.append(account)
        elif account == "Checking":
            account = CheckingAccount(balance)
            self.accounts.append(account)
            
        return account
            
        
    
    def closeAccount(self, account):
     
        assert account.getType() in {"Checking", "Savings"}, "Not a valid account"
       # assert isinstance(account.getType(), ("Savings") or isinstance(account.getType())
       # assert account != ""
        
       # self.accountList.remove(account)
        accountBalance = account.getBalance()
       
        account.withdraw(accountBalance)
        self.accounts.remove(account)
        
        
        
    def setFirst(self, firstName):
        self.first = firstName
    
    def setAddress(self, address):
        self._last = lastName
    
    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum
        
    
  


