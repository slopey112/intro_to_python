# Write a function called add that adds its parameters.

# Testing area.
from random import randint
for i in range(1, 11):
    a = randint(1, 101)
    b = randint(1, 101)
    if a + b == add(a, b):
        print("Test case {} passed.".format(i))
    else:
        print("Test case {} failed.".format(i))
