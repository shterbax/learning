a = int(input())
b = int(input())
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
else:
    if b != 0:
        print(a / b)
    else:
        print('na 0 ne delem')



