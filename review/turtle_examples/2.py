import turtle

t = turtle.Pen()
t.goto(-300, 0)
n = 600
t.setheading(90)
colors = ["yellow", "orange", "red", "purple", "blue", "green"]
c = 0
while True:
    n = round(n / 2)
    t.fillcolor(colors[c])
    t.begin_fill()
    for i in range(5):
        t.forward(n)
        t.right(90)
    t.end_fill()
    t.forward(n)
    c += 1
    c %= len(colors)
