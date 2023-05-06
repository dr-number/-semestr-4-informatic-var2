from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN
import math
_FORMAT = '| {:50} | {:20} | {:25} | {:35} | {:25} | {:25} | {:25} |'

def init():
    print(
        f'Вычислить значения функции: {get_text_color("f= G(x) + R(y)", COLOR_GREEN)}, где'
    )
    print(
        f'{get_text_color("G(x) = ( sin(x) + 2 ) / ( sin(x + 2/3 * ПИ) ),    -ПИ/2 <= x <= ПИ/2,     dx = ПИ/8", COLOR_GREEN)}'
    )
    print(
        f'{get_text_color("R(y) = (2 * sin(y)) / (cos^3(y)),                 1 <= y <= 2; dy = 0.25", COLOR_GREEN)}'
    )

    start_x = math.pi/2
    step_x = math.pi/8
    x = -start_x

    start_y = 1
    step_y = 0.25
    y = start_y

    print("\n" + _FORMAT.format(*[
        'G(x) = ( sin(x) + 2 ) / ( sin(x + 2/3 * ПИ) )',  
        'G(x) Вычисление (1)',
        f'{get_text_color("G(x) Результат", COLOR_GREEN)}',
        'R(y) = (2 * sin(y)) / (cos^3(y))',  
        'R(y) Вычисление (1)',
        f'{get_text_color("R(y) Результат", COLOR_GREEN)}',
        f'{get_text_color("f = G(x) + R(y)", COLOR_GREEN)}'
    ]))

    _2_3_pi = round(2/3 * math.pi, 2)
    while -start_x <= x <= start_x and 1 <= y <= 2:
        g_x = (math.sin(x) + 2) / math.sin(x + _2_3_pi)
        r_y = (2 * math.sin(y)) / (math.pow(math.cos(y), 3))
        print(_FORMAT.format(*[
            f'( sin({round(x, 2)}) + 2 ) / ( sin({round(x, 2)} + {round(_2_3_pi, 2)}) )',  
            f'{round(math.sin(x) + 2, 2)} / sin({round(x + _2_3_pi, 2)})',
            f'{get_text_color(round(g_x), COLOR_GREEN)}',
            f'(2 * sin({round(y, 2)})) / (cos^3({round(y, 2)}))',  
            f'(2 * {round(math.sin(y), 2)}) / ({round(math.cos(y), 2)}^3)',  
            f'{get_text_color(round(r_y), COLOR_GREEN)}',
            f'{get_text_color(g_x + r_y, COLOR_GREEN)}'
        ]))
        y += step_y
        x += step_x
