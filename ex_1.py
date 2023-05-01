from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL, COLOR_OKCYAN
import math

_DEFAULT_START_VALUE = -2
_DEFAULT_MIN_START_VALUE = -100
_DEFAULT_MAX_START_VALUE = -1

_DEFAULT_END_VALUE = 2.2
_DEFAULT_MIN_END_VALUE = 1
_DEFAULT_MAX_END_VALUE = 100

_DEFAULT_STEP = 0.2
_DEFAULT_MIN_STEP = -5
_DEFAULT_MAX_STEP = 5

_FORMAT = '| {:30} | {:30} | {:30} |'

def get_init_data():

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
    while True:
        step = input_number(
            text=f'Введите шаг: (по умолчанию {_DEFAULT_STEP})',
            default_value=_DEFAULT_STEP,
            min=_DEFAULT_MIN_STEP,
            max=_DEFAULT_MAX_STEP
        )

        if step == 0:
            print(get_text_color(f"Шаг не должен быть равен нулю! Повторите ввод!", COLOR_FAIL))
        else:
            break

    return start, end, step


def init():
    print(
        f'Вычислить на заданном интервале значения функции:\n'
        f'        | √(x + 2),   если 0 < x <= 1\n'
        f'y(x) = <  ln(x - 1),  если x > 1\n'
        f'        | 0,          если x <= 0\n\n'
        f'где -2 <= x <= 2.2;  dx = 0.2\n\n'
        f'На печать вывести значения x и y в виде таблицы с заголовком\n'
    )

    start, end, step = get_init_data()
    print(get_text_color(_FORMAT.format(*['х', 'Формула', 'y']), COLOR_WARNING))
    x = start
    count = 0
    while start <= x <= end:
        y, formul = '', ''

        if 0 < x <= 1:
            formul = f'√({x} + 2)' 
            y = math.sqrt(x + 2)
            print(get_text_color(_FORMAT.format(*[x, formul, y]), COLOR_GREEN))
        elif x > 1:
            formul = f'ln({x} - 1)'
            y = math.log(x - 1)
            print(get_text_color(_FORMAT.format(*[x, formul, y]), COLOR_OKCYAN))
        elif x <= 0:
            formul, y = '0', 0
            print(_FORMAT.format(*[x, formul, y]))
        
        count += 1
        x += step

    print(f'\nКоличество элементов: {count}')
    