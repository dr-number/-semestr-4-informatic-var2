from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_OKCYAN, COLOR_GREEN, COLOR_FAIL
import math

_DEFAULT_START_VALUE = 1
_DEFAULT_MIN_START_VALUE = 1
_DEFAULT_MAX_START_VALUE = 10

_DEFAULT_END_VALUE = 20
_DEFAULT_MIN_END_VALUE = 20
_DEFAULT_MAX_END_VALUE = 50

_FORMAT = '| {:10} | {:30} | {:20} | {:20} | {:30} | {:40} | {:20} |'

def init():
    print(
        f'Дана последовательность: a(k) = ln(k^2 - 4k + 8);    k=1,2...,20.\n'
        f'Вычислить произведение всех элементов этой последовательности.\n'
    )

    start = input_number(
        text=f'Введите начальное значение: (по умолчанию {_DEFAULT_START_VALUE})', 
        default_value=_DEFAULT_START_VALUE,
        min=_DEFAULT_MIN_START_VALUE,
        max=_DEFAULT_MAX_START_VALUE
    )
    end = input_number(
        text=f'Введите конечное значение: (по умолчанию {_DEFAULT_END_VALUE})', 
        default_value=_DEFAULT_END_VALUE,
        min=_DEFAULT_MIN_END_VALUE,
        max=_DEFAULT_MAX_END_VALUE
    )

    print(get_text_color(_FORMAT.format(*[
        '№', 
        '[1] ln(k^2 - 4*k + 8)', 
        '[2]',
        '[3]',
        'Результат',
        'Произведение',
        'Сумма'
    ]), COLOR_WARNING))
    multiplikation = 1
    for k in range(start, end):
        result = math.log(k*k - 4*k + 8)
        print(_FORMAT.format(*[
            k,
            f'ln({k}^2 - 4*{k} + 8)', 
            f'ln({k*k} - {4*k} + 8)', 
            f'ln({k*k - 4*k + 8})', 
            get_text_color(result, COLOR_OKCYAN),
            f'{result} * {multiplikation}',
            get_text_color(multiplikation * result, COLOR_OKCYAN),
        ]))
        multiplikation *= result

    print(f'\nКоличество элементов: {get_text_color(end - start, COLOR_GREEN)}')
    print(f'Произведение всех элементов последовательности {get_text_color(multiplikation, COLOR_GREEN)}')