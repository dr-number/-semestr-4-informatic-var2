from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

_DEFAULT_ROWS = 3
_DEFAULT_COLS = 5
_MIN_VALUE = -20
_MAX_VALUE = 20

def init():
    print(
        'Дана матрица A(3,5):\n'
        'Вычислить элементы массива Y по правилу:\n'
        f'{get_text_color("y[j] = Sin(x[j])", COLOR_GREEN)}, где\n'
        'x[j] - сумма положительных элементов j-го столбца матрицы A.\n'
    )
