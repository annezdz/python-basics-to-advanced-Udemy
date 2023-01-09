def getConcept():
    global conceito
    if __name__ == '__main__':
        nota = float(input('Informe uma nota: '))
        if nota < 0 or nota > 10:
            print('Nota Inválida')
        elif 9.0 < nota <= 10.0:
            conceito = 'A'
        elif nota > 8.0:
            conceito = 'A-'
        elif nota > 7.0:
            conceito = 'B'
        elif nota > 6.0:
            conceito = 'B-'
        elif nota > 5.0:
            conceito = 'C'
        elif nota > 4.0:
            conceito = 'C-'
        elif nota > 3.0:
            conceito = 'D'
        elif nota > 2.0:
            conceito = 'D-'
        elif nota > 1.0:
            conceito = 'E'
        else:
            conceito = 'E-'
    else:
        print('Package inválido')
    return conceito


resultado = getConcept()
print(resultado)
