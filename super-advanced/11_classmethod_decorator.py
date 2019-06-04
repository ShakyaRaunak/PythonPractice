class Person:
    totalObjects = 0

    def __init__(self):
        Person.totalObjects = Person.totalObjects + 1

    @classmethod
    def showcount(cls):
        print("Total objects: ", cls.totalObjects)


p1 = Person()
p2 = Person()
Person.showcount()  # Total objects:  2

p3 = Person()
p3.showcount()  # Total objects:  3
