#li = [1, 5, 7, 4, 8, 9, 8]
#li.reverse()
#li.append(li[0])
#li.reverse()
#li.pop()
#print(li)

#li_1 = li[::-1]
#print(li_1)

li = [1, 5, 7, 4, 8, 9, 8]

li.insert(0, li[-1])
li.pop()

print(li)