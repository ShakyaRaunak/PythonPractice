"""
The class has a documentation string, which can be accessed via ClassName.__doc__.
The class_suite consists of all the component statements defining class members, data attributes and functions.
"""


class Employee:
    'Common base class for all employees'

    # __init__ - special method, which is called class constructor or initialization method that Python calls when
    # you create a new instance of this class.
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1
        print(__doc__)
        print(self.__doc__)

    # class_suite
    empCount = 0

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee('Raunak', 50000, 26)

print("------------------------------------")

print(hasattr(emp1, 'age'))  # Returns true if 'age' attribute exists
setattr(emp1, 'age', 27)  # Set attribute 'age' at 27
print(getattr(emp1, 'age'))  # Returns value of 'age' attribute
delattr(emp1, 'age')  # Delete attribute 'age'
# print(getattr(emp1, 'age'))  # AttributeError: 'Employee' object has no attribute 'age'
