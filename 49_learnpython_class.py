# https://www.learnpython.org/en/Classes_and_Objects
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()

print(myobjectx.variable)

myobjectx.function()

myobjecty = MyClass()

myobjecty.variable = "yackity"

print(myobjecty.variable)


# another example
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.color = "red"
car1.value = 60000

car2.name = "Jump"
car2.color = "blue"
car2.value = 10000

# test code
print(car1.description())
print(car2.description())
