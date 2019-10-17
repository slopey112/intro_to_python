# You only need to change line 2.
a = 73
b = 41
c = [1, 2]
c[0] = a
c[1] = b
if c[-1] != 22:
    raise Exception('Try again.')
print('Yay! You solved it!')
