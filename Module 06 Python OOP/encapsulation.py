# encapsulation --> hode details
# access modifier: public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposit)->None:
        self.holder_name = holder_name # public
        self._branch = 'Sherpur Highway' # protected
        self.__balance = initial_deposit # private
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    def withdraw(self, amount):
        if amount <self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'You dont have {amount} Taka in your account'

abdulKhaleq = Bank('Abdul Khaleq', 10000)
print(abdulKhaleq.holder_name)
abdulKhaleq.deposit(3000)
print(abdulKhaleq.get_balance())
print(abdulKhaleq._branch)
print(abdulKhaleq._Bank__balance)