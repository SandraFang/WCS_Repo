#define the Student class
class Student:
    def __init__(self, name, age, grades):
        self.name =name
        self.age =age
        self.grades =grades
    #method to show info
    def show_info(self):
        print(f"Name:{self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade()}")
    def average_grade(self):
        if len(self.grades)==0:
            return 0
        else:
            return sum(self.grades)/len(self.grades)
    
# list to fill students
students = []

while True:
    print ("Student Database System")
    selection = input("Please select: add, view, exit:")

    if selection == "add":
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        grades_input = input("Enter grades separated by commma: ")
        grades = [float(g) for g in grades_input.split(",")]
        students.append(Student(name,age,grades))


    elif selection == "view":
        if not students:
            print("no records yet")
        else:
            for s in students:
                s.show_info()

    #exit
    elif selection == "exit":
        print ("Goodbye")
        break
    else:
        print("invalid selection, please try again!")