from math import atan, degrees, sqrt
import turtle

turtles = [turtle.Pen(), turtle.Pen()]
for t in turtles:
    t.up()
    t.speed(0)
    t.goto(250, -250)
    t.setheading(180)
    t.down()
x = 500

while True:
    for i in range(4):
        for t in turtles:
            t.forward(x)
            t.right(90)
    turtles[0].forward(0.1 * x)
    turtles[1].forward(0.9 * x)
    deg = degrees(atan((0.1 * x) / (0.9 * x)))
    turtles[0].right(deg)
    turtles[1].right(90 - deg)
    x = (x * sqrt(82)) / 10
