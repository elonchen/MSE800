class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    
    def display(self):
        print ("Student: ", self.name, self.age, self.id)

# global variable to store data
student_list = []

def collect_data(student):
    student_list.append(student)

def print_table_by_age():
    print("print out a list of student, age in order")
    student_list.sort(key=lambda s: s.age)

    # Print each student using display()
    for student in student_list:
        student.display()

if __name__ == "__main__":
    stu1 = Student("Alex", 30, "2001")
    stu2 = Student("Ben", 25, "2008")
    stu3 = Student("Sam", 36, "2005")
    collect_data(stu1)
    collect_data(stu2)
    collect_data(stu3)
    print_table_by_age()