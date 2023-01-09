trabalho_terca = False
trabalho_quinta = False

if trabalho_terca and trabalho_quinta:
    print('TV 50 + Sorvete')
elif trabalho_terca or trabalho_quinta:
    print('TV 32 + sorvete')
else:
    print('Fica em casa')


tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca or trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saudavel = not sorvete

print("TV50 = {}  TV32 = {}  Sorvete = {}   Saudável = {}".format(tv_50, tv_32, sorvete, mais_saudavel))

# print(5.0.is_integer())
# print(1.1 + 2.2)

from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))

getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print(1.1 + 2.2)
print(Decimal(1.1) + Decimal(2.2))