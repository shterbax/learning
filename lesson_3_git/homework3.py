import random

li = []

n = random.randint(3, 10)

while n <= 10:
    li.append(random.randint(1, 9))
    n += 1

print(li)
print([li[0], li[2], li[-2]])