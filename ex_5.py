from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

def init():
    print(
        f'Вычислить значения функции: {get_text_color("f= G(x) + R(y)", COLOR_GREEN)}, где\n'
        f'G(x) = ( sin(x) + 2 ) / ( sin(x + 2/3 * ПИ) ),    -ПИ/2 <= x <= ПИ/2,     dx = ПИ/8\n'
        f'R(y) = (2 * sin(y)) / (cos^3(y)),     1 <= y <= 2; dy = 0.25'
    )
