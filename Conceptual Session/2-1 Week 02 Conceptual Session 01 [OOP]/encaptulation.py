# Public 
class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
    def details(self):
        print("The name of the student is: ", self.name, "and ID is: ", self.id)

ob = Student('Abdul Khaleq', 69)
ob.details()
print("Before change")
print(ob.id)
ob.id = 0
print("Before change")
print(ob.id)

# Private 
class Teacher:
    def __init__(self, name, id) -> None:
        self.name = name
        self.__id = id
    def details(self):
        print("The name of the teacher is: ", self.name, "and ID is: ", self.__id)

ob = Teacher('Labib Hasan', 3)
ob.details()
print("Before change")
ob.__id = 0
print("Before change")
ob.details()
print(ob.__dict__)