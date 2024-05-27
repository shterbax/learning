import keyword
a = str(input('Variable:'))

allowed_s = set('qwertyuiopasdfghjklzxcvbnm_1234567890')

if set(a).issubset(allowed_s):
    if a[0].isdigit():
        print('False')
    elif keyword.iskeyword(a):
        print('False')
    elif a.count('_') > 1 or a.count('_') < 1:
        print('False')
    else:
        print('True')
else:
    print('False')

