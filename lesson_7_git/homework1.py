def add_one(some_list):
    result = ''

    for number in some_list:
        result += str(number)

    result = int(result) + 1

    return list(map(int, str(result)))


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
