"""
Every Python class keeps following built-in attributes which can be accessed using dot operator :
__dict__ − Dictionary containing the class's namespace.
__doc__ − Class documentation string or none, if undefined.
__name__ − Class name.
__module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
"""


class Employee:
    'Common base class for all employees'

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    empCount = 0

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee('Raunak', 50000, 26)

print("------------------------------------")

print("Employee.__doc__:", emp1.__doc__)  # you can also use : Employee.__doc__
print("Employee.__name__:", Employee.__name__)  # you must use class name
print("Employee.__module__:", emp1.__module__)  # you can also use : Employee.__module__
print("Employee.__bases__:", Employee.__bases__)  # you must use class name
print("Employee.__dict__:", emp1.__dict__)
# you can also use : Employee.__dict__
print("Employee.__dict__:", Employee.__dict__)
