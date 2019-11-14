def a_count(word):
    total = 0
    for i in word:
        if i == "a":
            total += 1
    return total


print(a_count("a"))
print(a_count("alphabet"))
print(a_count("aaaaaaaaaaaaaaa"))
print(a_count("abbbbbb"))
