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
        for i in range(1, rows):
            row = []
            for j in range(1, cols):
                row.append(random.uniform(min_value, max_value))
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

    for i in range(1, rows):
        row = []
        for j in range(1, cols):
            row.append(
                int(
                    input_number(
                        text=f'Введите значение (ряд {i} из {rows}, столбец {j} из {cols}): ', 
                        min=min_value,
                        max=max_value
                    )
                )
            )
        result.append(row)
    return result

    
