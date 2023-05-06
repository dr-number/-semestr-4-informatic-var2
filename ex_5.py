from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL
import math
_FORMAT = '| {:10} | {:30} | {:20} | {:20} | {:30} | {:40} | {:20} |'

def init():
    print(
        f'Вычислить значения функции: {get_text_color("f= G(x) + R(y)", COLOR_GREEN)}, где\n'
        f'G(x) = ( sin(x) + 2 ) / ( sin(x + 2/3 * ПИ) ),    -ПИ/2 <= x <= ПИ/2,     dx = ПИ/8\n'
        f'R(y) = (2 * sin(y)) / (cos^3(y)),     1 <= y <= 2; dy = 0.25'
    )

    start_x = math.pi/2
    step_x = math.pi/8
    x = -start_x

    start_y = 1
    step_y = 0.25
    y = start_y

    print(get_text_color(_FORMAT.format(*[
        'G(x) = ( sin(x) + 2 ) / ( sin(x + 2/3 * ПИ) )',  
        'G(x) Вычисление (1)',
        'G(x) Вычисление (2)',
        'G(x) Результат',
        'R(y) = (2 * sin(y)) / (cos^3(y))',  
        'R(y) Вычисление (1)',
        'R(y) Вычисление (2)',
        'R(y) Результат'
        'f = G(x) + R(y)'
    ]), COLOR_WARNING))

    _2_3_pi = 2/3 * math.pi
    while -start_x <= x <= start_x and 1 <= y <= 2:
        g_x = (math.sin(x) + 2) / math.sin(x + _2_3_pi)
        r_y = (2 * math.sin(y)) / (math.pow(math.cos(y), 3))
        print(_FORMAT.format(*[
            f'( sin({x}) + 2 ) / ( sin({x} + {_2_3_pi}) )',  
            f'{math.sin(x) + 2} / sin({x + _2_3_pi})',
            f'{math.sin(x) + 2} / {math.sin(x + _2_3_pi)}',
            f'{g_x}',
            f'(2 * sin({y})) / (cos^3({y}))',  
            'Вычисление (1)',
            'Вычисление (2)',
            f'{r_y}',
            'f = G(x) + R(y)'
        ]))
