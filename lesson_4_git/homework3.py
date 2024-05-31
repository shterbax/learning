import string

a = 'Python Community'
a = a.title()
a = a.replace(' ', '')
for x in a:
    if x in string.punctuation:
        print('False')
        break
    else:
        print('#' + a[0:140])
        break
