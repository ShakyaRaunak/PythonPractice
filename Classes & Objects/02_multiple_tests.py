# A class is a blueprint for the object.
class Person:

    # A constructor is a class function that begins with double underscore (_). The name of the constructor is always
    # the same __init__().

    # The __init__() function is called automatically every time the class is being used to create a new object.
    # While creating an object, a constructor can accept arguments if necessary. When we create a class without
    # a constructor, Python automatically creates a default constructor that doesn't do anything.
    def __init__(self, h, w):
        self.height = h
        self.weight = w

    # The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.
    # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any
    # function in the class:
    def setHandW(mysillyobject, h, w):  # def setHandW(self, h, w):
        mysillyobject.height = h
        mysillyobject.weight = w

    def walk(self):
        print(f'I walk! with {self.height} cm and {self.weight} kg.')


p1 = Person(130, 50)
# p1.setHandW(170, 80)
p1.height = 199
p1.__init__(140, 60)

# You can create a new attribute for an object and read it well at the time of defining the values.
p1.color = 'white'
print(p1.color)

print(str(p1))  # <__main__.Person object at 0x000001FAFDEAE208>
print(repr(p1))  # <__main__.Person object at 0x000001FAFDEAE208>

# delete properties on objects by using the del keyword:
# del p1.height

p1.walk()

# delete objects by using the del keyword:
# del p1
# print(p1)
