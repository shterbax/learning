from functools import wraps


def func_name_logger(f):

    def decorator(*args, **kwargs):
        name = f.__name__

        print(f'Name: {name}')
        print(f'Arguments: {args}, {kwargs}')
        print('Result:')

        return f(*args, **kwargs)

    return decorator

@func_name_logger
def any_functions(a, b, name, age):
    print(f'a = {a}, b = {b}, name is {name} and age is {age}')

any_functions(8, 4, name='Oleg', age=22)

