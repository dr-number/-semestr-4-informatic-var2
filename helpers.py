import random

COLOR_GREEN = '\033[92m'
COLOR_WARNING = '\033[93m'
COLOR_OKCYAN = '\033[96m'
COLOR_FAIL = '\033[91m'
COLOR_WHITE = '\033[37m'
_COLOR_ENDC = '\033[0m'

_MATRIX_MIN_ROWS = 2
_MATRIX_MAX_ROWS = 2
_MATRIX_MIN_COLS = 10
_MATRIX_MAX_COLS = 10

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(str)-> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False
        
def input_number(text: str, default_value: float = None, min: float = None, max: float = None)-> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '':
            if default_value is not None:
                return default_value
            else:
                print(get_text_color(f"Введите число!", COLOR_FAIL))
        elif is_number(number):
            if min is not None and float(number) < min:
                print(get_text_color(f"Минимально допустимое число - {min}!", COLOR_FAIL))
            elif max is not None and float(number) > max:
                print(get_text_color(f"Максимально допустимое число - {max}!", COLOR_FAIL))
            else:
                return float(number)
        else:
            print(get_text_color(f"\"{number}\" - не число! Повторите ввод!", COLOR_FAIL))
            
    return 0.0

def is_question(text: str)-> bool:
    return input(f'{get_text_color(text, COLOR_WARNING)} [Y/n]: ').lower() != 'n' 

def create_matrix(rows: int, cols: int, min_value: int, max_value: int):
    result = []
    is_hand = is_question('Ввести матрицу вручную?')
    if not is_hand:
        for i in range(0, rows):
            row = []
            for j in range(0, cols):
                row.append(int(random.uniform(min_value, max_value)))
            result.append(row)
        return result

    rows = int(input_number(
        text=f'Введите количество строк: (по умолчанию {rows})',
        default_value=rows,
        min=_MATRIX_MIN_ROWS,
        max=_MATRIX_MAX_ROWS
    ))
    cols = int(input_number(
        text=f'Введите количество строк: (по умолчанию {cols})',
        default_value=cols,
        min=_MATRIX_MIN_COLS,
        max=_MATRIX_MAX_COLS
    ))

    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(
                int(
                    input_number(
                        text=f'Введите значение (ряд {i + 1} из {rows}, столбец {j + 1} из {cols}): ', 
                        min=min_value,
                        max=max_value
                    )
                )
            )
        result.append(row)
    return result

def print_matrix(
    matrix, 
    select_positive: bool = False, 
    select_negative: bool = False,
    select_zero: bool = False,
    ):
    if not matrix:
        print(get_text_color(f"Матрица пуста!", COLOR_FAIL))
        return

    rows = len(matrix)
    cols = len(matrix[0])
    print(matrix[0])

    format_print = '| {:10} '*(cols + 1)
    format_print += '|'
    print(format_print)

    header = ['']
    for j in range(1, cols):
        header.append(f'[{j}]')
    print(format_print.format(*header))

    for i in range(1, rows):
        row = [f'[{j}]']
        for j in range(1, cols):
            value = matrix[i][j]
            if select_negative and value < 0:
                row.append(get_text_color(value, COLOR_FAIL))
            elif select_positive and value > 0:
                row.append(get_text_color(value, COLOR_GREEN))
            elif select_zero and value == 0:
                row.append(get_text_color(value, COLOR_WARNING))
            else:
                row.append(str(value))

            print(format_print.format(*row))

