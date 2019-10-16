import turtle

t = turtle.Pen()

while True:
    move = input()
    if move == 'w':
        t.setheading(90)
        t.forward(distance)
    elif move == 's':
        t.setheading(270)
        t.forward(distance)
    elif move == 'a':
        t.setheading(180)
        t.forward(distance)
    elif move == 'd':
        t.setheading(0)
        t.forward(distance)
