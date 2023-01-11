def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    dia_escolhido = (tipo_dia for numero_dia, tipo_dia in dias.items() if
                     dia in numero_dia)
    return next(dia_escolhido, '***  dia inválido ***')


for dia in range(0, 9):
    print(f'Dia - {dia} é {get_tipo_dia(dia)}')
