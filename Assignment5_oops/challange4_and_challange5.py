class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        # write code here
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        # write code here
        return self.balance * self.interestRate / 100

#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object
demo1.deposit(500)
# balance = demo1.getBalance()
# print(balance) 


demo1.withdrawal(500)
balance = demo1.getBalance()
print("Balance:",balance)  


interest_amount = demo1.interestAmount()
print("Interest:",interest_amount)  