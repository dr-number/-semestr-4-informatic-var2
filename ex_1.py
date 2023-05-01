from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

def init():
    print(
        f'Вычислить на заданном интервале значения функции:\n'
        f'        | √(x + 2),   если 0 < x <= 1\n'
        f'y(x) = <  ln(x - 1),  если x > 1\n'
        f'        | 0,          если x <= 0\n\n'
        f'где - 2 <= x <= 2.2;  dx = 0.2\n\n'
        f'На печать вывести значения x и y в виде таблицы с заголовком\n'
    )
    