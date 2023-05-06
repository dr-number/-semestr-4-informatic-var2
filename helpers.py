COLOR_GREEN = '\033[92m'
COLOR_WARNING = '\033[93m'
COLOR_OKCYAN = '\033[96m'
COLOR_FAIL = '\033[91m'
COLOR_WHITE = '\033[37m'
_COLOR_ENDC = '\033[0m'

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(str)-> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False
        
def input_number(text: str, default_value: float, min: float = None, max: float = None)-> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '':
            return default_value
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
