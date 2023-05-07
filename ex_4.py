from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

def init():
    print(
       f'Дан массив: {get_text_color("A=(0.1, -2.4, 12.56, -0.5, 0.4)", COLOR_GREEN)}\n' 
       f'Выдать на печать массив B , все элементы которого определяются по правилу\n'
       f'{get_text_color("b[i] = √(a[i]) - ((i + a[i]) / N)", COLOR_GREEN)}, где {get_text_color("N = 18", COLOR_GREEN)}\n'
       f'Определить значение максимального элемента массива B.'
    )
