li = [0, 1, 7, 2, 4, 8]

sum = 0

if len(li) != 0:
    for x in li[::2]:
        sum += x

    print(sum * li[-1])
else:
    print(0)