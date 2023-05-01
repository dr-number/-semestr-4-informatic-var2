from helpers import get_text_color, input_number, COLOR_WARNING, COLOR_GREEN, COLOR_FAIL

def init():
    print(
        f'Вычислить уровень расчетной рентабельности по формуле: {get_text_color("Kpp = P/T", COLOR_GREEN)} где\n'
        f'{get_text_color("P = Pб - Pfe - Pf - Pk", COLOR_GREEN)};\n'
        f'{get_text_color("T = F1 + En + Vn", COLOR_GREEN)}\n\n'
        f'{get_text_color("Pб", COLOR_GREEN)} - балансовая прибыль;\n'
        f'{get_text_color("Pfe", COLOR_GREEN)} - плата за фонды;\n'
        f'{get_text_color("Pf", COLOR_GREEN)} - финансируемые платежи;\n'
        f'{get_text_color("Pk", COLOR_GREEN)} - процент за кредит;\n'
        f'{get_text_color("F1", COLOR_GREEN)} - средняя стоимость основных фондов;\n'
        f'{get_text_color("En", COLOR_GREEN)} - нормируемые оборотные средства;\n'
        f'{get_text_color("Vn", COLOR_GREEN)} - сверхплановые запасы неустановленного оборудования.\n\n'
    )
    