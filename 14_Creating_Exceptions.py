class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def water(t):
    if type(t) is int or type(t) is float:
        if not 0 < t < 100:
            raise ProcessingException('Это не вода')
    else:
        raise InvalidDataException('Ввели не число')
    print(f'Температура воды {t} градусов')


def input_t(t):
    try:
        water(t)
    except ProcessingException as exc:
        print(f'{exc}. Температура должна быть от 0 до 100')
    except InvalidDataException as exc:
        print(f'{exc}. Температура должна быть числом')


input_t(5)
input_t(500)
input_t('asd')
