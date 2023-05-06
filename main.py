from helpers import get_text_color, COLOR_WARNING, COLOR_FAIL
import ex_1, ex_2, ex_3, ex_4, ex_5, ex_6, ex_7, ex_8

_EX_1 = '1'
_EX_2 = '2'
_EX_3 = '3'
_EX_4 = '4'
_EX_5 = '5'
_EX_6 = '6'
_EX_7 = '7'
_EX_8 = '8'

_ARRAY_EX = {
    _EX_1: ex_1, 
    _EX_2: ex_2,  
    _EX_3: ex_3,  
    _EX_4: ex_4,  
    _EX_5: ex_5, 
    _EX_6: ex_6, 
    _EX_7: ex_7, 
    _EX_8: ex_8
}

def main():
    while True:
        print(
            "\nЛарионов гр. 210з. Информатика. Индивидуальное задание № 2. Вариант 14.\n"
            "Какую задачу выполнить: \n"
            f"{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}Вычислить на заданном интервале значения функции\n"
            f"{get_text_color(f'{_EX_2}) ', COLOR_WARNING)}Вычислить произведение всех элементов последовательности.\n"
            f"{get_text_color(f'{_EX_3}) ', COLOR_WARNING)}Найти количество элементов последовательности, которые меньше 0.3\n"
            f"{get_text_color(f'{_EX_4}) ', COLOR_WARNING)}\n"
            # f"{get_text_color(f'{_EX_5}) ', COLOR_WARNING)}Вычислить значения функции\n"
            f"{get_text_color(f'{_EX_6}) ', COLOR_WARNING)}Дана матрицa B 3*3. Заменить отрицательные элементы матрицы нулями\n"
            f"{get_text_color(f'{_EX_7}) ', COLOR_WARNING)}\n"
            f"{get_text_color(f'{_EX_8}) ', COLOR_WARNING)}\n"
        )
        select = input('Для выхода введите \'0\'\n')

        if select in _ARRAY_EX:
            getattr(_ARRAY_EX[select], 'init')()
        elif select == '0':
            break
        else:
            print(
                f'{get_text_color("Введен неверный номер задачи!", COLOR_FAIL)}'
            )

if __name__ == '__main__':
    main()
