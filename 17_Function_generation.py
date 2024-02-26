# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции
# (например, деление, умножение) в зависимости от переданных аргументов.

def create_operation(operation):
    if operation == 'division':
        def division(x, y):
            return x / y

        return division
    elif operation == 'multiplication':
        def multiplication(x, y):
            return x * y

        return multiplication
    # else:
    #     print('Я могу принимать только аргументы division или multiplication')


try:
    my_func_add = create_operation('multiplication')
    print(my_func_add(3, 5))
    my_func_add = create_operation('division')
    print(my_func_add(3, 5))
    my_func_add = create_operation('division')
    print(my_func_add(3, 0))
except ZeroDivisionError:
    print('На НОЛЬ делить нелельзя!!!')

# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции
# и написать такую же функцию с использованием def. Например, возведение числа в квадрат

squared = lambda x: x ** 2
print(squared(4))


def squared_def(x):
    return x ** 2


print(squared_def(4))


# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.


class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


print(f'Площадь = {Rect(3, 5).__call__()}')  # Тут если __call__() не добавить,
                                                   # то не число, а адрес в памяти выходит
