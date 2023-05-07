from helpers import get_text_color, input_number, is_question, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

_DEFAULT_N = 18
_MIN_N = -100
_MAX_N = 100
_DEFAULT_MATRIX = [0.1, -2.4, 12.56, -0.5, 0.4]

def _input_n(text: str, default_value: float = None, min: float = None, max: float = None) -> float:
    while True:
        number = input_number(text=text, default_value=default_value, min=min, max=max)
        if number != 0:
            return number
        else:
            print(get_text_color(f"Число должно быть нулем!", COLOR_FAIL))

def init():
    print(
       f'Дан массив: {get_text_color("A=(0.1, -2.4, 12.56, -0.5, 0.4)", COLOR_GREEN)}\n' 
       f'Выдать на печать массив B , все элементы которого определяются по правилу\n'
       f'{get_text_color("b[i] = √(a[i]) - ((i + a[i]) / N)", COLOR_GREEN)}, где {get_text_color("N = 18", COLOR_GREEN)}\n'
       f'Определить значение максимального элемента массива B.'
    )
    n = int(_input_n(
        text=f'Введите целое число N: (по умолчанию {_DEFAULT_N})', 
        default_value=_DEFAULT_N,
        min=_MIN_N,
        max=_MAX_N
    ))
