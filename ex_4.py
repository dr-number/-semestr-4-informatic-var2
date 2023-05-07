from helpers import get_text_color, input_number, is_question, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL
import random

_DEFAULT_N = 18
_MIN_N = -100
_MAX_N = 100
_DEFAULT_ARRAY = [0.1, -2.4, 12.56, -0.5, 0.4]
_DEFAULT_COUNT_ARRAY = len(_DEFAULT_ARRAY)
_MIN_COUNT_ARRAY = _DEFAULT_COUNT_ARRAY
_MAX_COUNT_ARRAY = 50
_MIN_VALUE_ARRAY = -20
_MAX_VALUE_ARRAY = 20

def _input_n(text: str, default_value: float = None, min: float = None, max: float = None) -> float:
    while True:
        number = input_number(text=text, default_value=default_value, min=min, max=max)
        if number != 0:
            return number
        else:
            print(get_text_color(f"Число должно быть нулем!", COLOR_FAIL))

def init():
    print(
       'Дан массив: ' + get_text_color("A = (" + ', '.join(str(x) for x in _DEFAULT_ARRAY) + ")", COLOR_GREEN) + '\n' 
       f'Выдать на печать массив B , все элементы которого определяются по правилу\n'
       f'{get_text_color("b[i] = √(a[i]) - ((i + a[i]) / N)", COLOR_GREEN)}, где {get_text_color("N = 18", COLOR_GREEN)}\n'
       f'Определить значение максимального элемента массива B.\n'
    )
    n = int(_input_n(
        text=f'Введите целое число N: (по умолчанию {_DEFAULT_N})', 
        default_value=_DEFAULT_N,
        min=_MIN_N,
        max=_MAX_N
    ))
    array = _DEFAULT_ARRAY
    if is_question("Хотите изменить исходный массив?"):
        array = []
        size = int(input_number(
            text=f'Введите размер массива: (по умолчанию {_DEFAULT_COUNT_ARRAY})', 
            default_value=_DEFAULT_COUNT_ARRAY,
            min=_MIN_COUNT_ARRAY,
            max=_MAX_COUNT_ARRAY
        ))
        if is_question("Хотите ввести массив вручную?"):
            for i in range(0, size):
                array.append(
                    int(
                        input_number(
                            text=f'Введите значение {i + 1} из {size}', 
                            min=_MIN_VALUE_ARRAY,
                            max=_MAX_VALUE_ARRAY
                        )
                    )
                )
        else:
            for i in range(0, size):
                array.append(int(random.uniform(_MIN_VALUE_ARRAY, _MAX_VALUE_ARRAY)))



