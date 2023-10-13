from school import School, ClassRoom, Subject
from Persons import Student, Teacher

def main():
    school = School('School Name', 'Bogura')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    labib = Student('Labib Hasan', eight)
    school.student_admission(labib)
    labib2 = Student('Labib', eight)
    school.student_admission(labib2)

    # subjects 
    physics_teacher = Teacher('Shahjahan Tapon Rana')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Haradon')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher('Paoyadon')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)
    
    eight.take_semester_final()
    print(school)

    
    
if __name__ == '__main__':
    main()
