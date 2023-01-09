from random import randint

for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim!')


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    numero_sorteado = sortear_dado()
    if numero_sorteado % 2 != 0:
        continue
    elif i == numero_sorteado:
        print('ACERTOU', i)
        break
else:
    print('Não acertou o numero!')
