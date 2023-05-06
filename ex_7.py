from helpers import get_text_color, create_matrix, print_matrix, COLOR_GREEN, COLOR_WARNING

_DEFAULT_ROWS = 3
_DEFAULT_COLS = 5
_MIN_VALUE = -20
_MAX_VALUE = 20

def _sum_positive_col(matrix, col)-> int:
    rows = len(matrix)
    _sum = 0
    for i in range(0, rows):
        if matrix[i][col] > 0:
            _sum += matrix[i][col]

    return _sum

def init():
    print(
        'Дана матрица A(3,5):\n'
        'Вычислить элементы массива Y по правилу:\n'
        f'{get_text_color("y[j] = Sin(x[j])", COLOR_GREEN)}, где\n'
        'x[j] - сумма положительных элементов j-го столбца матрицы A.\n'
    )
    matrix = create_matrix(
        rows=_DEFAULT_ROWS,
        cols=_DEFAULT_COLS,
        min_value=_MIN_VALUE,
        max_value=_MAX_VALUE
    )
    if not matrix:
        return

    print(get_text_color('\nМатрица A', COLOR_GREEN))
    print_matrix(matrix=matrix)

    rows = len(matrix)
    cols = len(matrix[0])

    row = []
    for j in range(0, cols):
        row.append(_sum_positive_col(matrix=matrix, col=j))
    result_1 = [row]
    

    print(get_text_color('\nПромежуточный результат (без функции Sin)', COLOR_WARNING))
    print_matrix(matrix=result_1)
