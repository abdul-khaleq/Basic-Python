class Company:
    def __init__(self, companyName, location)->None:
        self.companyName = companyName
        self.location = location
    def company_details(self):
        print("Company name: ", self.companyName, "Location: ", self.location)

class Person:
    def __init__(self, personName, Age)->None:
        self.personName = personName
        self.age = Age
    def person_details(self):
        print("Name: ", self.personName, "Age: ", self.age)

class Employee(Company, Person):
    def __init__(self, emp_name, emp_age, cpm_name, cmp_location)->None:
        Person.__init__(self, emp_name, emp_age)
        Company.__init__(self, cpm_name, cmp_location)

john = Person('John', 45)
john.person_details()

employee = Employee('Abdul Khaleq', 25, 'IT Sector', 'Bogura')

employee.company_details()
employee.person_details()