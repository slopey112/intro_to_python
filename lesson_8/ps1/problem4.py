for i in range(1000):
if i % 3 == 0:
print("foo", end="")
elif i % 4 == 0:
if i % 7 == 0:
print("baz", end="")
elif i % 27 == 0:
print("aaa", end="")
else:
print("bar", end="")
elif i % 11 == 0:
print(chr((i % 26) + 96), end="")
else:
print("b", end="")
