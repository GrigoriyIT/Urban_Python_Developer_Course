class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


try:
    raise InvalidDataException('Данные не верные')
except InvalidDataException as exc:
    print(f'Исключение {exc}')
    raise ProcessingException('Исключение обработки')
