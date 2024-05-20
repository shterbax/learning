from random import random

li = [0, 1, 0, 12, 3]

li.sort(key=bool, reverse=True)

print(li)