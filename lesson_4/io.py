# This section concerns reading from a file.
with open('problem.in', 'r') as f:
    numbers = [int(x) for x in f.readlines()]
for number in numbers:
    print(number)


# Copy and paste this to write to a file.
with open('problem.out', 'w') as f:
    f.write(answer + '\n')
