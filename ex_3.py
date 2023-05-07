from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_WHITE
import math

_DEFAULT_COUNT_ELEMENTS = 16
_DEFAULT_MIN_COUNT_ELEMENTS = 1
_DEFAULT_MAX_COUNT_ELEMENTS = 50

_DEFAULT_LESS_THAN = 0.3
_DEFAULT_MIN_LESS_THAN = 0.1
_DEFAULT_MAX_LESS_THAN = 0.9

_FORMAT = '| {:10} | {:40} | {:35} | {:30} | {:30} |  {:30} |'

def init():
    print(
        f'{get_text_color("Дана последовательность:", COLOR_WARNING)}\n'
        f'{get_text_color("2*sin(x); 3*sin(x/2); 4*sin(x/3); ...; 17*sin(x/16);   где x = ПИ/12", COLOR_GREEN)}\n'
        f'{get_text_color("Найти количество элементов последовательности, которые меньше 0.3, и их порядковые номера.", COLOR_WARNING)}\n'
    )

    count_elements = int(input_number(
        text=f'Введите количество элементов последовательности: (по умолчанию {_DEFAULT_COUNT_ELEMENTS})', 
        default_value=_DEFAULT_COUNT_ELEMENTS,
        min=_DEFAULT_MIN_COUNT_ELEMENTS,
        max=_DEFAULT_MAX_COUNT_ELEMENTS
    ))

    less_than = input_number(
        text=f'Найти числа которые меньше: (по умолчанию {_DEFAULT_LESS_THAN})', 
        default_value=_DEFAULT_LESS_THAN,
        min=_DEFAULT_MIN_LESS_THAN,
        max=_DEFAULT_MAX_LESS_THAN
    )

    print(get_text_color(_FORMAT.format(*[
        '№',
        'Формула', 
        'Значение', 
        'Вычисление (1)', 
        'Вычисление (2)', 
        'Сравнение'
    ]), COLOR_WARNING))

    x = math.pi/12
    result_count_numbers = []
    for i in range(1, count_elements):
        k = 2+i-1
        result = k*math.sin(x/i)

        is_less_then_result = result < less_than
        if is_less_then_result:
            result_count_numbers.append(i)

        print(get_text_color(_FORMAT.format(*[
            f'{i}',
            f'{k} * sin({x} / {i})', 
            f'{k} * sin({x/i})',
            f'{k} * {math.sin(x/i)}',
            f'{result}',
            f'{result} < {less_than}'
        ]), COLOR_GREEN if is_less_then_result else COLOR_WHITE))

    print(
        f'\nПорядковые номера элементов последовательности, которые меньше {less_than}: '
        f'{get_text_color(result_count_numbers, COLOR_GREEN)}'
    )
    print(
        f'Количество элементов последовательности, которые меньше {less_than}: '
        f'{get_text_color(str(len(result_count_numbers)), COLOR_GREEN)}'
    )
