class BankAccount: 
    # constructor
    
    def __init__(self, accountOwnerName, routingNumber, accountNumber, accountBalance):
        self.accountOwnerName = accountOwnerName
        self.routingNumber = routingNumber
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance
# function

    def deposit(self,x):
        self.accountBalance += x
        print(self.accountOwnerName, self.accountBalance)
    
sarahsBankAccount = BankAccount("sarah:", "948784", "9737739", 100)
jerrysBankAccount = BankAccount("jerry:", "92890948", "47777", 200)

sarahsBankAccount.deposit(300)
jerrysBankAccount.deposit(300)

print(sarahsBankAccount.accountOwnerName, sarahsBankAccount.accountNumber)
print(jerrysBankAccount.accountOwnerName, jerrysBankAccount.accountNumber)