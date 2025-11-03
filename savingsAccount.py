# savingsAccount.py
# 
# authors: Hanna Nash, Victoria Seusankar, Will Wian
#
# Date: 10/29/25

class SavingsAccount:
    
    def __init__(self, initBalance=0.0):
        pass
    
    def displayDetails(self):
        pass
    
    def deposit(self, amount):
        pass

    
    # Calculates and applies the monthly 4.0% annual interest.
    # @return: True if the interest was calculated and applied, and False otherwise.
    def calculateInterest(self):
        # Calculate the monthly interest rate
        monthly_rate = self.INTEREST_RATE / 12.0
    
        # The interest earned on the balance based on the interest rate
        interestEarned = self._balance * monthly_rate

        if interestEarned > 0:
            # Add the interest earned to the balance
            self._balance += interestEarned
    
            # Create an interest transaction
            interestTransaction = Transaction(BankAccount._nextTransactionNumber, "interest", interestEarned)
        
            # Append the transaction to the transactions list
            self._transactions.append(interestTransaction)
            BankAccount._nextTransactionNumber += 1
            
            print("Interest Applied: %.2f added to Savings Account %d." % (interestEarned, self.getAccountNumber()))
            return True
        
        else:
            print("No interest applied to Savings Account %d due to negative balance." % (self.getAccountNumber()))
            return False

    
    # Handles withdrawals, including checks for debt limits and applying tiered overdraft fees.
    # @param amount: The amount to withdraw.
    # @return: True if the withdrawal is successful, and False otherwise.
    def withdraw(self, amount):
        # Check to see if the amount requested is positive
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False

        # Check to see if the current balance can cover the withdrawal
        if self._balance >= amount:            
            # Create the withdrawal transaction
            withdrawalTransaction = Transaction(BankAccount._nextTransactionNumber, "withdrawal", -amount)
            
            # Append the withdrawal to the transactions list
            self._transactions.append(withdrawalTransaction)
            
            # Add to the transaction number
            BankAccount._nextTransactionNumber += 1
            
            # Subtract the amount from the balance
            self._balance -= amount
            
            print("Standard withdrawal complete. New Balance: %.2f" % (self._balance))
            return True

    
    # 
    # 
    def transfer(self, fromAccount, amount):
        # If fromAccount tries to make a transfer to itself, deny the transfer and return false
        if fromAccount is self:
            print("Transfer denied: Cannot transfer to the same account.")
            return False
    
        # If the amount being transfered is negative or equal to 0, print a message to let the user know
        # that the amount being transferred needs to be positive, and return false
        if amount <= 0:
            print("Transfer denied: Amount must be positive.")
            return False
    
        # Create a variable to store the successful withdrawal
        successfulWithdrawal = fromAccount.withdraw(amount)
    
        # If the withdrawal is successful, deposit the specified amount and return true
        if successfulWithdrawal:
            self.deposit(amount) 
            return True
    
        # If the withdrawal does not meet the proper conditions, print a message to let the user know
        # that the transfer failed, and return false
        else:
            print("Transfer failed: Withdrawal from the source account was denied.")
            return False
        

    
    def printTransactions(self):
        pass

    
    def writeTransactions(self, filename):
        pass
    
    def readTransactions(self, filename):
        pass    


