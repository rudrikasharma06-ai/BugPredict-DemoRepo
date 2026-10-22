def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def power(a, b):
    if b < 0:
        return 1 / power(a, -b)
    return a ** b
