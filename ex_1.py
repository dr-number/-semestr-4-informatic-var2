from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL
_DEFAULT_START_VALUE = -2
_DEFAULT_END_VALUE = 2.2
_DEFAULT_STEP = 0.2

def init():
    print(
        f'Вычислить на заданном интервале значения функции:\n'
        f'        | √(x + 2),   если 0 < x <= 1\n'
        f'y(x) = <  ln(x - 1),  если x > 1\n'
        f'        | 0,          если x <= 0\n\n'
        f'где - 2 <= x <= 2.2;  dx = 0.2\n\n'
        f'На печать вывести значения x и y в виде таблицы с заголовком\n'
    )

    start = input_number(f'Введите начальное значение: (по умолчанию {_DEFAULT_START_VALUE})', _DEFAULT_START_VALUE)
    end = input_number(f'Введите конечное значение: (по умолчанию {_DEFAULT_END_VALUE})', _DEFAULT_END_VALUE)
    step = input_number(f'Введите шаг: (по умолчанию {_DEFAULT_STEP})', _DEFAULT_STEP)

    table = []
    
    for i in range(start, end, step):
        table.append([i, 0])

    print(table)

