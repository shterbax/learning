x = 'y'

while x == 'y':
    a = int(input('First number:'))
    b = int(input('Second number:'))
    op = input('Operation:')

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

    x = str(input('Do u want continue? (y/n):'))
