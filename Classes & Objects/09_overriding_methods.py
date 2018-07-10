# https://www.tutorialspoint.com/python/python_classes_objects.htm

"""
You can always override your parent class methods. One reason for overriding parent's methods is because you may want
special or different functionality in your subclass.
"""


class Parent:  # define parent class
    def myMethod(self):
        print('Calling parent method')


class Child(Parent):  # define child class
    def myMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.myMethod()  # child calls overridden method
