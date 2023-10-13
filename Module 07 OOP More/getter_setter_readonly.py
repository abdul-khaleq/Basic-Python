#  read only --> you can not set the value. Value can not be changed
# getter --> get a value of a property . Most of the time, you will get the value of a private attribute 
# setter --> Set a value of a property through a method. Most of the time, you will set the value of a private attribute
class User:
    def __init__(self, name, age, money) -> None:
       self._name = name
       self._age = age
       self.__money = money
    # getter without any setter is readonly attribute 
    @property
    def age(self):
        return self._age
    # getter
    @property
    def salary(self):
        return self.__money
    # setter 
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'Salary can not be negative'
        self.__money +=value

labib = User('Labib Hasan', 6, 10000)
print(labib.age)
print(labib.salary)

labib.salary = 3000
print(labib.salary)