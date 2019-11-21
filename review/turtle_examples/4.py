from math import atan, degrees, sqrt
import turtle

turtles = [turtle.Pen() for x in range(4)]
for t in turtles:
    t.up()
    t.speed(0)
    t.setheading(180)
turtles[0].goto(250, -250)
turtles[1].goto(0, 0)
turtles[2].goto(250, 0)
turtles[3].goto(0, -250)
for t in turtles:
    t.down()
x = 250

while True:
    for i in range(4):
        for t in turtles:
            t.forward(x)
            t.right(90)
    for t in turtles:
        t.forward(0.1 * x)
        t.right(degrees(atan((0.1 * x) / (0.9 * x))))
    x = (x * sqrt(82)) / 10
