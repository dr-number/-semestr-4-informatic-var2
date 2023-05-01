COLOR_GREEN = '\033[92m'
COLOR_WARNING = '\033[93m'
COLOR_FAIL = '\033[91m'
_COLOR_ENDC = '\033[0m'

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(str)-> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False
        
def input_number(text: str, default_value: float)-> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '':
            return default_value
        elif is_number(number):
            return float(number)
        else:
            print(get_text_color(f"\"{number}\" - не число! Повторите ввод!", COLOR_FAIL))
            
    return 0.0

def print_table(table):
    if not table:
        return

    size_cols = []
    head = table[0]
    size = len(head)

    for item in head:
        size_cols.append(len(item))

    if size <= 1:
        return

    for row in head:
        for i in range(0, size):
            if size_cols[i] < len(row[i]):
                size_cols[i] = len(row[i])

    for i in range(0, size):
        size_cols[i] = size_cols[i] + 4
