class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def  display_info(self):
        print(f"Имя: {my_student.name}, ID: {my_student.student_id}")
    
my_student = Student("Розанна Пак", "444")
my_student.display_info()

class Group:
    def __init__(self):
        self.student = []
group = Group()
print(group.student)
