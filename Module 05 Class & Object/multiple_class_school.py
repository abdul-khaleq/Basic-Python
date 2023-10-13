class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    def __repr__(self)-> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'

class Teacher:
    def __init__(self, name, subject, id)->None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self)->str:
        return f'Techer: {self.name}, subject: {self.subject}'

class School:
    def __init__(self, name)->None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    
    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money: {fee - 6500}'
        
    def __repr__(self)->str:
            print('Welcome to', self.name)
            print('--------OUR Teachers-------')
            for teacher in self.teachers:
                print(teacher)
            print('--------OUR Students-------')
            for student in self.students:
                print(student)
            return 'All done for now'


# abdulKhaleq = Student('Abdul Khaleq', 12, 1)
# labib = Teacher('Labib Hasan', 'English', 101)
# print(abdulKhaleq)
# print(labib)
phitron = School('Pritron')
phitron.enroll('Abdul Khaleq', 5200)
phitron.enroll('Labib Hasan', 8000)
phitron.enroll('Abdullah', 7000)
phitron.enroll('Monu', 90000)

phitron.add_teacher('Tom Cruise', 'Algorithm')
phitron.add_teacher('Decap', 'DSA')
phitron.add_teacher('AJ', 'DataBase')

print(phitron)