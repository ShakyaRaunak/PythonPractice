# https://codeclubprojects.org/en-GB/python/turtle-race/
from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

goblin = Turtle()
goblin.color('green')
goblin.shape('turtle')

goblin.penup()
goblin.goto(-160, 40)
goblin.pendown()

yippy = Turtle()
yippy.color('yellow')
yippy.shape('turtle')

yippy.penup()
yippy.goto(-160, 10)
yippy.pendown()

for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    goblin.forward(randint(1, 5))
    yippy.forward(randint(1, 5))
