class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f'You can not withdraw less than {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'You can not withdraw more than {self.max_withdraw}'
        else:
            self.balance -=amount
            return f'take your money {amount} and the rest of money after withdraw {self.get_balance()}'
brac = Bank(10000)
print(brac.withdraw(90))
print(brac.withdraw(1000000))
print(brac.withdraw(10005))
