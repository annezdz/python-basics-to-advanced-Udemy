def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return dias.get(dia, '** dia inválido')


for dia in range(0, 9):
    print(f'{dia}: {get_dia_semana(dia)}')


def get_dia(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return dias.get(dia, '** dia inválido')


def is_holiday(dia):
    if dia == 'Domingo' or dia == 'Sábado':
        print(f'{dia} is Holiday')
    else:
        print(f'{dia} is not holiday')


for dia in range(1, 9):
    is_holiday(get_dia(dia))
