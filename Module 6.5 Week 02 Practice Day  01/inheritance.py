# Inheritance is a mechanism that allows us to create a hierarchy of classes that share a set set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class. 

class Person:
    def __init__(self, name):
        self.name = name
    
    # to get name 
    def getName(self):
        return self.name
    
    # to check if this person is an employee 
    def isEmployee(self):
        return False

# Inherited or subclass 
class Employee(Person):
    # Here we return true 
    def isEmployee(self):
        return True

# Driver code
emp = Person('Abdul Khaleq') # an object of person
print(emp.getName(), emp.isEmployee())

emp = Employee('AK') # An object of Employee
print(emp.getName(), emp.isEmployee())