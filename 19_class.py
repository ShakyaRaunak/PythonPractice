""" There are also some special attributes that begins with double underscore (__).
    For example: __doc__ attribute. It is used to fetch the docstring of that class.
    When we define a class, a new class object is created with the same class name.
    This new class object provides a facility to access the different attributes as well as to instantiate new objects of that class.
"""


class Student:
    "This is a student class"

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def displayStudent(self):
        print("rollno: ", self.rollno, ", name: ", self.name)

    def show(self, name):
        print("Hello", name)


std1 = Student(1, "Raunak")
std2 = Student(2, "Patrick")
std1.displayStudent()
std2.displayStudent()
std2.show("Patrick")
