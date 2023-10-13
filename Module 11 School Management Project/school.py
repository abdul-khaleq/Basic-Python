class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        # composition 
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        if subject in self.teachers:
            self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            # TODO: set student id, (roll num) at the time of adding the student
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom as named {className}')

    def __repr__(self) -> str:
        print('------All Classroms-------')
        for key, value in self.classrooms.items():
            print(key)
        print('-------Students---------')
        eight = self.classrooms['eight']
        print(len(eight.students))
        for student in eight.students:
            print(student.name)

        print('-------Subjects---------')
        print(len(eight.subjects))
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)

        print('-------Subjects Exam Marks---------')
        for key, value in eight.students[0].marks.items():
            print(key)

        return ''
    
class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 30
    
    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            
class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        # composition 
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name} - {len(self.students) + 1}'
        student.id =serial_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.subjects)
        
    def __str__(self) -> str:
        return f'{self.name} - {len(self.students)}'
    
    # TODO: sort astudnts by grade 
    def get_top_students(self):
        pass
