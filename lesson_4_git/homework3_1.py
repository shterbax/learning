import string

a = 'Should, I. subscribe? Yes!'
result = ''

for x in a:
    for sp in string.punctuation:
        if sp == x:
            x = x.replace(sp, '')
    result += x

result = result.title()
result = result.replace(' ', '')

print('#' + result[0:140])
