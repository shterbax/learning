import math

x = input('Input number:')
x = list(str(x))
x = [int(item) for item in x]

while len(x) > 1:
    x = math.prod(x)
    x = list(str(x))
    x = [int(item) for item in x]

print(x[0])
