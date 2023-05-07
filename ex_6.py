from helpers import create_matrix, print_matrix, get_text_color, COLOR_GREEN, COLOR_FAIL, COLOR_WARNING

_DEFAULT_ROWS = 3
_DEFAULT_COLS = 3
_MIN_VALUE = -20
_MAX_VALUE = 20

def init():
    print(get_text_color(
        'Дана матрицa B 3*3\nЗаменить отрицательные элементы матрицы нулями. На печать вывести исходную и полученную матрицы.\n',
        COLOR_WARNING)
    )
    matrix = create_matrix(
        rows=_DEFAULT_ROWS,
        cols=_DEFAULT_COLS,
        min_value=_MIN_VALUE,
        max_value=_MAX_VALUE
    )
    if not matrix:
        return

    print(get_text_color('\nИсходная матрица', COLOR_GREEN))
    print_matrix(matrix=matrix, select_negative=True, select_zero=True)

    rows = len(matrix)
    cols = len(matrix[0])
    count_replace_elements = 0

    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
                count_replace_elements += 1

    print(get_text_color('\nКонечная матрица', COLOR_GREEN))
    print_matrix(matrix=matrix, select_zero=True)

    if count_replace_elements == 0:
        print(get_text_color(f"\nВ исходной матрице нет отрицательных элементов!", COLOR_FAIL))
    else:
        print(f"\nЗаменено {get_text_color(str(count_replace_elements), COLOR_GREEN)} отрицательных элементов")
