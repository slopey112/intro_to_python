import turtle

def circle(t):
    t.circle(100)
    t.forward(10)


def main():
    t = turtle.Pen()
    for i in range(int(input())):
        circle(t)


if __name__ == "__main__":
    main()
