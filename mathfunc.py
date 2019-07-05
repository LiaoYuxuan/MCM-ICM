def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('Can not divide by zero!')
    return a / b
