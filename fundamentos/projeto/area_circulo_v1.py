from math import pi
import sys

'''
PI = 3.14
raio = 15
area_circunferencia = PI * (raio ** 2)
print(f'A area da circunferencia do raio {raio} é : {area_circunferencia}')


# print(dir())
raio = 15
area_circunferencia = pi * (raio ** 2)
print(f'A area da circunferencia do raio {raio} é : {area_circunferencia}')

if __name__ == '__main__':
    raio = float(input('Informe o raio:'))
    area_circunferencia = pi * (raio ** 2)
    print(f'A area da circunferencia do raio {raio} é : {area_circunferencia}')




def circulo(raio):
    return pi * (raio ** 2)


if __name__ == '__main__':
    raio = float(input('Informe o raio:'))
    area_circunferencia = circulo(raio)
    print(f'A area da circunferencia do raio {raio} é : {area_circunferencia}')
    
'''


def circulo(raio):
    return pi * (raio ** 2)


def help():
    print('É necessário informar o raio do círculo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    elif not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numerico')
    else:
        raio = sys.argv[1]
        area_circunferencia = circulo(raio)
        print(
            f'A area da circunferencia do raio {raio} é : {area_circunferencia}')
