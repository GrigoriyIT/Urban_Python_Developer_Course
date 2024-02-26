def mult2(x):
    return x ** 2


def is_odd(x):
    return x % 2


my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = (filter(is_odd, map(mult2, my_numbers)))
print(list(result))
