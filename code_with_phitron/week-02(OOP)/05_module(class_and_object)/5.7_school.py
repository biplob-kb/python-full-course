class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_cls = current_class

    def __repr__(self)-> str:
        return f"Student name: {self.name}, class: {self.current_cls}, id: {self.id}"

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"Teacher: {self.name}, subject: {self.subject}, id: {self.id}"

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, crr_cls):
        id = len(self.students) + 1
        student = Student(name, crr_cls, id)
        self.students.append(student)


# alex = Student("Alex", 10, 1);
# bob = Teacher('Bob', 'Algorithm', 101)


sahin_school = School("Sahin School")
sahin_school.add_teacher('Ms Dhoni', 'Algorithm')
sahin_school.add_teacher('Sachin Tendulker', 'DSA')

sahin_school.enroll('Rohit Sharma', 9)
sahin_school.enroll('Virat Kholi', 10)

print(sahin_school.name)
print("All teachers: \n", sahin_school.teachers)
print("All students: \n", sahin_school.students)

