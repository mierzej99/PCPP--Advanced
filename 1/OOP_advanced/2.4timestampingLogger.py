from datetime import datetime


def simple_decorator(own_function):   
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return own_function

@simple_decorator
def ordinary_addition(a, b):
    return a + b

print(ordinary_addition(3,4))
