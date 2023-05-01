from helpers import get_text_color, COLOR_WARNING, COLOR_FAIL
import ex_1, ex_2, ex_3, ex_4, ex_5

_EX_1 = '1'
_EX_2 = '2'
_EX_3 = '3'
_EX_4 = '4'
_EX_5 = '5'

_ARRAY_EX = {
    _EX_1: ex_1, 
    _EX_2: ex_2,  
    _EX_3: ex_3,  
    _EX_4: ex_4,  
    _EX_5: ex_5 
}

def main():
    while True:
        print(
            "\nЛарионов гр. 210з. Информатика. Индивидуальное задание № 1. Вариант 14.\n"
            "Какую задачу выполнить: \n"
            f"{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}Вычислить уровень расчетной рентабельности\n"
            f"{get_text_color(f'{_EX_2}) ', COLOR_WARNING)}Вычислить значение F = y + 5.6\n"
            f"{get_text_color(f'{_EX_3}) ', COLOR_WARNING)}Вычислить значение y = f + a\n"
            f"{get_text_color(f'{_EX_4}) ', COLOR_WARNING)}Вычислить значение s\n"
            f"{get_text_color(f'{_EX_5}) ', COLOR_WARNING)}Определить, лежит ли точка с координатами (x,y) внутри квадрата\n"
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
