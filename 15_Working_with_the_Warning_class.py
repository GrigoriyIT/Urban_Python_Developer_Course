import warnings


def division_by(a, b):
    try:
        print(a / b)
        if 0.01 > b > 0:
            warnings.warn('Делитель меньше 0,01', category=UserWarning)  # мессадж из этоой строки не выйдет в
            # консоль, т.к. мы отловим эту ошибку в except благодаря warnings.simplefilter('error')
    except UserWarning:
        print('Поймали делитель меньше 0.01')
    except ZeroDivisionError:
        print('На ноль делить нельзя')


warnings.simplefilter('error')

division_by(10, 0)

division_by(10, 0.001)

# выхлоп
# На ноль делить нельзя
# 10000.0
# Поймали делитель меньше 0.01
