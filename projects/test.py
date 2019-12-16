from turtle import *
from time import sleep
from random import randint

gap = 20
lines = 20
track_length = 100
turtles = 5
colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']

penup()
speed(0)
for i in range(lines):
    write(i)
    forward(gap)
backward(lines * gap)
for i in range(lines):
    pendown()
    right(90)
    forward((turtles + 1) * 50)
    backward((turtles + 1) * 50)
    left(90)
    penup()
    forward(gap)
pendown()
speed(6)
pen = [Turtle() for i in range(turtles)]
for i in range(len(pen)):
    pen[i].shape('turtle')
    pen[i].color(colors[i % len(colors)])
    pen[i].speed(1)
    pen[i].up()
    pen[i].setheading(270)
    pen[i].forward(50 * (i + 1))
    pen[i].setheading(0)
    pen[i].down()
while len([i for i in pen if i.pos()[0] <= gap * lines]) > 0:
    for turtle in pen:
        turtle.forward(randint(1, 5))
sleep(5)
