import math

x = 423
x = list(str(x))
x = [int(item) for item in x]

while len(x) > 1:
    x = math.prod(x)
    x = list(str(x))
    x = [int(item) for item in x]

print(x[0])