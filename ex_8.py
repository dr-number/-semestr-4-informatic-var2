from helpers import (
    get_text_color, input_number, COLOR_GREEN, COLOR_FAIL, COLOR_WHITE
)
_DEFAULT_DIMENSION = 5
_MAX_DIMENSION = 100

def _input_odd_number(text: str, default_value: float = None, max: float = None) -> float:
    while True:
        number = input_number(text=text, default_value=default_value, min=1, max=max)
        if number % 2 != 0:
            return number
        else:
            print(get_text_color(f"Число должно быть нечетным!", COLOR_FAIL))

def _print_matrix(matrix):
    if not matrix:
        print(get_text_color(f"Матрица пуста!", COLOR_FAIL))
        return

    rows = len(matrix)
    cols = len(matrix[0])
    format_print = '| {:5} '*cols + '|'


    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            value = matrix[i][j]
            if value == 0:
                row.append(get_text_color(value, COLOR_GREEN))
            else:
                row.append(get_text_color(value, COLOR_WHITE))

        print(format_print.format(*row))

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

    matrix = [[1] * dimension for _ in range(dimension - 2)]
    outer_rows = [0] * dimension
    index_middle = int(dimension / 2)
    outer_rows[index_middle] = 1
    matrix.insert(0, outer_rows)
    matrix.append(outer_rows)
    
    for i in range(1, dimension):
        if i != index_middle and i != dimension - 1:
            matrix[i][0] = 0
            matrix[i][dimension - 1] = 0

    matrix[index_middle][index_middle] = 0

    print(get_text_color('\nКонечная матрица', COLOR_GREEN))
    _print_matrix(matrix=matrix)
