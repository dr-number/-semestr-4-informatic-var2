from helpers import create_matrix, print_matrix, get_text_color, COLOR_GREEN

_DEFAULT_ROWS = 3
_DEFAULT_COLS = 3
_MIN_VALUE = -20
_MAX_VALUE = 20

def init():
    print(
        'Дана матрицa B 3*3\n'
        'Заменить отрицательные элементы матрицы нулями. На печать вывести исходную и полученную матрицы.\n'
    )
    matrix = create_matrix(
        rows=_DEFAULT_ROWS,
        cols=_DEFAULT_COLS,
        min_value=_MIN_VALUE,
        max_value=_MAX_VALUE
    )
    print(get_text_color('\nИсходная матрица', COLOR_GREEN))
    print_matrix(matrix=matrix, select_negative=True)
