from helpers import get_text_color, input_number, print_matrix, COLOR_GREEN, COLOR_FAIL
_DEFAULT_DIMENSION = 5
_MAX_DIMENSION = 100


def _transpose(matrix):
    return [list(i) for i in zip(*matrix)]

def _input_odd_number(text: str, default_value: float = None, max: float = None) -> float:
    while True:
        number = input_number(text=text, default_value=default_value, min=1, max=max)
        if number % 2 == 0:
            return number
        else:
            print(get_text_color(f"Число должно быть нечетным!", COLOR_FAIL))

def init():
    example = (
        "    | 0 0 1 0 0 |\n"
        "    | 0 1 1 1 0 |\n"
        "M = | 1 1 0 1 1 |\n"
        "    | 0 1 1 1 0 |\n"
        "    | 0 0 1 0 0 |\n"
    )
    print(
        'Сформировать двумерный массив M(n,n) (где n - нечетное число) таким образом, чтобы "углы" ' 
        'и "центр" были заполнены нулями, а остальные элементы должны быть равны 1, т.е\n'
        f'{get_text_color(example, COLOR_GREEN)}\n'
    )

    dimension = int(_input_odd_number(
        text=f'Введите размерность квадратной матрицы: (по умолчанию {_DEFAULT_DIMENSION})', 
        default_value=_DEFAULT_DIMENSION,
        max=_MAX_DIMENSION
    ))

    matrix = [[1] * dimension] * dimension
    outer_rows = [0] * dimension
    index_middle = dimension / 2 + 1
    outer_rows[index_middle] = 1
    matrix[0] = outer_rows
    matrix[dimension] = outer_rows
    matrix = _transpose(matrix=matrix)
    matrix[0] = outer_rows
    matrix[dimension] = outer_rows
    matrix[index_middle][index_middle] = 0

    print(get_text_color('\nКонечная матрица', COLOR_GREEN))
    print_matrix(matrix=matrix, select_zero=True)
