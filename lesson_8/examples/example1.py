def sum_of_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_of_n(1))
print(sum_of_n(5))
print(sum_of_n(10))
print(sum_of_n(100000))
