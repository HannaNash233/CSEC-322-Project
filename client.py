# client.py
#
# Authors: Detric Brown, Evan Fannin, Hanna Nash, Victoria Seusankar
#
# Date: 10/29/25

from bankAccount import BankAccount

class Client:
    
    def __init__(self, firstName, lastName, phoneNum, address):
        pass
    
    def getClientNumber(self):
        pass
    
    def getFirstName(self):
        pass
    
    def getAddress(self):
        pass
    
    def getPhoneNum(self):
        pass
    
    def getAccountType(self):
        return self.accountType
    
    def openAccount(self, account):
        assert isinstance(account, BankAccount)
        #acctType = typeAccount.getType()
        if account.getType() == "Savings":
            savingsAccount = SavingsAccount(self.balance)
            self.accountList.append(savingsAccount)
        elif account.getType() == "Checking":
            checkingAccount = CheckingAccount(self.balance)
            self.accountList.append(checkingAccount)
    
    def closeAccount(self, account):
        assert isinstance(account, BankAccount)
        accountBalance = account.balance
        typeaccount.withdraw(accountBalance)
        self.accountList.pop(account)
        
    def setFirst(self, firstName):
        self.first = firstName
    
    def setAddress(self, address):
        self._last = lastName
    
    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum
    