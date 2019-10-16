from random import randint

with open('problem1', 'w') as f:
    for i in range(1000):
        f.write(str(randint(-100, 101)) + '\n')
