# Python program to demonstrate method overriding

# Defining parent class 
class Parent:
    # constructor
    def __init__(self) -> None:
        self.value = "Inside parent"
    
    # parent's show method 
    def show(self):
        print(self.value)

# Defining child class
class Child(Parent):
    # constructor 
    def __init__(self) -> None:
        self.value = "Inside child"
    
    # child's show method 
    def show(self):
        print(self.value)

# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()