# https://www.javatpoint.com/multilevel-inheritance-in-python

"""
Multilevel inheritance is the process of inheriting a derived class from another derived class. In Python,
it can be done at any depth.
"""


class Animal:
    def eat(self):
        print('Eating...')


class Dog(Animal):
    def bark(self):
        print('Barking...')


class BabyDog(Dog):
    def weep(self):
        print('Weeping...')


d = BabyDog()
d.eat()
d.bark()
d.weep()
