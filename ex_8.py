from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

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
