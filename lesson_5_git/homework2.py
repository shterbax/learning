var = int(input('Введите секунды:'))

# d = int(var / 86400)
# h = int(var / 3600 - d * 24)
# m = int(var // 3600 % 60)
# s = int(var % 60)
d = var // (24 * 3600)
var %= 24 * 3600
h = var // 3600
var %= 3600
m = var // 60
var %= 60

ost = d % 10

if d == 0 or d < 10 and 4 < ost < 11 or d > 10 and ost == 1 or d > 10 and 3 < ost < 11:
    day = 'днів'
elif d < 10 and 0 < ost < 5 or d > 10 and 1 < ost < 4:
    day = 'дні'
# elif d < 10 and ost > 4 and ost < 11:
#     day = 'днів'
elif d > 20 and ost == 1:
    day = 'день'
# elif d > 10 and ost > 1 and ost < 4:
#     day = 'дні'
# elif d > 10 and ost > 3 and ost < 11:
#     day = 'днів'
# elif d > 10 and ost == 1:
#     day = 'днів'


print(f'{d} {day}, {h}:{m}:{var}')