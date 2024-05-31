import string

var = input('Input variable:')
a, b = var.split('-')
result = string.ascii_letters

print(result[result.rfind(a):result.rfind(b)+1])
