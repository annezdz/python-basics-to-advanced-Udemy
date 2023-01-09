palavra = 'paralelepidedo'

# Exemplo com String
for letra in palavra:
    print(letra, end=',')
print('fim')

# Exemplo com lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

# Exemplo com tupla

dias_da_semana = (
'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in dias_da_semana:
    print(f'Hoje é {dia}')

# Exemplo com SET

for letra in set('muito legal'):
    print(letra)