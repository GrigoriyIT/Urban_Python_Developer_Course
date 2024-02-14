def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f'Ошибка: невозможно преобразовать {s} в целое число.'


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл '{filename}' не найден"
    except IOError:
        return f'Ошибка ввода/вывода при работе с файлом {filename}'


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка - на Ноль делить нельзя'
    except TypeError:
        return 'Ошибка: аргументы должен быть число'


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'Ошибка: индекс {index} вне списка'
    except TypeError:
        return f'Ошибка: индекс должен быть целым числом'
