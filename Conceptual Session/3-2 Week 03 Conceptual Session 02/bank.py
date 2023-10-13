from abc import ABC, abstractmethod
class Account(ABC):
    accounts = []
    def __init__(self, name, accNumber, password, type) -> None:
        self.name = name
        self.accNo = accNumber
        self.password = password
        self.type = type
        self.balance = 0
        Account.accounts.append(self)
    
    def deposit(self, amount):
        if amount >=0:
            self.balance += amount
        else:
            print('Invalid amount\n')

    def withdraw(self, amount):
        if amount >=0 and amount <= self.balance:
            self.balance -= amount
        else:
            print('Invalid amount\n')
    
    def changeInfo(self, name):
        self.name = name

    # Overloading of method changeInfo 
    def changeInfo(self, name, password):
        self.name = name
        self.password = password
    
    @abstractmethod
    def showInfo(self):
        pass

class SavingsAccount(Account):
    def __init__(self, name, accNumber, password, interestRate) -> None:
        super().__init__(name, accNumber, password, 'savings')
        self.interestRate = interestRate
    
    def showInfo(self):
        print(f'Account info-> Name: {self.name}\nAccount number: {self.accNo}\nAccount type: {self.type}\nBalance: {self.balance}\n')
    
    def applyInterest(self):
        interest = self.balance * (self.interestRate / 100)
        print(f'Applied interest of {self.balance} is {interest}')
        self.deposit(interest)

class SpecialAccount(Account):
    def __init__(self, name, accNumber, password, limit) -> None:
        super().__init__(name, accNumber, password, 'special')
        self.limit = limit
    
    def withdraw(self, amount):
        if amount >=0 and amount <= self.limit:
            self.balance -= amount
        else:
            print('Invalid amount\n')

    def showInfo(self):
        print(f'Account type: {self.type}\nAccount info-> Name: {self.name}\nAccount number: {self.accNo}\nBalance: {self.balance}\n')

currentUser = None
while(True):
    if currentUser == None:
        print("No user logged in")
        ch = input("Login or Register? (L/R)")
        if ch == 'R':
            name = input('Name: ')
            accNo = input('Account number: ')
            password = input('Password: ')
            a = input('Savings or special? (sv/sp): ')
            if a == 'sv':
                iRate = int(input('Interest Rate'))
                currentUser = SavingsAccount(name, accNo, password, iRate)
            elif a == 'sp':
                limit = int(input('Limit'))
                currentUser = SpecialAccount(name, accNo, password, limit)
            else:
                print('Invalid choice')

        elif ch == 'L':
            nu = input('Account number: ')
            for account in Account.accounts:
                if nu == account.accNo:
                    currentUser = account
                    break
    else:
        print(f'Welcome {currentUser.name}!')
        if currentUser.type == 'savings':
            print('1. Show info')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Apply interest')
            print('5. Change info')
            print('6. Logout')
            option = int(input('Choose option: '))
            if option == 1:
                currentUser.showInfo()
            elif option == 2:
                amount = int(input('Amount: '))
                currentUser.deposit(amount)
            elif option == 3:
                amount = int(input('Amount: '))
                currentUser.withdraw(amount)
            elif option == 4:
                currentUser.applyInterest()
            elif option == 5:
                print('Homework')
            elif option == 6:
                currentUser = None
            else:
                print('Invalid choice')
        elif currentUser.type == 'special':
            print('1. Show info')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Change info')
            print('5. Logout')
            option = input('Choose option: ')
            if option == 1:
                currentUser.showInfo()
            elif option == 2:
                amount = int(input('Amount: '))
                currentUser.deposit(amount)
            elif option == 3:
                amount = int(input('Amount: '))
                currentUser.withdraw(amount)
            elif option == 4:
                print('Homework')
            elif option == 5:
                currentUser = None
            else:
                print('Invalid choice')