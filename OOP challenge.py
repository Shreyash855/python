class Account():
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return 'Account owner: {}\nAccount balance: ${}'.format( self.owner,self.balance)
    
    def deposit(self,d):
        self.d = d
        self.balance = self.balance + self.d
        print('Deposit Accepted')
        
    def withdraw(self,w):
        self.w = w
        if self.w <= self.balance:
            self.balance = self.balance - self.w
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable')

acct1 = Account('Shreyash',1000)
print(acct1)
acct1.deposit(1000)
acct1.withdraw(50)
acct1.balance
acct1.owner