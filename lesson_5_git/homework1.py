import string

var = 'b-H'
a, b = var.split('-')
result = string.ascii_letters

print(result[result.rfind(a):result.rfind(b)+1])
