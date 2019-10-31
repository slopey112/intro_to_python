from math import sqrt, ceil

for i in range(3, 101):
print(i, end=": ")
for j in range(2, ceil(sqrt(i)) + 1):
if i % j == 0:
print((j, round(i / j)), end=" ")
print()
