import math

li = [1, 2, 3, 4, 5, 6, 7]

first = math.ceil(len(li) / 2)
second = len(li) - first
if len(li) % 2 != 0:
    if first > 1:
        second += 1

a = li[0:first]
b = li[second:]
print(a)
print(b)