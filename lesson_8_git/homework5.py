from datetime import datetime
import time

def my_decorator(func):
    def time_func(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        print(datetime.now() - start_time)

    return time_func

@my_decorator
def hello_name(name: str):
    print(f'Hello {name}!')

hello_name('Vasya')
