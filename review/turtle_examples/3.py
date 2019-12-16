from math import atan, degrees, sqrt
import turtle

t = turtle.Pen()
t.up()
t.goto(250, -250)
t.setheading(180)
t.down()
x = 500

while True:
    for i in range(4):
        t.forward(x)
        t.right(90)
    t.forward(0.1 * x)
    t.right(degrees(atan((0.1 * x) / (0.9 * x))))
    x = (x * sqrt(82)) / 10
